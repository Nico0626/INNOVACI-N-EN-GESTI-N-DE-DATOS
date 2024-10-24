
from gestor_usuarios import GestorUsuarios
from acceso import Acceso
import time
from gestor_usuarios import GestorUsuarios
from colorama import Fore, Style
from usuario import Usuario
import RegistrosPluviales
import captcha

def logo():
    print(Style.BRIGHT + Fore.CYAN + """
    ░█░░░▀█▀░█▀▄░█▀▄░█▀▀░█▀▄░▀█▀░█▀█
    ░█░░░░█░░█▀▄░█▀▄░█▀▀░█▀▄░░█░░█▀█
    ░▀▀▀░▀▀▀░▀▀░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀
    ░▀█▀░█▀▀░█░█░█▀█░█▀▄░█▀█░█░█░█░█
    ░░█░░▀▀█░█░█░█░█░█░█░█░█░█▀▄░█░█
    ░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀

--------------------------------------------------
    """)



def menu_principal():
    while True:
        print("\n*** Menú Principal ***")
        logo()
        print("1. Agregar un nuevo usuario")
        print("2. Modificar un usuario")
        print("3. Eliminar un usuario")
        print("4. Buscar usuario")
        print("5. Mostrar todos los usuarios")
        print("6. Ordenar usuarios Burbuja")
        print("7. Ordenar usuarios paython")
        print("8. Registros pluviales")
        print("9. Ingresar al sistema")
        print("10. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            GestorUsuarios.agregar_usuario()
        elif opcion == "2":
            GestorUsuarios.modificar_usuario()
        elif opcion == "3":
            GestorUsuarios.eliminar_usuario()
        elif opcion == "4":
            user=input("Ingrese el usuario a encontrar: ")
            GestorUsuarios.buscar_usuario(user)
        elif opcion == "5":
            GestorUsuarios.mostrar_usuarios()

        elif opcion == "6":
            GestorUsuarios.ordenar_usuarios_burbuja()

        elif opcion == "7":
            GestorUsuarios.ordenar_usuarios_python()

        elif opcion == "8":
            RegistrosPluviales.main()



        elif opcion == "9":
            login()
        elif opcion == "10":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida, intente nuevamente.")

def login():
    username = input("Usuario: ")
    captcha.resolver_captcha()
    password = input("Contraseña: ")
    usuario = Usuario.buscar_usuario(username)

    if usuario and usuario._password == password:
        print("Ingreso exitoso.")
        Acceso.guardar_acceso(Acceso(usuario._username))
        while True:
            print("\n1. Volver al menú principal")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                break
            elif opcion == "2":
                print("Saliendo del sistema.")
                return
    else:
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Intento fallido: {username}\n")
        print("Credenciales incorrectas.")

if __name__ == "__main__":
    menu_principal()