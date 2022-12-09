nota = float(input("Escribe tu nota: 5"))
if nota >= 1 and nota <= 2.9:
    print("Su nota es Deficiente.")
elif nota >= 3 and nota <= 4.9:
    print("Su nota es Insuficiente.")
elif nota >= 5 and nota <= 6.9:
    print("Su nota es Aceptable.")
elif nota >= 7 and nota <= 8.9:
    print("Su nota es Sobresaliente.")
elif nota >= 9 and nota <= 10:
    print("Su nota es Excelente.")
else:
    print("El valor introducido es incorrecto.")
print("Se cierra programa.")