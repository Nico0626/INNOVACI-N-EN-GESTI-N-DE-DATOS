import random
import pandas as pd
import matplotlib.pyplot as plt

def generar_datos_aleatorios(anio):
    """Genera datos aleatorios de lluvia para un año específico sin considerar años bisiestos."""
    # Definición de los días en cada mes
    meses = {
        1: 31,  # Enero
        2: 28,  # Febrero (no se considera bisiesto)
        3: 31,  # Marzo
        4: 30,  # Abril
        5: 31,  # Mayo
        6: 30,  # Junio
        7: 31,  # Julio
        8: 31,  # Agosto
        9: 30,  # Septiembre
        10: 31, # Octubre
        11: 30, # Noviembre
        12: 31  # Diciembre
    }
    
    # Inicializar un diccionario para almacenar los datos de lluvia por mes
    datos_anio = {mes: [] for mes in meses.keys()}

    # Generar datos aleatorios para cada día de cada mes
    for mes, dias in meses.items():
        for dia in range(1, dias + 1):
            # Generar una cantidad aleatoria de lluvia entre 0 y 20 mm
            cantidad = round(random.uniform(0, 20), 2)
            datos_anio[mes].append(cantidad)

    return datos_anio

def guardar_datos_csv(datos, anio):
    """Guarda los datos generados en un archivo CSV."""
    # Crear un DataFrame a partir de los datos
    df = pd.DataFrame(datos)
    df.index += 1  # Cambiar el índice para que comience en 1 (días del mes)
    # Guardar el DataFrame en un archivo CSV
    df.to_csv(f'registro_pluvial_{anio}.csv', index_label='Día')

def cargar_datos_csv(anio):
    """Carga los datos de lluvia desde un archivo CSV."""
    try:
        # Leer el archivo CSV y convertirlo en un diccionario de listas
        return pd.read_csv(f'registro_pluvial_{anio}.csv', index_col=0).to_dict(orient='list')
    except FileNotFoundError:
        # Si el archivo no existe, devolver None
        return None

def mostrar_registros_mes(datos, mes):
    """Muestra los registros de lluvia para un mes específico."""
    if mes in datos:
        # Imprimir los registros pluviales del mes solicitado
        print(f"Registros pluviales para el mes {mes}: {datos[mes]}")
    else:
        print("Mes inválido. Por favor, elige un mes del 1 al 12.")

def graficar_datos(datos):
    """Genera gráficos para visualizar los datos de lluvia."""
    # Calcular la lluvia total por mes
    total_anual = {mes: sum(datos[mes]) for mes in datos}
    
    # Gráfico de barras: lluvias anuales
    plt.figure(figsize=(10, 6))
    plt.bar(total_anual.keys(), total_anual.values(), color='blue')
    plt.title('Lluvias Anuales')
    plt.xlabel('Meses')
    plt.ylabel('Total de Lluvia (mm)')
    plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                               'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
    plt.grid(axis='y')  # Añadir cuadrícula en el eje y
    plt.show()

    # Gráfico de dispersión: días vs meses
    dias = []
    meses = []
    for mes, lluvias in datos.items():
        dias.extend(range(1, len(lluvias) + 1))  # Agregar días
        meses.extend([mes] * len(lluvias))  # Agregar mes correspondiente

    plt.figure(figsize=(10, 6))
    plt.scatter(meses, dias, c='red')  # Gráfico de dispersión
    plt.title('Gráfico de Dispersión de Lluvias')
    plt.xlabel('Meses')
    plt.ylabel('Días')
    plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                               'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
    plt.grid()
    plt.show()

    # Gráfico circular: distribución de lluvias por mes
    plt.figure(figsize=(8, 8))
    plt.pie(total_anual.values(), labels=total_anual.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de Lluvias por Mes')
    plt.axis('equal')  # Para que el gráfico sea un círculo
    plt.show()

def main():
    """Función principal para ejecutar el programa."""
    while True:
        try:
            # Solicitar el año al usuario
            anio = int(input("Ingrese el año para cargar los registros pluviales: "))
            # Intentar cargar los datos desde el CSV
            datos = cargar_datos_csv(anio)

            if datos is None:
                print(f"No se encontraron datos para el año {anio}. Generando datos aleatorios.")
                datos = generar_datos_aleatorios(anio)  # Generar datos aleatorios
                guardar_datos_csv(datos, anio)  # Guardar en CSV
            else:
                print(f"Datos cargados desde el archivo para el año {anio}.")
                
            # Solicitar el mes al usuario
            mes = int(input("Ingrese el mes (1-12) que desea consultar: "))
            mostrar_registros_mes(datos, mes)  # Mostrar datos del mes
            graficar_datos(datos)  # Graficar los datos
            
            # Preguntar si desea realizar otra consulta
            if input("¿Desea consultar otro año? (s/n): ").lower() != 's':
                break
        except ValueError:
            print("Entrada inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()  # Ejecutar la función principal
