import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, NaturalPerson, IncomeDeclaration, CalculoException
import psycopg2
from psycopg2 import sql
from Controller import SecretConfig

# Custom exception for not found cases
class NotFound(Exception):
    pass

class NaturalPersonController:

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
        connection, cursor = NaturalPersonController.get_cursor()
        cursor.execute(sql)
        sql = "DELETE FROM familiares;"
        cursor.execute(sql)
        cursor.connection.commit() 

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
            pass    
        except Exception as e:
            connection.rollback()
            print(f"Error creating the table: {e}")  
        finally:
            cursor.close()  
            connection.close()     

    @staticmethod
    def insert_natural_person(natural_person: NaturalPerson, personal_info_id: int, personal_info_rut: int):
        """
        Inserts a natural person into the 'natural_person' table.
        """
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
            print(f"Error inserting natural person: {e}")
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
        """
        connection, cursor = NaturalPersonController.get_cursor()
        try:
            # Retrieve the current data of the natural person
            cursor.execute("SELECT * FROM natural_person WHERE rut = %s;", (rut,))
            result = cursor.fetchone()

            if not result:
                raise NotFound("No natural person found with the provided RUT.")

            # Extract current values
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

            # Update values only if new ones are provided
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

            # Validate the updated data
            NaturalPerson(**updated_data)  # This will raise exceptions if there are validation errors

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
        except Exception as e:
            connection.rollback()
            print(f"Error updating natural person: {e}")
        finally:
            cursor.close()
            connection.close() 

    @staticmethod
    def delete_natural_person(rut: int):
        """
        Deletes a natural person from the 'natural_person' table based on the provided RUT.
        """
        connection, cursor = NaturalPersonController.get_cursor()
        try:
            cursor.execute("DELETE FROM natural_person WHERE rut = %s;", (rut,))
            if cursor.rowcount == 0:
                raise NotFound("No natural person found with the provided RUT.")
            else:
                connection.commit()
                print("Natural person deleted successfully.")
        except Exception as e:
            connection.rollback()
            print(f"Error deleting natural person: {e}")
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
            cursor.execute("SELECT * FROM natural_person WHERE rut = %s;", (rut,))
            result = cursor.fetchone()
            if not result:
                raise NotFound("No natural person found with the provided RUT.")
            return result  # Return the found data
        except Exception as e:
            print(f"Error searching for natural person: {e}")
        finally:
            cursor.close()
            connection.close()
