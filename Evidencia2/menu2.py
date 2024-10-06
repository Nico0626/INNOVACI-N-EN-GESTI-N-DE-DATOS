from usuario import Usuario

def main():
    while True:
        print("\n*** Menu de Gestión de Usuarios ***")
        print("1. Agregar un nuevo usuario")
        print("2. Modificar un usuario")
        print("3. Eliminar un usuario (por username o email)")
        print("4. Buscar usuario por email o username")
        print("5. Mostrar todos los usuarios")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Usuario.agregar_usuario()
        elif opcion == "2":
            Usuario.modificar_usuario()
        elif opcion == "3":
            Usuario.eliminar_usuario_by_criteria()
        elif opcion == "4":
            Usuario.buscar_usuario()
        elif opcion == "5":
            Usuario.mostrar_usuarios()
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()
