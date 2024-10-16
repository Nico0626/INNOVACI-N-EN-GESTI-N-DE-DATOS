import re
import aritmetica
import random
import json
import time
import captcha
from colorama import Fore, Style 
import pickle
import os

def logo():
    # Generador ASCII de https://www.freetool.dev/es/generador-de-letras-ascii
    # Tipo de letra PAGGA
    print(Style.BRIGHT + Fore.CYAN + '''
░█░░░▀█▀░█▀▄░█▀▄░█▀▀░█▀▄░▀█▀░█▀█
░█░░░░█░░█▀▄░█▀▄░█▀▀░█▀▄░░█░░█▀█
░▀▀▀░▀▀▀░▀▀░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀
░▀█▀░█▀▀░█░█░█▀█░█▀▄░█▀█░█░█░█░█
░░█░░▀▀█░█░█░█░█░█░█░█░█░█▀▄░█░█
░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀

--------------------------------------------------
''')

def bienvenida():
    logo()
    print("************************************************")
    print("Bienvenido al sistema de Gestion de libros de la libreria Azteca")
    print("************************************************")
    
class Usuario:
    
    next_id = 1
    
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        Usuario.next_id += 1
        
        
        
    @classmethod
    def __repr__(self):
        #Returna el usuario en str y no en un objeto inentendible
        return f"Usuario: {self.id}, username: {self.username}, email: {self.email}"
    
    @classmethod
    def traer_usuario(cls):
        #Trae los usuarios en el archivo y en caso de no tener, trae lista vacia  
        if os.path.exists('usuario.ispc'):
            with open('usuario.ispc', 'rb') as file:
                return pickle.load(file)
        return []
    
    @classmethod
    def guardar_usuarios(cls, usuarios):
        #Guarda los usuarios en el archivo
        with open('usuario.ispc', 'wb') as file:
            pickle.dump(usuarios, file)  
            
    @classmethod
    def crear_usuarios(cls, username, password, email):
        usuarios = cls.traer_usuario()  # Traer usuarios existentes
        nuevo_usuario = cls(Usuario.next_id, username, password, email)  # Crea un nuevo usuario con el siguiente ID disponible
        usuarios.append(nuevo_usuario)
        cls.guardar_usuarios(usuarios)
        print(f"Usuario {username} creado exitosamente")
        
    @classmethod
    def obtener_usuario(cls, user_id):
        """Obtiene un usuario por su ID"""
        usuarios = cls.cargar_usuarios()
        for usuario in usuarios:
            if usuario.id == user_id:
                return usuario
        print(f"Usuario con ID {user_id} no encontrado.")
        return None

    @classmethod
    def actualizar_usuario(cls, user_id, username=None, password=None, email=None):
        """Actualiza los datos de un usuario por su ID"""
        usuarios = cls.cargar_usuarios()
        for usuario in usuarios:
            if usuario.id == user_id:
                if username:
                    usuario.username = username
                if password:
                    usuario.password = password
                if email:
                    usuario.email = email
                cls.guardar_usuarios(usuarios)
                print(f"Usuario con ID {user_id} actualizado.")
                return
        print(f"Usuario con ID {user_id} no encontrado.")

    @classmethod
    def eliminar_usuario(cls, user_id):
        """Elimina un usuario por su ID"""
        usuarios = cls.cargar_usuarios()
        usuarios = [usuario for usuario in usuarios if usuario.id != user_id]
        cls.guardar_usuarios(usuarios)
        print(f"Usuario con ID {user_id} eliminado.")
            
        
        
        
class Acceso:
    def __init__(self, idAcceso, fechaIngreso, fechaSalida, id):
        self.idAcceso = idAcceso
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.id = id
        

        
    
def login():
    intentos = 0
    usuarios = Usuario.traer_usuario()
    while True:
        print("Para Ingresar al sistema porfavor ingrese \n.1_Para ingresar usuario y contraseña\n.2_Si olvido su contraseña\n3_Salir")
        opcion = input("Ingrese su opción: ")
        
        
        if opcion == "1":
            username=input("Usuario: ")
            password=input("Contraseña: ")
            
            # Verificar credenciales
            for usuario in usuarios:
                if usuario.username == username and usuario.password == password:
                    print("Bienvenido al sistema de biblioteca.")
                    return usuario

            intentos += 1
            print(f"Credenciales incorrectas. Intento {intentos}.")
            if intentos == 4:
                print("Superó el número de intentos permitidos.")
                with open('UsuarioBloqueado.txt', 'w') as archivo:
                    archivo.write(f"{username} ha sido bloqueado después de 4 intentos.")
                return None

        elif opcion == "2":
            olvidar_contraseña()
            return None
        elif opcion == "3":
            print("Saliendo del sistema.")
            break

def olvidar_contraseña():
    print("Por favor contacte al administrador para recuperar su contraseña.")
    

def registro_usuario(usuarios):
    while True:
        username = input("Ingrese su nombre de usuario (6-12 caracteres): ")
        if 6 <= len(username) <= 12 and username not in [u.username for u in usuarios]:
            break
        print("El nombre de usuario no cumple los requisitos o ya está en uso.")
        
    while True:
        password = input("Ingrese su clave (mínimo 8 caracteres, incluyendo minúsculas, mayúsculas, números y caracteres especiales): ")
        if validar_clave(password):
            break
        print("La clave no cumple los requisitos.")      
        
    email = input("Ingrese su correo: ")
    
    return username, password, email  # Retornar los datos del nuevo usuario

        
def validar_clave(clave):
        if len(clave) < 8:
            return False
        if not re.search(r"[a-z]", clave):
            return False
        if not re.search(r"[A-Z]", clave):
            return False
        if not re.search(r"[0-9]", clave):
            return False
        if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", clave):
            return False
        return True
    

def anotar_txt(usuarios):
    with open('UsuariosCreados.txt', 'w') as archivo:
        archivo.write(json.dumps(usuarios, indent=4))
        
def ingresotxt(nombre_usuario):
    tiempo_actual = time.localtime()
    tiempo =f"fecha: {tiempo_actual.tm_year}/{tiempo_actual.tm_mon}/{tiempo_actual.tm_mday} hora: {tiempo_actual.tm_hour}:{tiempo_actual.tm_min}"
    mensaje_completo =f"Nombre de usuario: {nombre_usuario} {tiempo}"
    with open('ingresotxt.txt', 'w') as archivo:
        archivo.write(mensaje_completo)
        
    
def main():
    usuarios = Usuario.traer_usuario()
    while True:
        bienvenida()
        print("\n1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Salir")
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            captcha.resolver_captcha()
            usuario = login()
            if usuario:
                print(f"Sesión iniciada como {usuario.username}")
                ingresotxt(usuario.username)
            break
        elif opcion == "2":
            captcha.resolver_captcha()
            username,password,email=registro_usuario(usuarios)
            Usuario.crear_usuarios(username, password, email)
            anotar_txt(usuarios)
        elif opcion == "3":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()
