# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales

nombre = input("Escribe tu nombre: ")
apellido1 = input("Escribe tu primer apellido: ")
apellido2 = input("Escribe tu segundo apellido: ")

inicial = nombre[0]
inicial = inicial + apellido1[0]
inicial = inicial + apellido2[0]

# Se usa el metodo upper para convertir a mayusculas
inicial = inicial.upper()

print("Las iniciales son: ", inicial)
