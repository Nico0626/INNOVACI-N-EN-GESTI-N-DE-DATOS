import os
import pickle
import captcha


class Usuario:
    next_id = 1

    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        Usuario.next_id += 1

    """@property
    def username(self):
        return self.__username
    @property
    def password(self):
        return self.__password
    @property
    def email(self):
        return self.__email
    @property
    def id(self):
        return self._id"""
        
    def __repr__(self):
        return f"Usuario: {self.id}, username: {self.username}, email: {self.email}"

    @classmethod
    def traer_usuario(cls):
        if os.path.exists('usuario.ispc'):
            with open('usuario.ispc', 'rb') as file:
                return pickle.load(file)
        return []

    @classmethod
    def guardar_usuarios(cls, usuarios):
        with open('usuario.ispc', 'wb') as file:
            pickle.dump(usuarios, file)

    @classmethod
    def crear_usuarios(cls, username, password, email):
        usuarios = cls.traer_usuario()
        nuevo_usuario = cls(Usuario.next_id, username, password, email)
        usuarios.append(nuevo_usuario)
        cls.guardar_usuarios(usuarios)
        print(f"Usuario {username} creado exitosamente")
        
    @classmethod
    def obtener_usuario(cls, user_id):
        usuarios = cls.traer_usuario()
        for usuario in usuarios:
            if usuario.id == user_id:
                return usuario
        return None

    @classmethod
    def actualizar_usuario(cls, user_id, username=None, password=None, email=None):
        usuarios = cls.traer_usuario()
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
        usuarios = cls.traer_usuario()
        usuarios = [usuario for usuario in usuarios if usuario.id != user_id]
        cls.guardar_usuarios(usuarios)
        print(f"Usuario con ID {user_id} eliminado.")

    @classmethod
    def agregar_usuario(cls):
        usuarios = cls.traer_usuario()
        username = input("Ingrese el nombre de usuario: ")
        captcha.resolver_captcha()
        password = input("Ingrese la contraseña: ")
        email = input("Ingrese el correo: ")
        cls.crear_usuarios(username, password, email)

    @classmethod
    def modificar_usuario(cls):
        user_id = input("Ingrese el ID del usuario a modificar: ")
        try:
            user_id = int(user_id)
        except ValueError:
            print("Por favor, ingrese un ID válido.")
            return

        usuario = cls.obtener_usuario(user_id)

        if usuario:
            print(f"Usuario encontrado: {usuario}")
            username = input("Nuevo username (deje en blanco para no cambiar): ")
            password = input("Nueva contraseña (deje en blanco para no cambiar): ")
            email = input("Nuevo email (deje en blanco para no cambiar): ")

            cls.actualizar_usuario(usuario.id, username if username else None, password if password else None, email if email else None)
        else:
            print("Usuario no encontrado.")

    @classmethod
    def eliminar_usuario_by_criteria(cls):
        criterio = input("Ingrese el username o email del usuario a eliminar: ")
        usuarios = cls.traer_usuario()
    
        for usuario in usuarios:
            if usuario.username == criterio or usuario.email == criterio:
                cls.eliminar_usuario(usuario.id)
                print("Usuario eliminado con éxito.")
                return
        print("Usuario no encontrado.")

    @classmethod
    def buscar_usuario(cls):
        criterio = input("Ingrese el email o username a buscar: ")
        usuarios = cls.traer_usuario()
        
        for usuario in usuarios:
            if usuario.username == criterio or usuario.email == criterio:
                print(f"Usuario encontrado: {usuario}")
                return
        print("Usuario no encontrado.")

    @classmethod
    def mostrar_usuarios(cls):
        usuarios = cls.traer_usuario()
        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            print("\n*** Lista de Usuarios ***")
            for usuario in usuarios:
                print(usuario)
