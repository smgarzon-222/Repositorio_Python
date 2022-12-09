# Un alumno desea saber cual será su calificación final en la materia, 
# dicha calificación se compone de los siguientes porcentajes:
# 1. 55% del promedio de sus tres calificaciones parciales.
# 2. 30% de la calificación del examen final.
# 3. 15% de la calificación de un trabajo final. 

import math
parcial1 = float(input("Ingrese la nota del parcial 1: "))
parcial2 = float(input("Ingrese la nota del parcial 2: "))
parcial3 = float(input("Ingrese la nota del parcial 3: "))
examenfinal = float(input("Ingrese la nota Examen final: "))
trabajofinal = float(input("Ingrese la nota Trabajo final: "))

promedio1 = (((parcial1 + parcial2 + parcial3) /3) *0.55)
promedio2 = examenfinal * 0.30
promedio3 = trabajofinal * 0.15
totalpromedio = promedio1 + promedio2 + promedio3

# Otra solucion del ejercicio:
# nota = ((parcial1 +parcial2 + parcial3) / 3) * 0.55 + 0.3 * examenfinal + 0.15 * trabajofinal

print("La nota de sus parciales es de %.2f: " % totalpromedio)
print("La nota final del examen final es %.2f: " % examenfinal)
print("La nota de su trabajo final es %.2f: " % trabajofinal)
print("Su calificacion final es de %.2f: " % totalpromedio)