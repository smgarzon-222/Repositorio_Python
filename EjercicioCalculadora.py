# Diseñar un programa que solicite numeros y que pida la operacion matematica a realizar.
print("Ingrse el primer numero")
numero1 = float(input())
print ('''Ingrese la operacion que desea realizar suma (+), resta (-), multiplicacion (*), division (/), potenciacion (**): ''')
operacion = input()
print("Ingrse el segundo numero")
numero2 = float(input())
if operacion == "+":
    operacion = numero1 + numero2
    print("La suma es igual a: ", operacion)
elif operacion == "-":
    operacion == numero1 - numero2
    print("La resta es igual a: ", operacion)
elif operacion == "*":
    operacion = numero1 * numero2
    print("La multiplicacion es igual a: ", operacion)
elif operacion == "/":
    operacion = numero1 / numero2
    print("La division es igual a: ", operacion)
elif operacion == "**":
    operacion = numero1 ** numero2
    print("La potenciacion es igual a: ", operacion)
else:
    print("La operación introducida es incorrecta. ") 

