import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

# Leer la base de datos
survey = pd.read_csv('survey_results_public.csv')

# Quedarse con las columnas necesarias unicamente
survey = survey[['Salary', 'Gender', 'Race', 'Country', 'DeveloperType', 
                 'YearsCodedJob', 'FormalEducation', 'HaveWorkedLanguage']]

# Eliminar rows que no contengan salario
survey = survey[pd.notnull(survey['Salary'])]

# Simplificar Gender añadiendo nueva columna
def simplify_gender(df):
    conditions_gender = [(df['Gender'] == 'Male'),
                         (df['Gender'] == 'Female'),
                         (df['Gender'] != 'Male') & (df['Gender'] != 'Female') 
                         & (pd.isnull(df['Gender']) == False)]
    choices_gender = ['Male', 'Female', 'Other']
    df['Gender_New'] = np.select(conditions_gender, choices_gender, default = np.NaN)
    return df

# Aplicar funcion a df
survey = simplify_gender(survey)

# Convertir YearsCodedJob a numérico
def convert_coding(df, col, new_col):
    conditions_coding = [(df[col] == '1 to 2 years'),
                         (df[col] == '2 to 3 years'),
                         (df[col] == '3 to 4 years'),
                         (df[col] == '4 to 5 years'),
                         (df[col] == '5 to 6 years'),
                         (df[col] == '6 to 7 years'),
                         (df[col] == '7 to 8 years'),
                         (df[col] == '8 to 9 years'),
                         (df[col] == '9 to 10 years'),
                         (df[col] == '10 to 11 years'),
                         (df[col] == '11 to 12 years'),
                         (df[col] == '12 to 13 years'),
                         (df[col] == '13 to 14 years'),
                         (df[col] == '14 to 15 years'),
                         (df[col] == '15 to 16 years'),
                         (df[col] == '16 to 17 years'),
                         (df[col] == '17 to 18 years'),
                         (df[col] == '18 to 19 years'),
                         (df[col] == '19 to 20 years'),
                         (df[col] == '20 or more years')]
    choices_coding = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21]
    df[new_col] = np.select(conditions_coding, choices_coding, default = np.NaN)    
    return df
# Apply function to subsets
survey = convert_coding(survey, 'YearsCodedJob', 'YearsCodedJobNum')

# Convertir YearsCodedJob a numérico
def convert_education(df, col, new_col):
    conditions_education = [(df[col] == 'I prefer not to answer'),
                         (df[col] == 'I never completed any formal education'),
                         (df[col] == 'Primary/elementary school'),
                         (df[col] == 'Secondary school'),
                         (df[col] == 'Some college/university study without earning a bachelor\'s degree'),
                         (df[col] == 'Professional degree'),
                         (df[col] == 'Bachelor\'s degree'),
                         (df[col] == 'Master\'s degree'),
                         (df[col] == 'Doctoral degree')]
    choices_coding = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    df[new_col] = np.select(conditions_education, choices_coding, default = np.NaN)    
    return df
# Apply function to subsets
survey = convert_education(survey, 'FormalEducation', 'FormalEducationNum')

# definir los calculos necesarios
def ComputeFiveNumbers(df, col):
    df = df.groupby([col])
    minimum         = df.min().sort_values('Salary')
    first_quartile  = df.quantile(0.25).sort_values('Salary')
    median          = df.quantile(0.5).sort_values('Salary')
    third_quartile  = df.quantile(0.75).sort_values('Salary')
    maximum         = df.max().sort_values('Salary')
    return minimum, first_quartile, median, third_quartile, maximum

def ComputeStats(df, col):
    df      = df.groupby([col])
    mean    = df.mean().sort_values('Salary')
    std     = df.std().sort_values('Salary')
    return mean, std

# Crear df con valores separados, con salario
def split_list(df, col):
    in_sal = list(df['Salary'])
    in_list = list(df[col])
 
    out_sal = []
    out_list = []
    for i in range(len(in_list)):
        if pd.isnull(in_list[i]) == False:
            # vals = in_list[i].split(';')
            vals = [x.strip() for x in in_list[i].split(';')]
            sal = [in_sal[i]]*len(vals)
            
            out_list.append(vals)
            out_sal.append(sal)
    out_df = pd.DataFrame({'Salary': list(np.concatenate(out_sal)), col: list(np.concatenate(out_list))})
    return out_df

# Definir funcion para boxplot
def boxplot(df, col):
    bp = df.boxplot(column='Salary', by=col)
    axes = pl.gca()
    pl.show()

# Crear dataframes para funciones
gender_survey = survey[['Salary', 'Gender_New']]
races_survey = split_list(survey, 'Race')

devtype_survey = split_list(survey, 'DeveloperType')
country_survey = survey[['Salary', 'Country']]

experience_salary_survey = survey[['YearsCodedJobNum', 'Salary']]
education_salary_survey = survey[['FormalEducationNum', 'Salary']]
languages_survey = split_list(survey, 'HaveWorkedLanguage')


 # a
## Calculos para género
#print(ComputeFiveNumbers(gender_survey, 'Gender_New'))
#print(ComputeStats(gender_survey, 'Gender_New'))
## Boxplot para Gender
#boxplot(gender_survey, 'Gender_New')

# # b
# # Calculos por raza
print(ComputeFiveNumbers(races_survey, 'Race'))
print(ComputeStats(races_survey, 'Race'))
# Boxplot para Race
boxplot(races_survey, 'Race')

# # c
# # Calculos por DeveloperType
# print(ComputeFiveNumbers(devtype_survey, 'DeveloperType'))
# print(ComputeStats(devtype_survey, 'DeveloperType'))
# # Boxplot para DevType
# boxplot(devtype_survey, 'DeveloperType')

# d
# Calculos por Country
# print(ComputeStats(country_survey, 'Country'))

# # e 
# # Grafica de barra de respuesta por paises
# frequency_country_survey = country_survey['Country'].value_counts()
# frequency_country_survey.plot.bar()
# pl.show()

# # f
# # correlacion entre experiencia y salario
# print(experience_salary_survey.corr(method='pearson'))

# # g
# # Correlacion entre educacion y salario
# print(education_salary_survey.corr(method='pearson'))

# # h
# # Grafica de barra de frecuencia de uso de lenguajes
# frequency_languages_survey = languages_survey['HaveWorkedLanguage'].value_counts()
# frequency_languages_survey.plot.bar()
# pl.show()