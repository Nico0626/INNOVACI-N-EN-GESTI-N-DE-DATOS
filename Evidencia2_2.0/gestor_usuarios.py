from usuario import Usuario
import captcha


class GestorUsuarios:
    @staticmethod
    def agregar_usuario():
        username = input("Ingrese el nombre de usuario: ")
        captcha.resolver_captcha()

        password = input("Ingrese la contraseña: ")
        email = input("Ingrese el correo: ")
        Usuario.crear_usuario(username, password, email)

    @staticmethod
    def modificar_usuario():
        user_id = int(input("Ingrese el ID del usuario a modificar: "))
        username = input("Nuevo username (deje en blanco para no cambiar): ")
        password = input("Nueva contraseña (deje en blanco para no cambiar): ")
        email = input("Nuevo email (deje en blanco para no cambiar): ")
        Usuario.modificar_usuario(user_id, username or None, password or None, email or None)

    @staticmethod
    def eliminar_usuario():
        criterio = input("Ingrese el username o email del usuario a eliminar: ")
        Usuario.eliminar_usuario(criterio)

    @staticmethod
    def buscar_usuario():
        criterio = input("Ingrese el username o email a buscar: ")
        usuario = Usuario.buscar_usuario(criterio)
        if usuario:
            print(usuario)
        else:
            print("Usuario no encontrado.")

    @staticmethod
    def mostrar_usuarios():
        usuarios = Usuario.traer_usuarios()
        for usuario in usuarios:
            print(usuario)