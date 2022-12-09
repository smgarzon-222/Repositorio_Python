# Un ciclista parte de la ciudad A a las HH horas, MM minutos y SS segundos 
# El tiempo de viaje hasta llegar a la ciudad B es de T segundos.
# Escribir un algoritmo que determine la hora de llegada a la ciudad.

horapartida = int(input("Ingrese la hora de salida: "))
minutopartida = int(input("Ingrese los minutos de salida: "))
Segundospartida = int(input("Ingrese los segundos de partida: "))
Segviaje = int(input("Tiempo que has tardado en segundos: "))

# Convertir la hora de salida a segundos
Seginicial = horapartida * 3600 + minutopartida * 60 +Segundospartida

# Le sumo los segundos que he tardado
segfinal = Seginicial + Segviaje

#Convierto los segundos totales a hora, minuto y segundo
horallegada = segfinal //3600
minutollegada = (segfinal % 3600) // 60
segundollegada = (segfinal % 3600) % 60

# Muestro la hora de llegada
print("Hora de llegada")
print(horallegada, ":", minutollegada, ":", segundollegada)