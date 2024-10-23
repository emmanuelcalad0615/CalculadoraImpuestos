import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, IncomeDeclaration, NaturalPerson
import psycopg2
from psycopg2 import sql
import SecretConfig
class NotFound(Exception):
    pass
class PersonalInfoController:

    @staticmethod
    def get_cursor():
        """
        Crea la conexion a la base de datos y retorna un cursor para ejecutar instrucciones
        """
        DATABASE = SecretConfig.PGDATABASE
        USER = SecretConfig.PGUSER
        PASSWORD = SecretConfig.PGPASSWORD
        HOST = SecretConfig.PGHOST
        PORT = SecretConfig.PGPORT
        connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
        return connection, connection.cursor()

    @staticmethod
    def create_table():
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            with open("sql/create-personal_info.sql", "r") as f:
                sql_script = f.read()
            cursor.execute(sql_script)
            connection.commit()  # Asegúrate de hacer commit después de la ejecución
        except Exception as e:
            connection.rollback()
            print(f"Error creando la tabla: {e}")  # Puedes usar logging en lugar de print
        finally:
            cursor.close()  # Asegúrate de cerrar el cursor
            connection.close()  # Y cierra la conexión    

    @staticmethod
    def insert_personal_info(personal_info: PersonalInfo):
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            cursor.execute(
                "INSERT INTO personal_info (cedula, nombre, ocupacion) VALUES (%s, %s, %s);",
                (personal_info.id, personal_info.nombre, personal_info.ocupacion)
            )
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error insertando información personal: {e}")
        finally:
            cursor.close()
            connection.close()    

    @staticmethod
    def update_personal_info(cedula: int, nombre: str = None, ocupacion: str = None):
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            # Obtener los datos actuales de la persona
            cursor.execute("SELECT * FROM personal_info WHERE cedula = %s;", (cedula,))
            result = cursor.fetchone()

            if not result:
                raise NotFound("No se encontró información personal con la cédula proporcionada.")

            updates = []
            params = []

            # Agregar nombre a la consulta si no es None
            if nombre is not None:
                updates.append("nombre = %s")
                params.append(nombre)

            # Agregar ocupación a la consulta si no es None
            if ocupacion is not None:
                updates.append("ocupacion = %s")
                params.append(ocupacion)

            # Asegúrate de que haya algo que actualizar
            if not updates:
                print("No se proporcionaron cambios para actualizar.")
                return

            # Construir la consulta
            query = f"UPDATE personal_info SET {', '.join(updates)} WHERE cedula = %s;"
            params.append(cedula)

            cursor.execute(query, params)
            connection.commit()
            print("Información actualizada correctamente.")
        except Exception as e:
            connection.rollback()
            print(f"Error actualizando información personal: {e}")
        finally:
            cursor.close()
            connection.close()


    @staticmethod
    def delete_personal_info(cedula: int):
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            cursor.execute(
                "DELETE FROM personal_info WHERE cedula = %s;",
                (cedula,)
            )
            if cursor.rowcount == 0:
                raise NotFound("No se encontró información personal con la cédula proporcionada.")
            else:
                connection.commit()
                print("Información personal eliminada correctamente.")
        except Exception as e:
            connection.rollback()
            print(f"Error eliminando información personal: {e}")
        finally:
            cursor.close()
            connection.close() 

    @staticmethod
    def search_personal_info(cedula: int):
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            cursor.execute("SELECT * FROM personal_info WHERE cedula = %s;", (cedula,))
            result = cursor.fetchone()
            if not result:
                raise NotFound("No se encontró información personal con la cédula proporcionada.")
            return result  # Retorna los datos encontrados
        except Exception as e:
            print(f"Error buscando información personal: {e}")
        finally:
            cursor.close()
            connection.close()              
            
#PersonalInfoController.create_table()
#Crear instancia de PersonalInfo
personal_info = PersonalInfo(nombre="Juan Perez", id=12345678, ocupacion="Ingeniero", rut=12345678)

# Insertar información personal
PersonalInfoController.insert_personal_info(personal_info)

print(PersonalInfoController.search_personal_info(12345678))



        