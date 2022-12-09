#Dados los catetos de un triangulo, calcular su hipotenusa.

import math
cateto1 = float(input("Introduce el cateto 1: "))
cateto2 = float(input("Ingrese el cateto 2: "))
hipotenusa = math.sqrt(cateto1 ** 2 +cateto2 ** 2)
#Coloca %.xf equivale a que ddespues del punto apareceran dos decimales,
#posteriormente se debe de colocar % para que aparezcan los decimales correspondientes como resultado en pantalla.
print("La hipotenusa es igual a %.2f: "% hipotenusa)