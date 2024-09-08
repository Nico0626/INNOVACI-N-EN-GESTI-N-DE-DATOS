import re
import aritmetica
import random
import json
import time
import captcha
from colorama import Fore, Style 

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
    
    
def login(usuarios):
    intentos = 0
    while True:
        print("Para Ingresar al sistema porfavor ingrese \n.1_Para ingresar usuario y contraseña\n.2_Si olvido su contraseña\n3_Salir")
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            usuario=input("Usuario: ")
            contraseña=input("Contraseña: ")
        
        elif opcion == "2":
            olvidar_contraseña(usuarios,usuario)
            return
        elif opcion == "3":
            print("Saliendo del sistema")
            break
        
        if usuario in usuarios and usuarios [usuario]['clave'] == contraseña:
            print("Bienvenido Al sistema de biblioteca")
            return usuario            
        elif usuario in usuarios and usuarios [usuario]['clave'] != contraseña:
            intentos += 1
            print(f"Contraseña incorrecta, intento número {intentos}. Nuevamente ingrese su clave. Le recuerdo que solo tiene 4 intentos")
            if intentos == 3:
                contraseña_olvidada=input("¿Ha olvidado su contraseña? Responda 'si' o 'no': ")
                if contraseña_olvidada == "si":
                    olvidar_contraseña(usuarios, usuario)
                    intentos = 0
                else:
                    continue
            elif intentos == 4:
                print("Ha superado el número de intentos permitidos.")
                with open('UsuarioBloqueado.txt', 'w') as archivo:
                    msg = f"{usuario} ha sido bloqueado superando 4 intentos"
                    archivo.write(msg)
                return
        else:
            print("Usuario o contraseña incorrectos.")

def olvidar_contraseña(usuarios, usuario):
    print("Por favor contacte al administrador para recuperar su contraseña.")
    

def registro_usuario(usuarios):
    nombre =input("Ingrese su nombre: ")
    apellido =input("Ingrese su apellido: ")
    dni = input("Ingrese su dni: ")
    correo = input("Ingrese su correo: ")
    fecha_nacimiento = input("Ingrese su fecha nacimiento: ")
    
    while True:
        nombre_usuario = input("Ingrese su nombre de usuario(6-12 caracteres): ")
        if 6 <= len(nombre_usuario) <=12 and nombre_usuario not in usuarios:
            break
        print("El nombre de usuario no cumple los requisitos o ya está en uso.")
        
    while True:
        clave = input("Ingrese su clave (mínimo 8 caracteres, incluyendo minúsculas, mayúsculas, números y caracteres especiales): ")
        if validar_clave(clave):
            break
        print("La clave no cumple los requisitos.")      

    
    usuarios[nombre_usuario] = {
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni,
        'correo': correo,
        'fecha_nacimiento': fecha_nacimiento,
        'clave': clave
    }
    print("Usuario registrado con éxito.")     
        
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
    
    
# def captcha():
#     print("Para ingresar primero deberá responder esta pregunta para verificar que usted no es un robot")
#     a, b = 10, 20
#     operaciones = [(aritmetica.dividir(a,b), "/"),
#                    (aritmetica.multiplicar(a,b),"X"),
#                    (aritmetica.restar(a,b),"-"),
#                    (aritmetica.sumar(a,b),"+")]
    
#     operacion, nombre_operacion = random.choice(operaciones)
    
    
#     print(f"Responda esta operación: {a} {nombre_operacion} {b}")
#     while True:
#         try:
#             resultado = float(input("Responda aquí porfavor: "))
#             if resultado == operacion:
#                 print("Captcha correcto")
#                 return True
#             else:
#                 print("Captcha incorrecto. Intente nuevamente.")
#         except Exception:
#             print(f"Error, Ingrese un numero porfavor!")
            
def anotar_txt(usuarios):
    with open('UsuariosCreados.txt', 'w') as archivo:
        archivo.write(json.dumps(usuarios, indent=4))
        
def ingresotxt(nombre_usuario):
    tiempo_actual = time.localtime()
    tiempo =f"fecha: {tiempo_actual.tm_year}/{tiempo_actual.tm_mon}/{tiempo_actual.tm_mday} hora: {tiempo_actual.tm_hour}:{tiempo_actual.tm_min}"
    mensaje_completo =f"Nombre de usuario: {nombre_usuario} {tiempo}"
    with open('ingresotxt.txt', 'w') as archivo:
        archivo.write(mensaje_completo)
        
    
#main
usuarios = {}

while True:
    bienvenida()
    print("\n1. Iniciar sesión")
    print("\n2. Registrar usuario")
    print("\n3. Salir")
    opcion = input("\nSeleccione una opción (1 o 2): ")
    
    if opcion == "1":
        if captcha.resolver_captcha():
            usuario = login(usuarios)
            if usuario:
                ingresotxt(usuarios, usuario)
            break
    elif opcion == "2":
        if captcha.resolver_captcha():
            registro_usuario(usuarios)
            anotar_txt(usuarios)
    elif opcion == "3":
        print("Saliendo del sistema")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
