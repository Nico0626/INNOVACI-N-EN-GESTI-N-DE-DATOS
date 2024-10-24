import mysql.connector
from mysql.connector import Error


class Conexiondb:
    def __init__(self, host, user, password, database):
        """
        Inicializa los parámetros de la conexión a la base de datos.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
        """
        Conecta con la base de datos.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexión exitosa")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None
            
    def execute_query(self, query, params=None):
        """
        Ejecuta una consulta en la base de datos.
        """
        if self.connection is None:
            print("No hay conexión con la base de datos.")
            return None

        try:
            with self.connection.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)

                # Si la consulta es de tipo SELECT, intentamos consumir todos los resultados
                if query.strip().lower().startswith("select"):
                    resultados = cursor.fetchall()
                    if resultados:
                        print("Resultados obtenidos:")
                        for fila in resultados:
                            print(fila)
                        return resultados
                    else:
                        print("No se encontraron resultados.")
                else:
                    # Para consultas como INSERT, UPDATE, DELETE
                    self.connection.commit()
                    print("Consulta ejecutada exitosamente.")
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
    
    
    def close(self):
        """
        Cierra la conexión a la base de datos.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada.")    

conexion = Conexiondb('localhost','root','NM260621','libreria')

conexion.conectar()
conexion.execute_query('SELECT * FROM libros')

conexion.execute_query('''
SELECT v.id_venta, v.fecha_venta, v.total, u.nombre
FROM venta v
JOIN usuario u ON v.id_usuario = u.id_usuario
WHERE v.fecha_venta BETWEEN '2024-01-01' AND '2024-12-31'
''')
