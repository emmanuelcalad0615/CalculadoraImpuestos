import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, IncomeDeclaration, NaturalPerson, CalculoException
import psycopg2
from psycopg2 import sql
from Controller import SecretConfig

class NotFound(Exception):
    pass

class IncomeDeclarationController:

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
    def BorrarFilas():
        
        sql = "delete from usuarios;"
        conecction, cursor = IncomeDeclarationController.get_cursor()
        cursor.execute( sql )
        sql = "delete from familiares;"
        cursor.execute( sql )
        cursor.connection.commit() 

    @staticmethod
    def create_table():
        connection, cursor = IncomeDeclarationController.get_cursor()
        try:
            with open("sql/crate-income_declaration.sql", "r") as f:
                sql_script = f.read()
            cursor.execute(sql_script)
            connection.commit()  
        except psycopg2.errors.DuplicateTable:
            pass    
        except Exception as e:
            connection.rollback()
            print(f"Error creando la tabla: {e}") 
        finally:
            cursor.close()  
            connection.close()  

    @staticmethod
    def insert_income_declaration(income_declaration: IncomeDeclaration, rut: int):
        connection, cursor = IncomeDeclarationController.get_cursor()
        try:
            total_ingresos_gravados = income_declaration.calcular_total_ingresos_gravados()
            total_ingresos_no_gravados = income_declaration.calcular_total_ingresos_no_gravados()
            total_costos_deducibles = income_declaration.calcular_total_costos_deducibles()
            valor_impuesto = income_declaration.calcular_valor_impuesto()

            cursor.execute(
                "INSERT INTO income_declaration (rut, total_ingresos_gravados, total_ingresos_no_gravados, "
                "total_costos_deducibles, valor_impuesto) VALUES (%s, %s, %s, %s, %s);",
                (
                    rut,
                    total_ingresos_gravados,
                    total_ingresos_no_gravados,
                    total_costos_deducibles,
                    valor_impuesto
                )
            )
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error insertando declaración de ingresos: {e}")
        finally:
            cursor.close()
            connection.close()    

    @staticmethod
    def update_income_declaration(rut: int, total_ingresos_gravados: int,
                               total_ingresos_no_gravados: int,
                               total_costos_deducibles: int,
                               valor_impuesto: int):
        connection, cursor = IncomeDeclarationController.get_cursor()
        try:
            # Verificar que se proporcione una declaración existente
            cursor.execute("SELECT * FROM income_declaration WHERE rut = %s;", (rut,))
            result = cursor.fetchone()

            if not result:
                print("No se encontró la declaración de ingresos con el ID proporcionado.")
                return

            # Construir la consulta de actualización
            query = """
                UPDATE income_declaration
                SET total_ingresos_gravados = %s,
                    total_ingresos_no_gravados = %s,
                    total_costos_deducibles = %s,
                    valor_impuesto = %s
                WHERE rut = %s;
            """

            cursor.execute(query, (total_ingresos_gravados, total_ingresos_no_gravados,
                                   total_costos_deducibles, valor_impuesto, rut))
            connection.commit()
            print("Declaración de ingresos actualizada correctamente.")
    
        except Exception as e:
            connection.rollback()
            print(f"Error actualizando declaración de ingresos: {e}")
        finally:
            cursor.close()
            connection.close()
 

    @staticmethod
    def delete_income_declaration(rut: int):
        connection, cursor = IncomeDeclarationController.get_cursor()
        try:
            cursor.execute("DELETE FROM income_declaration WHERE rut = %s;", (rut,))
            if cursor.rowcount == 0:
                raise NotFound("No se encontró declaración de ingresos con el RUT proporcionado.")
            else:
                connection.commit()
                print("Declaración de ingresos eliminada correctamente.")
        except Exception as e:
            connection.rollback()
            print(f"Error eliminando declaración de ingresos: {e}")
        finally:
            cursor.close()
            connection.close() 

    @staticmethod
    def serch_income_declaration(rut: int):
        connection, cursor = IncomeDeclarationController.get_cursor()
        try:
            cursor.execute("SELECT * FROM income_declaration WHERE rut = %s;", (rut,))
            result = cursor.fetchone()
            if not result:
                raise NotFound("No se encontró declaración de ingresos con el RUT proporcionado.")
            return result  # Retorna los datos encontrados
        except Exception as e:
            print(f"Error buscando declaración de ingresos: {e}")
        finally:
            cursor.close()
            connection.close()

IncomeDeclarationController.update_income_declaration(1000873479, 2000000000000, 400000, 6, 7)



