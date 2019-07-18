# Cuantas aulas hay en la escuela
aulas = 100
# Cuantos alumnos caben en cada aula
cupo_del_aula = 30
# Docentes que trabajan en la escuela
docentes = 55
# Cantidad de alumnos
alumnos = 500

# Aulas sin docente
aulas_vacias = aulas - docentes
# aulas = aulas - 50 
# Aulas con docente
aulas_llenas = docentes
# Capacidad máxima de alumnos en aulas
capacidad_maxima_de_alumnos = aulas_llenas * cupo_del_aula
# Cantidad promedio de alumnos por aula
promedio_alumnos_por_aula = alumnos / aulas_llenas

print("Hay", aulas, "aulas disponibles.")
print("Solo hay", docentes, "docentes disponibles.")
print("Habrán", aulas_vacias, "aulas vacias.")
print("Podemos dar clases a", capacidad_maxima_de_alumnos, "alumnos cómo máximo.")
print("Tenemos", alumnos, "asistiendo.")
print("Necesitamos tener", promedio_alumnos_por_aula, "en cada aula.")

