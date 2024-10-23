import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, IncomeDeclaration, NaturalPerson, CalculoException
import psycopg2
from psycopg2 import sql
from Controller import SecretConfig

# Custom exception for not found cases
class NotFound(Exception):
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
    def delete_rows():
        """
        Deletes all rows from the 'usuarios' and 'familiares' tables.
        """
        sql = "DELETE FROM usuarios;"
        connection, cursor = IncomeDeclarationController.get_cursor()
        cursor.execute(sql)
        sql = "DELETE FROM familiares;"
        cursor.execute(sql)
        cursor.connection.commit() 

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
    def insert_income_declaration(income_declaration: IncomeDeclaration, rut: int):
        """
        Inserts an income declaration into the 'income_declaration' table.
        """
        connection, cursor = IncomeDeclarationController.get_cursor()
        try:
            total_taxable_income = income_declaration.calcular_total_ingresos_gravados()
            total_non_taxable_income = income_declaration.calcular_total_ingresos_no_gravados()
            total_deductible_costs = income_declaration.calcular_total_costos_deducibles()
            tax_value = income_declaration.calcular_valor_impuesto()

            cursor.execute(
                "INSERT INTO income_declaration (rut, total_ingresos_gravados, total_ingresos_no_gravados, "
                "total_costos_deducibles, valor_impuesto) VALUES (%s, %s, %s, %s, %s);",
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
    def update_income_declaration(rut: int, total_ingresos_gravados: int,
                                  total_ingresos_no_gravados: int,
                                  total_costos_deducibles: int,
                                  valor_impuesto: int):
        """
        Updates an existing income declaration in the 'income_declaration' table based on the provided RUT.
        """
        connection, cursor = IncomeDeclarationController.get_cursor()
        try:
            # Check that an existing declaration is provided
            cursor.execute("SELECT * FROM income_declaration WHERE rut = %s;", (rut,))
            result = cursor.fetchone()

            if not result:
                print("No income declaration found with the provided RUT.")
                return

            # Build the update query
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
                raise NotFound("No income declaration found with the provided RUT.")
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
            cursor.execute("SELECT * FROM income_declaration WHERE rut = %s;", (rut,))
            result = cursor.fetchone()
            if not result:
                raise NotFound("No income declaration found with the provided RUT.")
            return result  # Return the found data
        except Exception as e:
            print(f"Error searching for income declaration: {e}")
        finally:
            cursor.close()
            connection.close()
