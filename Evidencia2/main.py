from usuario import Usuario
import re
from colorama import Fore, Style
import menu2
from acceso import Acceso
import captcha


def login():
    intentos = 0
    usuarios = Usuario.traer_usuario()
    while True:
        print("Para Ingresar al sistema porfavor ingrese \n.1_Para ingresar usuario y contraseña\n.2_Si olvido su contraseña\n.3_Salir")
        opcion = input("Ingrese su opción: ")
        
        
        if opcion == "1":
            username=input("Usuario: ")
            captcha.resolver_captcha()
            password=input("Contraseña: ")
            
            for usuario in usuarios:
                if usuario.username == username and usuario.password == password:
                    Acceso.ingresotxt(username)
                    print("Bienvenido al sistema de biblioteca.")
                    while True:
                        print("1. Menu de Gestión de Usuarios")
                        print("2. Cerrar sesion")

                        opcion = input("Seleccione una opción: ")

                        if opcion == "1":
                            menu2.main()
                        elif opcion == "2":
                            acceso.ingresotxt(username)
                            main()
                            break
                        else:
                            print("Opción inválida, intente nuevamente.")

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
    
    return username, password, email  

        
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
    
    
        

def logo():
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
    print("Bienvenido al sistema de Gestion de libros de la libreria Azteca")

def main():
    usuarios = Usuario.traer_usuario()
    while True:
        bienvenida()
        print("\n1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Salir")
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            login()
            pass
        elif opcion == "2":
            username, password, email = registro_usuario(usuarios)
            Usuario.crear_usuarios(username, password, email)
        elif opcion == "3":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()