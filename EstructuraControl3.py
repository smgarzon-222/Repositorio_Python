# Escriba un algoritmo que pida un numero y que diga si es un positivo, negativo o 0.
numero1 = int(input("Dime un numero: "))
if numero1 == 0:
    print("Es igual a 0.")
elif numero1 > 0:
    print("El numero es positivo.")
else:
    print("Es negativo.")