import sys
sys.path.append("src")
import unittest
from controller.IncomeDeclarationController import IncomeDeclarationController, NotFoundIncomeDeclaration, InsertionErrorIncomeDeclaration, UpdateErrorIncomeDeclaration, DeletionErrorIncomeDeclaration
from controller.NaturalPersonController import NaturalPersonController, NotFoundNaturalPerson, InsertionErrorNaturalPerson
from controller.PersonalInfoController import PersonalInfoController, NotFoundPersonalInfo, InsertionErrorPersonalInfo, DeletionErrorPersonalInfo
from TaxCalculator.IncomeDeclaration import IncomeDeclaration, PersonalInfo, NaturalPerson


class TestPersonalInfoController(unittest.TestCase):
    """
    Class that contains tests for the personal information controller.
    Each method verifies different functionalities of the controller.
    """

    def setUp(self):
        """
        Method that runs before each test.
        Clears the personal information table and prepares a test object.
        """
        PersonalInfoController.clear_tables()
        self.info = PersonalInfo(1, "Daniel", "Ingeniero")

    def test_insert_info(self):
        """
        Verifies the functionality of inserting personal information.
        A PersonalInfo object is inserted and searched to confirm it was inserted correctly.
        """
        PersonalInfoController.insert_personal_info(self.info)
        find_info = PersonalInfoController.search_personal_info(self.info.id)
        self.assertEqual(find_info.id, self.info.id)
        self.assertEqual(find_info.name, self.info.name)
        self.assertEqual(find_info.ocupation, self.info.ocupation)

    def test_update_personal_info(self):
        """
        Verifies the functionality of updating personal information.
        A PersonalInfo object is inserted, some of its attributes are updated,
        and it checks that the changes have been applied correctly.
        """
        PersonalInfoController.insert_personal_info(self.info)
        new_name = "Daniel Updated"
        new_occupation = "Senior Engineer"
        PersonalInfoController.update_personal_info(self.info.id, nombre=new_name, ocupacion=new_occupation)

        updated_info = PersonalInfoController.search_personal_info(self.info.id)
        self.assertEqual(updated_info.name, new_name)
        self.assertEqual(updated_info.ocupation, new_occupation)    

    def test_search_personal_info(self):
        """
        Verifies the functionality of searching for personal information.
        A PersonalInfo object is inserted and searched to confirm it can be retrieved correctly.
        """
        PersonalInfoController.insert_personal_info(self.info)
        found_info = PersonalInfoController.search_personal_info(self.info.id)
        self.assertEqual(found_info.id, self.info.id)
        self.assertEqual(found_info.name, self.info.name)
        self.assertEqual(found_info.ocupation, self.info.ocupation) 

    def test_delete_personal_info(self):
        """
        Verifies the functionality of deleting personal information.
        A PersonalInfo object is inserted and then deleted.
        An attempt to search for the deleted personal information should raise a NotFound exception.
        """
        PersonalInfoController.insert_personal_info(self.info)
        PersonalInfoController.delete_personal_info(self.info.id)

        with self.assertRaises(NotFoundPersonalInfo):
            PersonalInfoController.search_personal_info(self.info.id) 

    def test_insert_personal_info_error(self):
        """
        Verifies that an error is raised when trying to insert personal information with invalid data.
        """
        
        invalid_info = PersonalInfo(None, "Daniel", "Engineer")

        with self.assertRaises(InsertionErrorPersonalInfo):
            PersonalInfoController.insert_personal_info(invalid_info)

    def test_update_personal_info_error(self):
        """
        Verifies that an error is raised when trying to update personal information with a non-existing ID.
        """
        PersonalInfoController.insert_personal_info(self.info)
        with self.assertRaises(NotFoundPersonalInfo):
            PersonalInfoController.update_personal_info(999, nombre="Daniel Updated", ocupacion="Senior Engineer")

    def test_delete_personal_info_error(self):
        """
        Verifies that an error is raised when trying to delete personal information that does not exist.
        """
    
        with self.assertRaises(DeletionErrorPersonalInfo):
            PersonalInfoController.delete_personal_info(999)
        

    

