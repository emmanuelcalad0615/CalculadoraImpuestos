import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, NaturalPerson, IncomeDeclaration, CalculoException
from controller.IncomeDeclarationController import IncomeDeclarationController
from controller.PersonalInfoController import PersonalInfoController
from controller.NaturalPersonController import NaturalPersonController

def show_menu():
    """ 
    Function to display the main menu options to the user. 
    Each option corresponds to a specific action the user can take within the program.
    """
    print("\n--- Tax Declaration Menu ---")
    print("1. Enter taxpayer data")  
    print("2. Calculate taxes")  
    print("3. Save to database")  
    print("4. Update in database")  
    print("5. Delete from database")  
    print("6. Search in database")  
    print("7. Exit")  

def main():
    """ 
    Main function to control the flow of the tax declaration program. 
    Initializes necessary variables, creates database tables, and handles user interaction.
    """
    natural_person = None  
    personal_info = None  
    declaration = None  
    
    PersonalInfoController.create_table()  
    NaturalPersonController.create_table()  
    IncomeDeclarationController.create_table()  

    while True:
        show_menu()  
        option = input("Select an option: ")  

        if option == '1':
            """ 
            Option to enter taxpayer data. 
            Prompts the user for personal and financial information to create a NaturalPerson object.
            """
            try:
                name = input("Enter the name: ")  
                id = int(input("Enter the ID: "))  
                occupation = input("Enter the occupation: ")  
                rut = int(input("Enter the RUT: "))  
                
                labor_income = int(input("Enter labor income: "))  
                other_income = int(input("Enter other income: "))  
                withholding_source = int(input("Enter withholding tax: "))  
                social_security_payments = int(input("Enter social security payments: "))  
                pension_contributions = int(input("Enter pension contributions: "))  
                mortgage_payments = int(input("Enter mortgage payments: "))  
                donations = int(input("Enter donations: "))  
                educational_expenses = int(input("Enter educational expenses: "))  
                
                personal_info = PersonalInfo(id, name, occupation)  
                natural_person = NaturalPerson(
                    rut, labor_income, other_income, withholding_source,
                    social_security_payments, pension_contributions,
                    mortgage_payments, donations, educational_expenses,
                    personal_info  
                )
                
            except ValueError:
                """ 
                Handle case where the user input is not a valid integer. 
                Inform the user of the error.
                """
                print("Error: Please enter valid numeric values.")
            except CalculoException as e:
                """ 
                Handle specific calculation exceptions that may arise. 
                Display the exception message to the user.
                """
                print(f"Error: {e}")

        elif option == '2':
            """ 
            Option to calculate taxes based on entered data. 
            Creates an IncomeDeclaration instance for the natural person and displays results.
            """
            if natural_person:
                try:
                    declaration = IncomeDeclaration(person=natural_person)  
                    print(declaration)  

                except CalculoException as e:
                    """ 
                    Handle any exceptions that occur during tax calculations. 
                    Display the exception message to the user.
                    """
                    print(f"{e}")
            else:
                """ 
                Inform the user that no taxpayer data has been entered yet. 
                This check prevents errors during tax calculation.
                """
                print("Error: No taxpayer data has been entered.")

        elif option == '3':
            """ 
            Option to save entered data to the database. 
            Ensures that all necessary data has been entered before saving.
            """
            if natural_person and personal_info and declaration:
                try:
                    PersonalInfoController.insert_personal_info(personal_info)  
                    NaturalPersonController.insert_natural_person(natural_person, personal_info.id)  
                    IncomeDeclarationController.insert_income_declaration(natural_person.rut)  

                except Exception as e:
                    """ 
                    Handle any errors that occur during the save process. 
                    Display an error message.
                    """
                    print(f"Error while saving to the database: {e}")
            else:
                """ 
                Inform the user that they must enter all required data before saving. 
                Prevents incomplete data from being saved.
                """
                print("Error: You must enter taxpayer data and calculate the declaration before saving.")
        
        elif option == '4':
            """ 
            Option to update taxpayer information in the database. 
            Allows the user to modify existing records and recalculate declarations.
            """
            if natural_person and declaration:
                try:
                    id_number = (personal_info.id)  
                    rut = natural_person.rut  
                    print(f"Entering new data for the taxpayer with RUT: {rut}")  
                    
                    new_name = input("Enter the new name (leave blank to not change): ")  
                    new_occupation = input("Enter the new occupation (leave blank to not change): ")  

                    PersonalInfoController.update_personal_info(
                        cedula=id_number,  
                        nombre=new_name if new_name else None,  
                        ocupacion=new_occupation if new_occupation else None  
                    )
                    try:
                        new_labor_income = input("Enter the new labor income (leave blank to not change): ")
                        new_labor_income = int(new_labor_income) if new_labor_income else None  

                        new_other_income = input("Enter the new other income (leave blank to not change): ")
                        new_other_income = int(new_other_income) if new_other_income else None  

                        new_withholding = input("Enter the new withholding tax (leave blank to not change): ")
                        new_withholding = int(new_withholding) if new_withholding else None  

                        new_social_security_payments = input("Enter the new social security payments (leave blank to not change): ")
                        new_social_security_payments = int(new_social_security_payments) if new_social_security_payments else None  

                        new_pension_contributions = input("Enter the new pension contributions (leave blank to not change): ")
                        new_pension_contributions = int(new_pension_contributions) if new_pension_contributions else None  

                        new_mortgage_payments = input("Enter the new mortgage payments (leave blank to not change): ")
                        new_mortgage_payments = int(new_mortgage_payments) if new_mortgage_payments else None  

                        new_donations = input("Enter the new donations (leave blank to not change): ")
                        new_donations = int(new_donations) if new_donations else None  

                        new_educational_expenses = input("Enter the new educational expenses (leave blank to not change): ")
                        new_educational_expenses = int(new_educational_expenses) if new_educational_expenses else None  

                        NaturalPersonController.update_natural_person(
                            rut=rut,
                            laboral_income=new_labor_income,  
                            other_income=new_other_income,  
                            withholding_source=new_withholding,  
                            social_security_payments=new_social_security_payments,  
                            pension_contributions=new_pension_contributions,  
                            mortgage_payments=new_mortgage_payments,  
                            donations=new_donations,  
                            educational_expenses=new_educational_expenses  
                        )
                    except Exception as e:
                        """ 
                        Handle any errors that occur during the update process. 
                        Display the error message and exit the function if necessary.
                        """
                        print(f"Error: {e}")
                        return        

                    declaration = IncomeDeclaration(person=natural_person)  
                    total_taxable_income = declaration.calculate_total_taxable_income()  
                    total_non_taxable_income = declaration.calculate_total_non_taxable_income()  
                    total_deductible_costs = declaration.calculate_total_deductible_costs()  
                    tax_value = declaration.calculate_tax_value()  

                    IncomeDeclarationController.update_income_declaration(natural_person.rut, total_taxable_income, total_non_taxable_income, total_deductible_costs, tax_value)  

                    print("Data updated successfully.")  

                except Exception as e:
                    """ 
                    Handle any exceptions that occur during the update process. 
                    Display the error message to the user.
                    """
                    print(f"{e}")
            else:
                """ 
                Inform the user that no taxpayer data has been entered, nor has the declaration been calculated. 
                Prevents any update attempts when no data is available.
                """
                print("Error: No taxpayer data has been entered, nor has the declaration been calculated.")
        
        elif option == '5':
            """ 
            Option to delete taxpayer information from the database. 
            Prompts the user for an ID to delete the corresponding record.
            """
            try: 
                id = int(input("Enter your ID: "))  
                PersonalInfoController.delete_personal_info(id)  
            except Exception as e:
                """ 
                Handle any exceptions that occur during the deletion process. 
                Display the error message to the user.
                """
                print(f"{e}")   

        elif option == '6':
            """ 
            Option to search for taxpayer information in the database. 
            Prompts the user for a RUT and displays the corresponding income declaration.
            """
            try:
                rut = int(input("Enter your RUT: "))  
                print(IncomeDeclarationController.search_income_declaration(rut))  
            except Exception as e:
                """ 
                Handle any exceptions that occur during the search process. 
                Display the error message to the user.
                """
                print(e)              
        
        elif option == '7':

            print("Exiting the program...")
            break

        else:
            print("Invalid option. Please select an option from the menu.")

if __name__ == "__main__":
    main()
