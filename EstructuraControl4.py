# Escriba un programa que pida un nombre de usuario y una contraseña
# y si se ha introducido "pepe" y "asdasd" se indica "Has ingresado al sistema"
# sino se da un error.
usuario = input("Ingrese su usuario: ")
contrasena = input("Ingrese su contraseña: ")
if usuario == "jmorenog" and contrasena == "C0l0mb142022.":
    print("Has ingresado al sistema.")
else:
    print("Usuario//contraseña incorrecto.")