class TestNaturalPersonController(unittest.TestCase):
    """
    Class that contains tests for the natural person controller.
    Each method verifies different functionalities of the controller.
    """

    def setUp(self):
        """
        Method that runs before each test.
        Clears the natural person table and prepares a test object.
        """
        NaturalPersonController.clear_tables()
        self.info = PersonalInfo(1, "Daniel", "Ingeniero")
        self.natural_person = NaturalPerson(1, 6000000000, 20000000, 10000000, 2000000, 3000000, 400000, 5000000, 600000, self.info)

    def test_insert_natural_person(self):
        """
        Verifies the functionality of inserting a natural person.
        A NaturalPerson object is inserted and searched to confirm it was inserted correctly.
        """
        NaturalPersonController.insert_natural_person(self.natural_person, self.info.id)
        found_person = NaturalPersonController.search_natural_person(self.natural_person.rut)
        self.assertEqual(found_person.rut, self.natural_person.rut)
        self.assertEqual(found_person.laboral_income, self.natural_person.laboral_income)
        self.assertEqual(found_person.other_income, self.natural_person.other_income)
        self.assertEqual(found_person.withholding_source, self.natural_person.withholding_source)
        self.assertEqual(found_person.social_security_payments, self.natural_person.social_security_payments)
        self.assertEqual(found_person.pension_contributions, self.natural_person.pension_contributions)
        self.assertEqual(found_person.mortgage_payments, self.natural_person.mortgage_payments)
        self.assertEqual(found_person.donations, self.natural_person.donations)
        self.assertEqual(found_person.educational_expenses, self.natural_person.educational_expenses)

    def test_update_natural_person(self):
        """
        Verifies the functionality of updating a natural person.
        A NaturalPerson object is inserted, one of its attributes is updated,
        and it checks that the change has been applied correctly.
        """
        NaturalPersonController.insert_natural_person(self.natural_person, self.info.id)
        
        updated_income = 760000000
        NaturalPersonController.update_natural_person(self.natural_person.rut, laboral_income=updated_income)

        found_person = NaturalPersonController.search_natural_person(self.natural_person.rut)
        self.assertEqual(found_person.laboral_income, updated_income)  

    def test_search_natural_person(self):
        """
        Verifies the functionality of searching for a natural person.
        A NaturalPerson object is inserted and searched to confirm it can be retrieved correctly.
        """
        NaturalPersonController.insert_natural_person(self.natural_person, self.info.id)
        found_natural_person = NaturalPersonController.search_natural_person(self.natural_person.rut)
        self.assertEqual(found_natural_person.rut, self.natural_person.rut)
        self.assertEqual(found_natural_person.laboral_income, self.natural_person.laboral_income)
        self.assertEqual(found_natural_person.other_income, self.natural_person.other_income)
        self.assertEqual(found_natural_person.withholding_source, self.natural_person.withholding_source)
        self.assertEqual(found_natural_person.social_security_payments, self.natural_person.social_security_payments)
        self.assertEqual(found_natural_person.pension_contributions, self.natural_person.pension_contributions)
        self.assertEqual(found_natural_person.mortgage_payments, self.natural_person.mortgage_payments)
        self.assertEqual(found_natural_person.donations, self.natural_person.donations)
        self.assertEqual(found_natural_person.educational_expenses, self.natural_person.educational_expenses)
    

    def test_delete_natural_person(self):
        
        """Verifies the functionality of deleting a natural person.
        A natural person is inserted and then deleted.
        An attempt to search for the deleted natural person should raise a NotFound exception."""
        
        NaturalPersonController.insert_natural_person(self.natural_person, self.info.id)
        
        NaturalPersonController.delete_natural_person(self.natural_person.rut)

        with self.assertRaises(NotFoundNaturalPerson):
            NaturalPersonController.search_natural_person(self.natural_person.rut)

    def test_insert_natural_person_error(self):
        """
        Verify that an error is thrown when trying to insert a natural person with invalid or duplicate data.
        """
        NaturalPersonController.insert_natural_person(self.natural_person, self.info.id)
        with self.assertRaises(InsertionErrorNaturalPerson):
            # Intentar insertar con datos duplicados
            NaturalPersonController.insert_natural_person(self.natural_person, self.info.id) 
    def test_update_natural_person_error(self):
        """
        Verify that an error is thrown when trying to update a natural person with invalid data.        
        
        """
       
        natural_person = NaturalPerson(1, 6000000000, 20000000, 10000000, 2000000, 3000000, 400000, 5000000, 600000, self.info)
        NaturalPersonController.insert_natural_person(natural_person, self.info.id)

        
        with self.assertRaises(NotFoundNaturalPerson):
            NaturalPersonController.update_natural_person(999999999, laboral_income=800000000)  

    def test_delete_natural_person_error(self):
        """
        Verify that an error is thrown when trying to delete a natural person that does not exist.   
        
        """
        with self.assertRaises(NotFoundNaturalPerson):
            NaturalPersonController.delete_natural_person(999999999)                     
    
            


