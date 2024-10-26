import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, IncomeDeclaration, NaturalPerson, CalculoException
import psycopg2
from . import SecretConfig
from controller.NaturalPersonController import NaturalPersonController

# Base exception for database errors
class DatabaseErrorIncomeDeclaration(Exception):
    """ 
    Base exception class for database-related errors.
    """
    pass

class NotFoundIncomeDeclaration(DatabaseErrorIncomeDeclaration):
    """ 
    Exception raised when an income declaration is not found in the database.
    """
    pass

class DatabaseConnectionErrorIncomeDeclaration(DatabaseErrorIncomeDeclaration):
    """ 
    Exception raised for errors during database connection.
    """
    pass

class TableCreationErrorIncomeDeclaration(DatabaseErrorIncomeDeclaration):
    """ 
    Exception raised when there is an error creating a table.
    """
    pass

class InsertionErrorIncomeDeclaration(DatabaseErrorIncomeDeclaration):
    """ 
    Exception raised when there is an error inserting an income declaration.
    """
    pass

class UpdateErrorIncomeDeclaration(DatabaseErrorIncomeDeclaration):
    """ 
    Exception raised when there is an error updating an income declaration.
    """
    pass

class DeletionErrorIncomeDeclaration(DatabaseErrorIncomeDeclaration):
    """ 
    Exception raised when there is an error deleting an income declaration.
    """
    pass

class SearchErrorIncomeDeclaration(DatabaseErrorIncomeDeclaration):
    """ 
    Exception raised when there is an error searching for an income declaration.
    """
    pass

class IncomeDeclarationController:

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
            raise DatabaseConnectionErrorIncomeDeclaration(f"Error connecting to the database: {e}")

    @staticmethod        
    def clear_tables():
        """ 
        Clears all entries from the 'income_declaration' table. 
        Used for resetting the table during development or testing.
        """
        connection, cursor = IncomeDeclarationController.get_cursor()
        try:
            sql = "DELETE FROM income_declaration;"
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
        Creates the 'income_declaration' table in the database by reading the SQL script from a file.
        Handles the error if the table already exists.
        """
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
            raise TableCreationErrorIncomeDeclaration(f"Error creating the table: {e}")   
        finally:
            cursor.close()  
            connection.close()

    @staticmethod
    def insert_income_declaration(rut: int):
        """
        Inserts an income declaration into the 'income_declaration' table.
        """
        connection, cursor = IncomeDeclarationController.get_cursor()
        try:
            natural_person = NaturalPersonController.search_natural_person(rut)
            income_declaration = IncomeDeclaration(natural_person)
            total_taxable_income = income_declaration.total_taxable_income
            total_non_taxable_income = income_declaration.total_non_taxable_income
            total_deductible_costs = income_declaration.total_deductible_costs
            tax_value = income_declaration.tax_value

            cursor.execute(
                "INSERT INTO income_declaration (rut, total_taxable_income, total_non_taxable_income, total_deductible_costs, tax_value) VALUES (%s, %s, %s, %s, %s);",
                (
                    rut,
                    total_taxable_income,
                    total_non_taxable_income,
                    total_deductible_costs,
                    tax_value
                )
            )
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise InsertionErrorIncomeDeclaration(f"Error inserting income declaration: {e}")
        finally:
            cursor.close()
            connection.close()    

    @staticmethod
    def update_income_declaration(rut: int, total_taxable_income: int,
                                  total_non_taxable_income: int,
                                  total_deductible_costs: int,
                                  tax_value: int):
        """
        Updates an existing income declaration in the 'income_declaration' table based on the provided RUT.
        """
        connection, cursor = IncomeDeclarationController.get_cursor()
        try:
            cursor.execute("SELECT total_taxable_income, total_non_taxable_income, total_deductible_costs, tax_value FROM income_declaration WHERE rut = %s;", (rut,))
            result = cursor.fetchone()

            if not result:
                raise NotFoundIncomeDeclaration("No income declaration found with the provided RUT.")

            # Build the update query
            query = """
                UPDATE income_declaration
                SET total_taxable_income = %s,
                    total_non_taxable_income = %s,
                    total_deductible_costs = %s,
                    tax_value = %s
                WHERE rut = %s;
            """

            cursor.execute(query, (total_taxable_income, total_non_taxable_income,
                                   total_deductible_costs, tax_value, rut))
            connection.commit()
            print("Income declaration updated successfully.")
    
        except CalculoException as e:
            print(f"Validation error: {e}")
            connection.rollback()
        except NotFoundIncomeDeclaration as e:
            print(f"Error: {e}")
            connection.rollback()
            raise
        except Exception as e:
            connection.rollback()
            raise UpdateErrorIncomeDeclaration(f"Error updating natural person: {e}")
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete_income_declaration(rut: int):
        """
        Deletes an income declaration from the 'income_declaration' table based on the provided RUT.
        """
        connection, cursor = IncomeDeclarationController.get_cursor()
        try:
            cursor.execute("DELETE FROM income_declaration WHERE rut = %s;", (rut,))
            if cursor.rowcount == 0:
                raise NotFoundIncomeDeclaration("No income declaration found with the provided RUT.")
            else:
                connection.commit()
                print("Income declaration deleted successfully.")
        except NotFoundIncomeDeclaration as e:
            print(f"Error: {e}")
            raise    

        except Exception as e:
            connection.rollback()
            raise DeletionErrorIncomeDeclaration(f"Error deleting income declaration: {e}")
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def search_income_declaration(rut: int):
        """
        Searches for an income declaration in the 'income_declaration' table based on the provided RUT.
        Returns the found data or raises an exception if no information is found.
        """
        connection, cursor = IncomeDeclarationController.get_cursor()
        try:
            cursor.execute("SELECT total_taxable_income, total_non_taxable_income, total_deductible_costs, tax_value FROM income_declaration WHERE rut = %s;", (rut,))
            result = cursor.fetchone()
            if not result:
                raise NotFoundIncomeDeclaration("No income declaration found with the provided RUT.")

            natural_person = NaturalPersonController.search_natural_person(rut)
            income_declaration = IncomeDeclaration(natural_person, result[0], result[1], result[2], result[3])
            return income_declaration
        except NotFoundIncomeDeclaration as e:
            print(f"Error: {e}")
            raise
        except Exception as e:
            print(f"Error searching for natural person: {e}")
            raise SearchErrorIncomeDeclaration("An error occurred while searching for the natural person.")
        finally:
            cursor.close()
            connection.close()
