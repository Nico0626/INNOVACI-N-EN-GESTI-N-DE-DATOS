from colorama import Fore, Style
import time
import json

class Acceso:
    def __init__(self, idAcceso, fechaIngreso, fechaSalida, id):
        self.idAcceso = idAcceso
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.id = id

    def anotar_txt(self,usuarios):
        with open('UsuariosCreados.txt', 'w') as archivo:
            archivo.write(json.dumps(usuarios, indent=4))
            
    def ingresotxt(nombre_usuario):
        tiempo_actual = time.localtime()
        tiempo =f"fecha: {tiempo_actual.tm_year}/{tiempo_actual.tm_mon}/{tiempo_actual.tm_mday} hora: {tiempo_actual.tm_hour}:{tiempo_actual.tm_min}"
        mensaje_completo =f"Nombre de usuario: {nombre_usuario} {tiempo}"
        with open('ingresotxt.txt', 'w') as archivo:
            archivo.write(mensaje_completo)