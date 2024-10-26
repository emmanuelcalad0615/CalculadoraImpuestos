import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, NaturalPerson, IncomeDeclaration, CalculoException
import psycopg2
from . import SecretConfig
from controller.PersonalInfoController import PersonalInfoController


class DatabaseErrorNaturalPerson(Exception):
    """ 
    Base exception class for database-related errors.
    """
    pass

class NotFoundNaturalPerson(DatabaseErrorNaturalPerson):
    """ 
    Exception raised when a natural person is not found in the database.
    """
    pass

class DatabaseConnectionErrorNaturalPerson(DatabaseErrorNaturalPerson):
    """ 
    Exception raised for errors during database connection.
    """
    pass

class TableCreationErrorNaturalPerson(DatabaseErrorNaturalPerson):
    """ 
    Exception raised when there is an error creating a table.
    """
    pass

class InsertionErrorNaturalPerson(DatabaseErrorNaturalPerson):
    """ 
    Exception raised when there is an error inserting a natural person.
    """
    pass

class UpdateErrorNaturalPerson(DatabaseErrorNaturalPerson):
    """ 
    Exception raised when there is an error updating a natural person.
    """
    pass

class DeletionErrorNaturalPerson(DatabaseErrorNaturalPerson):
    """ 
    Exception raised when there is an error deleting a natural person.
    """
    pass

class SearchErrorNaturalPerson(DatabaseErrorNaturalPerson):
    """ 
    Exception raised when there is an error searching for a natural person.
    """
    pass

