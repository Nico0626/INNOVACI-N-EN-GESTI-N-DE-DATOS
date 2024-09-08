
░▀█▀░█▀▀░█░█░█▀█░█▀▄░█▀█░█░█░█░█  
░░█░░▀▀█░█░█░█░█░█░█░█░█░█▀▄░█░█  
░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀

TSUNDOKU es un sistema que apunta a la gestión de librerías, enfocada en la venta de libros, la administración de inventarios, el registro de clientes y la gestión de ventas.

## Descripción del Proyecto

**Proyecto Integrador - Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial - Cohorte 2024**

Como parte del "Proyecto Integrador" para la Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial, Cohorte 2024, nos propusimos a desarrollar una aplicación y base de datos que apunta principalmente a la gestión de stock y ventas de una librería. 

### Asignaturas y sus respectivos contenidos

- Base de Datos II
     - [Ver Diagrama de Base de Datos»](https://github.com/Nico0626/INNOVACION-EN-GESTION-DE-DATOS/blob/master/DIAGRAMA-ER.pdf "Ver Base de Datos »")
           
- Programación I
     - [Ver código »](https://github.com/Nico0626/INNOVACION-EN-GESTION-DE-DATOS "Ver código »")

### Autores

| Nombre             | Usuario de GitHub                                | DNI        | Email                       |
|--------------------|--------------------------------------------------|------------|-----------------------------|
| Angellotti Enzo    | [Enzoriukz](https://github.com/Enzoriukz "Enzoriukz")        | 32107971   | enzomakz@gmail.com          |
| Menón Nicolas      | [Nico0626](https://github.com/Nico0626 "Nico0626")           | 46129760   | nico.menon.2@gmail.com      |
| Leyria Federico    | [Federicoleyria](https://github.com/Federicoleyria "Federicoleyria") | 43523682   | fedeleyria2016@gmail.com    |
| Soto Noelia        | [NoeliaSoto](https://github.com/NoeliaSoto "NoeliaSoto")     | 41253579   | noeli4.soto@gmail.com       |



## Modularización del codigo

### main.py:
Este archivo contiene el flujo principal del programa, que gestiona el inicio de sesión, el registro de usuarios, y las interacciones con los usuarios. También maneja la generación de captchas para verificar que no sean bots y registra la actividad en archivos de texto.
### test_aritmetica.py:
Incluye pruebas unitarias para las funciones definidas en el archivo aritmetica.py, verificando que las operaciones aritméticas básicas y otras funciones se comporten correctamente.
### aritmetica.py:
Define funciones aritméticas básicas como sumar, restar, multiplicar, dividir, y otras operaciones sobre múltiples números como suma y promedio.
### captcha.py:
Genera operaciones matemáticas aleatorias para un sistema de captcha. Calcula los resultados de dichas operaciones y valida la respuesta del usuario, asegurando que no sea un bot.

## Funcionalidades Clave del sistema:

### Archivo: main.py
logo(): Muestra un logo en formato ASCII.
bienvenida(): Imprime un mensaje de bienvenida.
login(usuarios): Gestiona el inicio de sesión con validación de usuario y contraseña.
olvidar_contraseña(usuarios, usuario): Muestra un mensaje para contactar al administrador si se olvida la contraseña.
registro_usuario(usuarios): Permite el registro de un nuevo usuario verificando el cumplimiento de los requisitos.
validar_clave(clave): Verifica si una clave cumple los requisitos de seguridad.
anotar_txt(usuarios): Guarda la información de los usuarios en un archivo de texto.
ingresotxt(nombre_usuario): Registra la fecha y hora de ingreso de un usuario en un archivo de texto.

### Archivo: test_aritmetica.py
test_sumar(): Prueba la función de suma.
test_restar(): Prueba la función de resta.
test_dividir(): Prueba la función de división, incluyendo la verificación de divisiones por cero.
test_multiplicar(): Prueba la función de multiplicación.
test_sumar_n(): Prueba la función de suma de múltiples números.
test_promedio_n(): Prueba la función de cálculo de promedio.


## Análisis EPS

Este análisis detalla cómo las diferentes entradas (nombre de usuario, contraseña, opción del menú) se procesan en el sistema y qué salidas se generan en función de esas entradas y procesos.

### Entradas

1. **Usuario**: El nombre de usuario que el usuario ingresa para iniciar sesión en el sistema.
2. **Contraseña**: La contraseña correspondiente al nombre de usuario ingresado.
3. **Opción del Menú**: La opción seleccionada por el usuario en el menú principal después de iniciar sesión.

### Procesos

**Inicio de Sesión**:

1. El sistema solicita al usuario que ingrese su nombre de usuario.
2. El usuario ingresa su nombre de usuario.
3. El sistema solicita al usuario que ingrese su contraseña.
4. El usuario ingresa su contraseña.
5. El sistema verifica las credenciales ingresadas.
   - Si las credenciales son válidas, el usuario inicia sesión y se muestra el menú principal.
   - Si las credenciales son inválidas, el sistema muestra un mensaje de error y permite al usuario intentar nuevamente iniciar sesión.

**Menú Principal**:

1. El sistema muestra las opciones del menú disponibles.
2. El usuario selecciona una opción del menú.
3. El sistema procesa la opción seleccionada y ejecuta la funcionalidad correspondiente.
4. Después de completar la acción seleccionada, el sistema vuelve a mostrar el menú principal para que el usuario pueda seleccionar otra opción o salir del sistema.

### Salidas

1. **Inicio de Sesión Exitoso**:
   - Mensaje de bienvenida que incluye el nombre de usuario.
   - Menú principal con opciones.

2. **Inicio de Sesión Fallido**:
   - Mensaje de error indicando que las credenciales son incorrectas.
   - Opción para volver a intentar iniciar sesión.

3. **Selección de Opción del Menú**:
   - Ejecución de la funcionalidad correspondiente según la opción seleccionada.
   - Mensajes de confirmación o resultados de la acción realizada.
   - Regreso al menú principal para seleccionar otra opción o salir del sistema.

## Archivos esenciales y uso de la aplicación

Este repositorio contiene varios archivos esenciales para el funcionamiento de TSUNDOKU, estos son:

1. **main.py**: Archivo principal que gestiona la interfaz de usuario, incluyendo la bienvenida, el inicio de sesión, registro de usuarios, verificación de captchas y registro de actividades en archivos de texto.

2. **test_aritmetica.py**: Contiene pruebas unitarias para verificar que las funciones aritméticas del archivo aritmetica.py funcionen correctamente.

3. **aritmetica.py**: Define las funciones básicas para operaciones aritméticas como sumar, restar, multiplicar, dividir, y cálculos de suma y promedio sobre múltiples números.

4. **captcha.py**: Genera captchas basados en operaciones matemáticas aleatorias y valida que el usuario no sea un bot.

Para usar la aplicación, se deben instalar Visual Studio Code, MySQL y MySQL Workbench. Luego, se clona el repositorio y se ejecutan los scripts SQL proporcionados para crear y poblar la base de datos. Finalmente, se ejecuta el archivo `main.py` desde Visual Studio Code. El sistema pedirá un nombre de usuario y contraseña para acceder, y mostrará un menú principal para gestionar la librería, permitiendo a cualquier usuario interactuar con la aplicación sin necesidad de conocimientos previos en programación.



