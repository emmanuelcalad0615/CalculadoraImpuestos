import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, IncomeDeclaration, NaturalPerson
import psycopg2
from . import SecretConfig

class NotFoundPersonalInfo(Exception):
    """ 
    Exception raised when personal information is not found in the database.
    """
    pass

class DatabaseErrorPersonalInfo(Exception):
    """ 
    Base exception class for database-related errors.
    """
    pass

class TableCreationErrorPersonalInfo(DatabaseErrorPersonalInfo):
    """ 
    Exception raised when there is an error creating a table.
    """
    pass

class InsertionErrorPersonalInfo(DatabaseErrorPersonalInfo):
    """ 
    Exception raised when there is an error inserting personal information.
    """
    pass

class UpdateErrorPersonalInfo(DatabaseErrorPersonalInfo):
    """ 
    Exception raised when there is an error updating personal information.
    """
    pass

class DeletionErrorPersonalInfo(DatabaseErrorPersonalInfo):
    """ 
    Exception raised when there is an error deleting personal information.
    """
    pass

class SearchErrorPersonalInfo(DatabaseErrorPersonalInfo):
    """ 
    Exception raised when there is an error searching for personal information.
    """
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
        try:
            connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
            return connection, connection.cursor()
        except Exception as e:
            raise DatabaseErrorPersonalInfo(f"Error connecting to the database: {e}")

    @staticmethod
    def create_table():
        """ 
        Creates the personal_info table in the database if it doesn't already exist.
        Reads the SQL script from a file and executes it.
        """
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            with open("sql/create-personal_info.sql", "r") as f:
                sql_script = f.read()
            cursor.execute(sql_script)
            connection.commit()  
            print("Table created successfully.")
        except psycopg2.errors.DuplicateTable:
            """ 
            Ignore if the table already exists.
            """
            pass
        except Exception as e:
            connection.rollback()
            raise TableCreationErrorPersonalInfo(f"Error creating the table: {e}")  
        finally:
            cursor.close()  
            connection.close()

    @staticmethod        
    def clear_tables():
        """ 
        Deletes all entries from the personal_info table.
        Useful for resetting the table during development or testing.
        """
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            sql = "DELETE FROM personal_info;"
            cursor.execute(sql)
            connection.commit()  
            print("Tables cleared successfully.")
        except Exception as e:
            connection.rollback()
            raise DatabaseErrorPersonalInfo(f"Error deleting tables: {e}")
        finally:
            cursor.close()  
            connection.close()

    @staticmethod
    def insert_personal_info(personal_info: PersonalInfo):
        """ 
        Inserts a new personal information record into the database.
        Accepts a PersonalInfo object and inserts its attributes into the table.
        """
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            cursor.execute(
                "INSERT INTO personal_info (ID, name, ocupation) VALUES (%s, %s, %s);",
                (personal_info.id, personal_info.name, personal_info.ocupation)
            )
            connection.commit()
            print("Personal information inserted successfully.")
        except Exception as e:
            connection.rollback()
            raise InsertionErrorPersonalInfo(f"Error inserting personal information: {e}")
        finally:
            cursor.close()
            connection.close()    

    @staticmethod
    def update_personal_info(cedula: int, nombre: str = None, ocupacion: str = None):
        """ 
        Updates the personal information for a specific ID.
        Accepts new values for name and occupation; only updates those that are not None.
        """
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            # Get the current data for the person
            cursor.execute("SELECT name, ocupation FROM personal_info WHERE ID = %s;", (cedula,))
            result = cursor.fetchone()

            if not result:
                raise NotFoundPersonalInfo("No personal information found with the provided ID.")

            updates = []
            params = []

            # Add name to the query if it's not None
            if nombre is not None:
                updates.append("name = %s")
                params.append(nombre)

            # Add occupation to the query if it's not None
            if ocupacion is not None:
                updates.append("ocupation = %s")
                params.append(ocupacion)

            # Make sure there is something to update
            if not updates:
                return

            # Build the query
            query = f"UPDATE personal_info SET {', '.join(updates)} WHERE ID = %s;"
            params.append(cedula)

            cursor.execute(query, params)
            connection.commit()
            print("Personal information updated successfully.")
        except NotFoundPersonalInfo as e:
            print(f"Error: {e}")
            connection.rollback()
            raise
        except Exception as e:
            connection.rollback()
            raise UpdateErrorPersonalInfo(f"Error updating natural person: {e}")
        finally:
            cursor.close()
            connection.close() 

    @staticmethod
    def delete_personal_info(cedula: int):
        """ 
        Deletes the personal information record with the specified ID.
        Raises an exception if no record is found for the given ID.
        """
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            cursor.execute(
                "DELETE FROM personal_info WHERE ID = %s;",
                (cedula,)
            )
            if cursor.rowcount == 0:
                raise NotFoundPersonalInfo("No personal information found with the provided ID.")
            else:
                connection.commit()
                print("Personal information deleted successfully.")
        except Exception as e:
            connection.rollback()
            raise DeletionErrorPersonalInfo(f"Error deleting personal information: {e}")
        finally:
            cursor.close()
            connection.close() 

    @staticmethod
    def search_personal_info(cedula: int):
        """ 
        Searches for personal information by ID and returns the result.
        Raises an exception if no record is found for the specified ID.
        """
        connection, cursor = PersonalInfoController.get_cursor()
        try:
            cursor.execute("SELECT ID, name, ocupation FROM personal_info WHERE ID = %s;", (cedula,))
            result = cursor.fetchone()
            
            if not result:
                raise NotFoundPersonalInfo("No personal information found with the provided ID.")

            personal_info = PersonalInfo(result[0], result[1], result[2])
            return personal_info 
        except NotFoundPersonalInfo as e:
            print(f"Error: {e}")
            raise
        except Exception as e:
            raise SearchErrorPersonalInfo(f"Error searching for personal information: {e}")
        finally:
            cursor.close()
            connection.close()  
