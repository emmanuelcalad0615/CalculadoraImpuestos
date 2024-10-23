import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, NaturalPerson, IncomeDeclaration, CalculoException
import psycopg2
from psycopg2 import sql
from Controller import SecretConfig
class NotFound(Exception):
    pass
class NaturalPersonController:

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
        conecction, cursor = NaturalPersonController.get_cursor()
        cursor.execute( sql )
        sql = "delete from familiares;"
        cursor.execute( sql )
        cursor.connection.commit() 

    @staticmethod
    def create_table():
        connection, cursor = NaturalPersonController.get_cursor()
        try:
            with open("sql/crate-natural_person.sql", "r") as f:
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
    def insert_natural_person(natural_person: NaturalPerson, personal_info_id: int, personal_info_rut: int):
        connection, cursor = NaturalPersonController.get_cursor()
        try:
            cursor.execute(
                "INSERT INTO natural_person (rut, laboral_income, other_income, withholding_source, "
                "social_security_payments, pension_contributions, mortgage_payments, "
                "donations, educational_expenses, cedula) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (
                    personal_info_rut,  
                    natural_person.laboral_income,
                    natural_person.other_income,
                    natural_person.withholding_source,
                    natural_person.social_security_payments,
                    natural_person.pension_contributions,
                    natural_person.mortgage_payments,
                    natural_person.donations,
                    natural_person.educational_expenses,
                    personal_info_id
                )
            )
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error insertando persona natural: {e}")
        finally:
            cursor.close()
            connection.close() 

    @staticmethod
    def update_natural_person(rut: int, laboral_income: int = None, other_income: int = None,
                               withholding_source: int = None, social_security_payments: int = None,
                               pension_contributions: int = None, mortgage_payments: int = None,
                               donations: int = None, educational_expenses: int = None):
        connection, cursor = NaturalPersonController.get_cursor()
        try:
            # Obtener los datos actuales de la persona natural
            cursor.execute("SELECT * FROM natural_person WHERE rut = %s;", (rut,))
            result = cursor.fetchone()

            if not result:
                raise NotFound("No se encontró la persona natural con el RUT proporcionado.")

            # Extraer los valores actuales
            current_data = {
                "laboral_income": result[1],
                "other_income": result[2],
                "withholding_source": result[3],
                "social_security_payments": result[4],
                "pension_contributions": result[5],
                "mortgage_payments": result[6],
                "donations": result[7],
                "educational_expenses": result[8],
            }

            # Actualizar los valores solo si se proporcionan nuevos
            updated_data = {
                "laboral_income": laboral_income if laboral_income is not None else current_data["laboral_income"],
                "other_income": other_income if other_income is not None else current_data["other_income"],
                "withholding_source": withholding_source if withholding_source is not None else current_data["withholding_source"],
                "social_security_payments": social_security_payments if social_security_payments is not None else current_data["social_security_payments"],
                "pension_contributions": pension_contributions if pension_contributions is not None else current_data["pension_contributions"],
                "mortgage_payments": mortgage_payments if mortgage_payments is not None else current_data["mortgage_payments"],
                "donations": donations if donations is not None else current_data["donations"],
                "educational_expenses": educational_expenses if educational_expenses is not None else current_data["educational_expenses"],
            }

            # Validar los datos actualizados
            NaturalPerson(**updated_data)  # Esto lanzará excepciones si hay errores de validación

            # Construir la consulta de actualización
            updates = []
            params = []

            for field, value in updated_data.items():
                updates.append(f"{field} = %s")
                params.append(value)

            # Ejecutar la actualización
            query = f"UPDATE natural_person SET {', '.join(updates)} WHERE rut = %s;"
            params.append(rut)

            cursor.execute(query, params)
            connection.commit()
            print("Información actualizada correctamente.")

        except CalculoException as e:
            print(f"Error en validaciones: {e}")
            connection.rollback()
        except Exception as e:
            connection.rollback()
            print(f"Error actualizando persona natural: {e}")
        finally:
            cursor.close()
            connection.close() 

    @staticmethod
    def delete_natural_person(rut: int):
        connection, cursor = NaturalPersonController.get_cursor()
        try:
            cursor.execute("DELETE FROM natural_person WHERE rut = %s;", (rut,))
            if cursor.rowcount == 0:
                raise NotFound("No se encontró persona natural con el RUT proporcionado.")
            else:
                connection.commit()
                print("Persona natural eliminada correctamente.")
        except Exception as e:
            connection.rollback()
            print(f"Error eliminando persona natural: {e}")
        finally:
            cursor.close()
            connection.close()     

    @staticmethod
    def search_natural_person(rut: int):
        connection, cursor = NaturalPersonController.get_cursor()
        try:
            cursor.execute("SELECT * FROM natural_person WHERE rut = %s;", (rut,))
            result = cursor.fetchone()
            if not result:
                raise NotFound("No se encontró la persona natural con el RUT proporcionado.")
            return result  # Retorna los datos encontrados
        except Exception as e:
            print(f"Error buscando persona natural: {e}")
        finally:
            cursor.close()
            connection.close()                    
