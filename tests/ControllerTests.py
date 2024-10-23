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

    def test_insert_personal_info_success(self):
        # Create a PersonalInfo object
        personal_info = PersonalInfo(nombre="John Doe", id=1, ocupacion="Engineer", rut=12345678)

        # Call the insertion method
        result = PersonalInfoController.insert_personal_info(personal_info)

        # Check the result
        self.assertIsNone(result)  # Assuming the method returns None on success

    def test_update_personal_info_success(self):
        # Update the information
        updated_name = "Jane Doe"
        updated_occupation = "Senior Engineer"
        
        result = PersonalInfoController.update_personal_info(
            cedula=12345678,
            nombre=updated_name,
            ocupacion=updated_occupation
        )

        # Check the result (assuming the method returns None on success)
        self.assertIsNone(result)

        # Verify the update
        updated_info = PersonalInfoController.search_personal_info(12345678)  # Example method
        self.assertEqual(updated_info[1], updated_name)
        self.assertEqual(updated_info[2], updated_occupation)
    
    def test_delete_personal_info(self):
        cedula = 12345678
        personal_info = PersonalInfo(id=cedula, nombre="Juan Pérez", ocupacion="Ingeniero", rut= 1234)
        
        # Crear la tabla
        PersonalInfoController.create_table()
        
        # Insertar información personal
        PersonalInfoController.insert_personal_info(personal_info)

        # Verificar que la información se haya insertado correctamente
        result = PersonalInfoController.search_personal_info(cedula)
        self.assertIsNotNone(result, "No se encontró información personal después de la inserción.")

        # Eliminar la información personal
        PersonalInfoController.delete_personal_info(cedula)

        # Verificar que la información haya sido eliminada
        with self.assertRaises(NotFound):
            PersonalInfoController.search_personal_info(cedula)

        # Limpiar la base de datos
        PersonalInfoController.BorrarFilas()    

  


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

    def test_insert_income_declaration_success(self):
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

        # Create an IncomeDeclaration object
        income_declaration = IncomeDeclaration(person=natural_person)

        # Set values for the income declaration
        income_declaration.total_ingresos_gravados = 15000
        income_declaration.total_ingresos_no_gravados = 6000
        income_declaration.total_costos_deducibles = 4000
        income_declaration.valor_impuesto = 2500

        # Call the insertion method
        result = IncomeDeclarationController.insert_income_declaration(income_declaration, personal_info.rut)

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

        # Create an IncomeDeclaration object
        self.income_declaration = IncomeDeclaration(person=self.natural_person)
        IncomeDeclarationController.insert_income_declaration(self.income_declaration, self.natural_person.personal_info.rut)

    def test_update_income_declaration_success(self):
        # Update the income declaration values
        updated_gravados = 20000
        updated_no_gravados = 8000
        updated_costos_deducibles = 5000
        updated_valor_impuesto = 3000

        result = IncomeDeclarationController.update_income_declaration(
            rut=12345678,
            total_ingresos_gravados=updated_gravados,
            total_ingresos_no_gravados=updated_no_gravados,
            total_costos_deducibles=updated_costos_deducibles,
            valor_impuesto=updated_valor_impuesto
        )

        # Check the result (assuming the method returns None on success)
        self.assertIsNone(result)

        # Verify the update (if you have a method to retrieve the updated info)
        updated_declaration = IncomeDeclarationController.serch_income_declaration(12345678)  # Example method
        self.assertEqual(updated_declaration[1], updated_gravados)
        self.assertEqual(updated_declaration[2], updated_no_gravados)
        self.assertEqual(updated_declaration[3], updated_costos_deducibles)
        self.assertEqual(updated_declaration[4], updated_valor_impuesto)

    


if __name__ == '__main__':
    unittest.main()