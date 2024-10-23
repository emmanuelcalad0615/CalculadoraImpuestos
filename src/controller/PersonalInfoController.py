import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, IncomeDeclaration, NaturalPerson
import psycopg2
from psycopg2 import sql
from Controller import SecretConfig

# Custom exception to handle not found cases
class NotFound(Exception):
    pass

class PersonalInfoController:

    @staticmethod
    def get_cursor():
        """
        Creates a connection to the database and returns a cursor for executing instructions.
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
        """
        Creates the 'personal_info' table in the database by reading the SQL script from a file.
        Handles the error if the table already exists.
        """
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            with open("sql/create-personal_info.sql", "r") as f:
                sql_script = f.read()
            cursor.execute(sql_script)
            connection.commit()  
        except psycopg2.errors.DuplicateTable:
            # Ignore if the table already exists
            pass    
        except Exception as e:
            connection.rollback()
            print(f"Error creating the table: {e}")  
        finally:
            cursor.close()  
            connection.close() 

    @staticmethod        
    def delete_rows():
        """
        Deletes all rows from the 'usuarios' and 'familiares' tables.
        """
        sql = "DELETE FROM usuarios;"
        connection, cursor = PersonalInfoController.get_cursor()
        cursor.execute(sql)
        sql = "DELETE FROM familiares;"
        cursor.execute(sql)
        cursor.connection.commit()             

    @staticmethod
    def insert_personal_info(personal_info: PersonalInfo):
        """
        Inserts personal information into the 'personal_info' table.
        """
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            cursor.execute(
                "INSERT INTO personal_info (cedula, nombre, ocupacion) VALUES (%s, %s, %s);",
                (personal_info.id, personal_info.nombre, personal_info.ocupacion)
            )
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error inserting personal information: {e}")
        finally:
            cursor.close()
            connection.close()    

    @staticmethod
    def update_personal_info(cedula: int, nombre: str = None, ocupacion: str = None):
        """
        Updates personal information in the 'personal_info' table based on the provided cedula.
        """
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            # Retrieve the current data for the person
            cursor.execute("SELECT * FROM personal_info WHERE cedula = %s;", (cedula,))
            result = cursor.fetchone()

            if not result:
                raise NotFound("No personal information found with the provided cedula.")

            updates = []
            params = []

            # Add name to the query if not None
            if nombre is not None:
                updates.append("nombre = %s")
                params.append(nombre)

            # Add occupation to the query if not None
            if ocupacion is not None:
                updates.append("ocupacion = %s")
                params.append(ocupacion)

            # Ensure there's something to update
            if not updates:
                print("No changes provided for update.")
                return

            # Build the query
            query = f"UPDATE personal_info SET {', '.join(updates)} WHERE cedula = %s;"
            params.append(cedula)

            cursor.execute(query, params)
            connection.commit()
            print("Information updated successfully.")
        except Exception as e:
            connection.rollback()
            print(f"Error updating personal information: {e}")
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete_personal_info(cedula: int):
        """
        Deletes personal information from the 'personal_info' table based on the provided cedula.
        """
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            cursor.execute(
                "DELETE FROM personal_info WHERE cedula = %s;",
                (cedula,)
            )
            if cursor.rowcount == 0:
                raise NotFound("No personal information found with the provided cedula.")
            else:
                connection.commit()
                print("Personal information deleted successfully.")
        except Exception as e:
            connection.rollback()
            print(f"Error deleting personal information: {e}")
        finally:
            cursor.close()
            connection.close() 

    @staticmethod
    def search_personal_info(cedula: int):
        """
        Searches for personal information in the 'personal_info' table based on the provided cedula.
        Returns the found data or raises an exception if no information is found.
        """
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            cursor.execute("SELECT * FROM personal_info WHERE cedula = %s;", (cedula,))
            result = cursor.fetchone()
            if not result:
                raise NotFound("No personal information found with the provided cedula.")
            return result  # Return the found data
        except Exception as e:
            print(f"Error searching for personal information: {e}")
        finally:
            cursor.close()
            connection.close()