class NaturalPersonController:

    @staticmethod
    def get_cursor():
        """ 
        Creates a connection to the database and returns a cursor for executing SQL instructions.
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
            raise DatabaseConnectionErrorNaturalPerson(f"Error connecting to the database: {e}")

    @staticmethod        
    def clear_tables():
        """ 
        Deletes all entries from the 'natural_person' table. 
        This method is used for resetting the table during development or testing.
        """
        try:
            sql = "DELETE FROM natural_person;"
            connection, cursor = NaturalPersonController.get_cursor()
            cursor.execute(sql)
            connection.commit()  
        except Exception as e:
            connection.rollback()
            print(f"Error deleting tables: {e}")
        finally:
            cursor.close()  
            connection.close() 

    @staticmethod
    def create_table():
        """ 
        Creates the 'natural_person' table in the database by reading the SQL script from a file.
        Handles the error if the table already exists.
        """
        connection, cursor = NaturalPersonController.get_cursor()
        try:
            with open("sql/crate-natural_person.sql", "r") as f:
                sql_script = f.read()
            cursor.execute(sql_script)
            connection.commit()  
        except psycopg2.errors.DuplicateTable:
            # Ignore if the table already exists.
            pass    
        except Exception as e:
            connection.rollback()
            raise TableCreationErrorNaturalPerson(f"Error creating the table: {e}")  
        finally:
            cursor.close()  
            connection.close()     

    @staticmethod
    def insert_natural_person(natural_person: NaturalPerson, personal_info_id: int):
        """ 
        Inserts a new natural person into the 'natural_person' table.
        Accepts a NaturalPerson object and the ID of the related personal information.
        """
        connection, cursor = NaturalPersonController.get_cursor()
        try:
            cursor.execute(
                "INSERT INTO natural_person (rut, laboral_income, other_income, withholding_source, "
                "social_security_payments, pension_contributions, mortgage_payments, "
                "donations, educational_expenses, ID) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (
                    natural_person.rut,  
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
            raise InsertionErrorNaturalPerson(f"Error inserting natural person: {e}")
        finally:
            cursor.close()
            connection.close() 

    @staticmethod
    def update_natural_person(rut: int, laboral_income: int = None, other_income: int = None,
                               withholding_source: int = None, social_security_payments: int = None,
                               pension_contributions: int = None, mortgage_payments: int = None,
                               donations: int = None, educational_expenses: int = None):
        """ 
        Updates an existing natural person in the 'natural_person' table based on the provided RUT.
        Only updates fields that are provided with new values.
        """
        connection, cursor = NaturalPersonController.get_cursor()
        try:
            # Retrieve the current data of the natural person
            cursor.execute("SELECT laboral_income, other_income, withholding_source, "
                "social_security_payments, pension_contributions, mortgage_payments, "
                "donations, educational_expenses FROM natural_person WHERE rut = %s;", (rut,))
            result = cursor.fetchone()

            if not result:
                raise NotFoundNaturalPerson("No natural person found with the provided RUT.")

            # Extract current values
            current_data = {
                "laboral_income": result[0],
                "other_income": result[1],
                "withholding_source": result[2],
                "social_security_payments": result[3],
                "pension_contributions": result[4],
                "mortgage_payments": result[5],
                "donations": result[6],
                "educational_expenses": result[7]
            }

            # Update values only if new ones are provided
            updated_data = {
                "rut": rut,
                "laboral_income": laboral_income if laboral_income is not None else current_data["laboral_income"],
                "other_income": other_income if other_income is not None else current_data["other_income"],
                "withholding_source": withholding_source if withholding_source is not None else current_data["withholding_source"],
                "social_security_payments": social_security_payments if social_security_payments is not None else current_data["social_security_payments"],
                "pension_contributions": pension_contributions if pension_contributions is not None else current_data["pension_contributions"],
                "mortgage_payments": mortgage_payments if mortgage_payments is not None else current_data["mortgage_payments"],
                "donations": donations if donations is not None else current_data["donations"],
                "educational_expenses": educational_expenses if educational_expenses is not None else current_data["educational_expenses"],
            }

            # Validate the updated data
            NaturalPerson(**updated_data)  

            # Build the update query
            updates = []
            params = []

            for field, value in updated_data.items():
                updates.append(f"{field} = %s")
                params.append(value)

            # Execute the update
            query = f"UPDATE natural_person SET {', '.join(updates)} WHERE rut = %s;"
            params.append(rut)

            cursor.execute(query, params)
            connection.commit()
            print("Information updated successfully.")

        except CalculoException as e:
            print(f"Validation error: {e}")
            connection.rollback()
        except NotFoundNaturalPerson as e:
            print(f"Error: {e}")
            connection.rollback()
            raise
        except Exception as e:
            connection.rollback()
            raise UpdateErrorNaturalPerson(f"Error updating natural person: {e}")
        finally:
            cursor.close()
            connection.close() 

    @staticmethod
    def delete_natural_person(rut: int):
        """ 
        Deletes a natural person from the 'natural_person' table based on the provided RUT.
        Raises an exception if no record is found for the given RUT.
        """
        connection, cursor = NaturalPersonController.get_cursor()
        try:
            cursor.execute("DELETE FROM natural_person WHERE rut = %s;", (rut,))
            if cursor.rowcount == 0:
                raise NotFoundNaturalPerson("No natural person found with the provided RUT.")
            else:
                connection.commit()
                print("Natural person deleted successfully.")
        except NotFoundNaturalPerson as e:
            print(f"Error: {e}")
            connection.rollback()
            raise
        except Exception as e:
            connection.rollback()
            raise DeletionErrorNaturalPerson(f"Error deleting natural person: {e}")
        finally:
            cursor.close()
            connection.close()     

    @staticmethod
    def search_natural_person(rut: int):
        """ 
        Searches for a natural person in the 'natural_person' table based on the provided RUT.
        Returns the found data or raises an exception if no information is found.
        """
        connection, cursor = NaturalPersonController.get_cursor()
        try:
            cursor.execute("SELECT rut, laboral_income, other_income, withholding_source, social_security_payments, pension_contributions, mortgage_payments, donations, educational_expenses, id FROM natural_person WHERE rut = %s;", (rut,))
            result = cursor.fetchone()
            
            if not result:
                raise NotFoundNaturalPerson("No natural person found with the provided RUT.")

            personal_info = PersonalInfoController.search_personal_info(result[9])
            natural_person = NaturalPerson(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], personal_info)

            return natural_person  # Return the found data
        except NotFoundNaturalPerson as e:
            print(f"Error: {e}")
            raise
        except Exception as e:
            print(f"Error searching for natural person: {e}")
            raise SearchErrorNaturalPerson("An error occurred while searching for the natural person.")
        finally:
            cursor.close()
            connection.close()
