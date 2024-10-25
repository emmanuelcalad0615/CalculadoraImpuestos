import sys
sys.path.append("src")
import unittest
from Controller.IncomeDeclarationController import IncomeDeclarationController
from Controller.NaturalPersonController import NaturalPersonController, NotFound
from Controller.PersonalInfoController import PersonalInfoController
from TaxCalculator.IncomeDeclaration import IncomeDeclaration, PersonalInfo, NaturalPerson


class TestPersonalInfoController(unittest.TestCase):
    def setUp(self):
        PersonalInfoController.clear_tables()
        self.info = PersonalInfo(1, "Daniel", "Ingeniero")

    def test_insert_info(self):
        PersonalInfoController.insert_personal_info(self.info)
        find_info = PersonalInfoController.search_personal_info(self.info.id)
        self.assertEqual(find_info.id, self.info.id)
        self.assertEqual(find_info.name, self.info.name)
        self.assertEqual(find_info.ocupation, self.info.ocupation)

    def test_update_personal_info(self):
        PersonalInfoController.insert_personal_info(self.info)
        new_name = "Daniel Updated"
        new_occupation = "Senior Engineer"
        PersonalInfoController.update_personal_info(self.info.id, nombre=new_name, ocupacion=new_occupation)

        updated_info = PersonalInfoController.search_personal_info(self.info.id)
        self.assertEqual(updated_info.name,  new_name)
        self.assertEqual(updated_info.ocupation, new_occupation)    

    def test_search_personal_info(self):
        PersonalInfoController.insert_personal_info(self.info)
        found_info = PersonalInfoController.search_personal_info(self.info.id)
        self.assertEqual(found_info.id, self.info.id)
        self.assertEqual(found_info.name, self.info.name)
        self.assertEqual(found_info.ocupation, self.info.ocupation)    

class TestNaturalPersonController(unittest.TestCase):
    def setUp(self):
        NaturalPersonController.clear_tables()
        self.info = PersonalInfo(1, "Daniel", "Ingeniero")
        self.natural_person = NaturalPerson(1, 6000000000, 20000000, 10000000, 2000000, 3000000,400000, 5000000, 600000, self.info)
            

    def test_insert_natural_person(self):
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
        NaturalPersonController.insert_natural_person(self.natural_person, self.info.id)
        
        updated_income = 760000000
        NaturalPersonController.update_natural_person(self.natural_person.rut, laboral_income = updated_income)

        found_person = NaturalPersonController.search_natural_person(self.natural_person.rut)
        self.assertEqual(found_person.laboral_income, updated_income)  

    def test_search_natural_person(self):
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
    

    """def test_delete_natural_person(self):
        #NaturalPersonController.insert_natural_person(self.natural_person, self.info.id)
        

        with self.assertRaises(NotFound):
            NaturalPersonController.delete_natural_person(self.natural_person.rut)
            NaturalPersonController.search_natural_person(self.natural_person.rut)"""


class TestIncomeDeclarationController(unittest.TestCase):
    def setUp(self):
        PersonalInfoController.clear_tables()
        NaturalPersonController.clear_tables()
        IncomeDeclarationController.clear_tables()
        # Insert a sample PersonalInfo to associate with the NaturalPerson
        self.info = PersonalInfo(1, "Daniel", "Ingeniero")
        PersonalInfoController.insert_personal_info(self.info)
        self.natural_person = NaturalPerson(1, 6000000000, 20000000, 10000000, 2000000, 3000000,400000, 5000000, 600000, self.info)

        NaturalPersonController.insert_natural_person(self.natural_person, self.info.id)

    def test_insert_income_declaration(self):
        income_declaration = IncomeDeclaration(self.natural_person)
        IncomeDeclarationController.insert_income_declaration(self.natural_person.rut)

        found_declaration = IncomeDeclarationController.search_income_declaration(self.natural_person.rut)
        self.assertEqual(found_declaration.person.rut, self.natural_person.rut)
        self.assertEqual(found_declaration.total_taxable_income, income_declaration.total_taxable_income)
        self.assertEqual(found_declaration.total_non_taxable_income, income_declaration.total_non_taxable_income)
      

    def test_update_income_declaration(self):
        income_declaration = IncomeDeclaration(self.natural_person)
        IncomeDeclarationController.insert_income_declaration(self.natural_person.rut)

        updated_taxable_income = 70000
        IncomeDeclarationController.update_income_declaration(self.natural_person.rut, updated_taxable_income, 20000, 1000, 3000)

        found_declaration = IncomeDeclarationController.search_income_declaration(self.natural_person.rut)
        self.assertEqual(found_declaration.total_taxable_income, updated_taxable_income)

    """def test_delete_income_declaration(self):
        income_declaration = IncomeDeclaration(natural_person)
        IncomeDeclarationController.insert_income_declaration(natural_person.rut)

        IncomeDeclarationController.delete_income_declaration(natural_person.rut)

        with self.assertRaises(NotFound):
            IncomeDeclarationController.search_income_declaration(natural_person.rut)"""





        


        

  




    

    


if __name__ == '__main__':
    unittest.main()