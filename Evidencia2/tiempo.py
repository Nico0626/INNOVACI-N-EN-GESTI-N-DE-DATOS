import time

tiempo_actual = time.localtime()
print(f"fecha: {tiempo_actual.tm_year}/{tiempo_actual.tm_mon}/{tiempo_actual.tm_mday} \n hora: {tiempo_actual.tm_hour}:{tiempo_actual.tm_min}")
print(type(tiempo_actual))