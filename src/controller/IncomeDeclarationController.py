import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, IncomeDeclaration, NaturalPerson, CalculoException
import psycopg2
from psycopg2 import sql
from . import SecretConfig
from TaxCalculator.IncomeDeclaration import IncomeDeclaration
from controller.NaturalPersonController import NaturalPersonController

# Custom exception for not found cases
class NotFoundIncomeDeclaration(Exception):
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
        connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
        return connection, connection.cursor()

    @staticmethod        
    def clear_tables():
        try:
            sql = "delete from income_declaration;"
            conecction, cursor = IncomeDeclarationController.get_cursor()
            cursor.execute( sql )
            cursor.connection.commit()  
        except Exception as e:
            print(f"Error borrando tablas: {e}")
            
        finally:
            conecction.close()  
            cursor.close() 

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
            print(f"Error creating the table: {e}") 
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
            print(f"Error inserting income declaration: {e}")
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
            # Check that an existing declaration is provided
            cursor.execute("SELECT total_taxable_income, total_non_taxable_income, total_deductible_costs, tax_value FROM income_declaration WHERE rut = %s;", (rut,))
            result = cursor.fetchone()

            if not result:
                print("No income declaration found with the provided RUT.")
                return

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
    
        except Exception as e:
            connection.rollback()
            print(f"Error updating income declaration: {e}")
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
        except Exception as e:
            connection.rollback()
            print(f"Error deleting income declaration: {e}")
            
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
            natural_person = NaturalPersonController.search_natural_person(rut)
            income_declaration = IncomeDeclaration(natural_person, result[0], result[1], result[2], result[3])
            return income_declaration
        except Exception as e:
            print(f"Error searching for income declaration: {e}")
            raise NotFoundIncomeDeclaration("No income declaration found with the provided RUT.")

        finally:
            cursor.close()
            connection.close()