class TestIncomeDeclarationController(unittest.TestCase):
    """
    Class that contains tests for the income declaration controller.
    Each method verifies different functionalities of the controller.
    """

    def setUp(self):
        """
        Method that runs before each test.
        Clears the personal information, natural persons, and income declaration tables.
        Inserts a personal information object and a natural person object for the tests.
        """
        PersonalInfoController.clear_tables()
        NaturalPersonController.clear_tables()
        IncomeDeclarationController.clear_tables()
        self.info = PersonalInfo(1, "Daniel", "Ingeniero")
        PersonalInfoController.insert_personal_info(self.info)
        self.natural_person = NaturalPerson(1, 6000000000, 20000000, 10000000, 2000000, 3000000, 400000, 5000000, 600000, self.info)

        NaturalPersonController.insert_natural_person(self.natural_person, self.info.id)

    def test_insert_income_declaration(self):
        """
        Verifies the functionality of inserting an income declaration.
        An income declaration for a natural person is inserted and searched to confirm it was inserted correctly.
        """
        income_declaration = IncomeDeclaration(self.natural_person)
        IncomeDeclarationController.insert_income_declaration(self.natural_person.rut)

        found_declaration = IncomeDeclarationController.search_income_declaration(self.natural_person.rut)
        self.assertEqual(found_declaration.person.rut, self.natural_person.rut)
        self.assertEqual(found_declaration.total_taxable_income, income_declaration.total_taxable_income)
        self.assertEqual(found_declaration.total_non_taxable_income, income_declaration.total_non_taxable_income)

    def test_update_income_declaration(self):
        """
        Verifies the functionality of updating an income declaration.
        An income declaration is inserted, one of its attributes is updated,
        and it checks that the change has been applied correctly.
        """
        income_declaration = IncomeDeclaration(self.natural_person)
        IncomeDeclarationController.insert_income_declaration(self.natural_person.rut)

        updated_taxable_income = 70000
        IncomeDeclarationController.update_income_declaration(self.natural_person.rut, updated_taxable_income, 20000, 1000, 3000)

        found_declaration = IncomeDeclarationController.search_income_declaration(self.natural_person.rut)
        self.assertEqual(found_declaration.total_taxable_income, updated_taxable_income)

    def test_delete_income_declaration(self):
        
        """Verifies the functionality of deleting an income declaration.
        An income declaration is inserted and then deleted.
        An attempt to search for the deleted declaration should raise a NotFound exception."""
        
        IncomeDeclarationController.insert_income_declaration(self.natural_person.rut)

        IncomeDeclarationController.delete_income_declaration(self.natural_person.rut)

        with self.assertRaises(NotFoundIncomeDeclaration):
            IncomeDeclarationController.search_income_declaration(self.natural_person.rut)

    def test_insert_income_declaration_error(self):
        """
        Verifies that an error is raised when trying to insert an income declaration with invalid data.
        """
        with self.assertRaises(InsertionErrorIncomeDeclaration):
            IncomeDeclarationController.insert_income_declaration(999)

    def test_update_income_declaration_error(self):
        """
        Verifies that an error is raised when trying to update an income declaration with a non-existing RUT.
        """

        IncomeDeclarationController.insert_income_declaration(self.natural_person.rut)

        
        with self.assertRaises(NotFoundIncomeDeclaration):
            IncomeDeclarationController.update_income_declaration(999, 70000, 20000, 1000, 3000)

    def test_delete_income_declaration_error(self):
        """
        Verifies that an error is raised when trying to delete an income declaration that does not exist.
        """
        
        with self.assertRaises(NotFoundIncomeDeclaration):
            IncomeDeclarationController.delete_income_declaration(999)

    

        


if __name__ == '__main__':
    unittest.main()
