import sys
sys.path.append("src")
import unittest
from Controller.IncomeDeclarationController import IncomeDeclarationController
from Controller.NaturalPersonController import NaturalPersonController
from Controller.PersonalInfoController import PersonalInfoController, NotFound
from TaxCalculator.IncomeDeclaration import IncomeDeclaration, PersonalInfo, NaturalPerson


class TestPersonalInfoController(unittest.TestCase):
    def setUp(self):
        # Create a test PersonalInfo object
        self.personal_info = PersonalInfo(nombre="John Doe", id=12345678, ocupacion="Engineer", rut=12345678)
        PersonalInfoController.insert_personal_info(self.personal_info)

        

  


class TestNaturalPersonController(unittest.TestCase):
    def setUp(self):
        # Create a test PersonalInfo object
        self.personal_info = PersonalInfo(nombre="John Doe", id=12345678, ocupacion="Engineer", rut=12345678)
        PersonalInfoController.insert_personal_info(self.personal_info)

        # Create a test NaturalPerson object
        self.natural_person = NaturalPerson(
            laboral_income=50000,
            other_income=10000,
            withholding_source=5000,
            social_security_payments=3000,
            pension_contributions=2000,
            mortgage_payments=4000,
            donations=1000,
            educational_expenses=500,
            personal_info=self.personal_info
        )
        NaturalPersonController.insert_natural_person(self.natural_person, self.personal_info.id, self.personal_info.rut)


    def test_insert_natural_person_success(self):
        # Create a PersonalInfo object
        personal_info = PersonalInfo(nombre="John Doe", id=1, ocupacion="Engineer", rut=12345678)

        # Create a NaturalPerson object
        natural_person = NaturalPerson(
            laboral_income=50000,
            other_income=10000,
            withholding_source=5000,
            social_security_payments=3000,
            pension_contributions=2000,
            mortgage_payments=4000,
            donations=1000,
            educational_expenses=500,
            personal_info=personal_info
        )

        # Call the insertion method
        result = NaturalPersonController.insert_natural_person(natural_person, personal_info.id, personal_info.rut)

        # Check the result
        self.assertIsNone(result)  # Assuming the method returns None on success

    
    def test_update_natural_person_success(self):
        # Update the natural person's data
        updated_income = 60000
        result = NaturalPersonController.update_natural_person(
            rut=12345678,
            laboral_income=updated_income,
            other_income=None,
            withholding_source=None,
            social_security_payments=None,
            pension_contributions=None,
            mortgage_payments=None,
            donations=None,
            educational_expenses=None
        )

        # Check the result (assuming the method returns None on success)
        self.assertIsNone(result)

        # Verify the update
        updated_person = NaturalPersonController.search_natural_person(12345678)  # Example method
        self.assertEqual(updated_person[1], updated_income)   

       


class TestIncomeDeclarationController(unittest.TestCase):
    pass

    

    


if __name__ == '__main__':
    unittest.main()