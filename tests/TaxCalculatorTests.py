import unittest
import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, NaturalPerson, IncomeDeclaration, NegativeValues, LaboralIncomeZero, SocialSecurityPaymentsZero, SocialSecurityPaymentsExceedIncome, PensionContributionsExceedIncome, MortgagePaymentsExceedIncome, DonationsExceedIncome, EducationalExpensesExceedIncome, WithholdingSourceNegative, InsufficientIncomeForDeductions, CalculoException, BelowLimits, NegativeTaxes

class TestCalculadoraDeImpuestos(unittest.TestCase):

    def testCasoNormal1(self):
        # Average monthly income with some additional income
        information = PersonalInfo("Juan Pérez", 123456789, "Ingeniero", 11111111)

        person = NaturalPerson(
            laboral_income = 140000000,
            other_income = 2000000,
            withholding_source = 1000000,
            social_security_payments = 800000,
            pension_contributions = 500000,
            mortgage_payments = 300000,
            donations = 150000,
            educational_expenses = 200000, 
            personal_info = information 
            

    )
        expected_value = 48017500.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calcular_valor_impuesto()

        self.assertEqual(result, expected_value)

    def testCasoNormal2(self):
         # Income for a worker with additional income
        personal_info = PersonalInfo("María García", 987654321, "Abogada", 22222222)
        person = NaturalPerson(
            laboral_income = 200000000,  # Approximately 17 minimum wages
            other_income = 3000000,
            withholding_source = 1500000,
            social_security_payments = 1200000,
            pension_contributions = 800000,
            mortgage_payments = 500000,
            donations = 200000,
            educational_expenses = 300000, 
            personal_info = personal_info
        )
        expected_value = 68500000.0
        icome_declaration =IncomeDeclaration (person)
        result = icome_declaration.calcular_valor_impuesto()
        self.assertEqual(result, expected_value)

    def testCasoNormal3(self):
        # Income for a high-salaried worker
        personal_info = PersonalInfo("Carlos Sánchez", 112233445, "Médico", 33333333)
        person = NaturalPerson(
            laboral_income = 250000000,  # Approximately 22 minimum wages
            other_income = 2500000,
            withholding_source = 2000000,
            social_security_payments = 1500000,
            pension_contributions = 1000000,
            mortgage_payments = 800000,
            donations = 300000,
            educational_expenses = 400000,
            personal_info = personal_info
        )
        icome_declaration = IncomeDeclaration(person)
        expected_value = 84975000.0
        result = icome_declaration.calcular_valor_impuesto()
        self.assertEqual(result, expected_value)

    def testCasoNormal4(self):
       # Income for a person with an average salary and some additional income
        personal_info = PersonalInfo("Ana Rodríguez", 556677889, "Profesor", 44444444)
        person = NaturalPerson(
            laboral_income = 51100000,  # Approximately 14 minimum wages
            other_income = 2500000,
            withholding_source = 1200000,
            social_security_payments = 1000000,
            pension_contributions = 600000,
            mortgage_payments = 400000,
            donations = 200000,
            educational_expenses = 250000, 
            personal_info= personal_info

        )
        expected_value = 16702500.0
        icome_declaration = IncomeDeclaration(person)
        result = icome_declaration.calcular_valor_impuesto()
        self.assertEqual(result, expected_value)

    def testCasoNormal5(self):
        
        personal_info = PersonalInfo("Luis Fernández", 998877665, "Arquitecto", 55555555)
        person = NaturalPerson(
            laboral_income = 120000000,  # Approximately 10 minimum wages
            other_income = 1500000,
            withholding_source = 800000,
            social_security_payments = 600000,
            pension_contributions = 400000,
            mortgage_payments = 300000,
            donations = 100000,
            educational_expenses = 150000, 
            personal_info = personal_info
        )
        expected_value = 41182500.0
        income_declaration = IncomeDeclaration(person)
        
        result = income_declaration.calcular_valor_impuesto()
        self.assertEqual(result, expected_value)
        

    def testCasoNormal6(self):
        
            # Average income with various expenses
        personal_info = PersonalInfo("Laura López", 223344556, "Contadora", 66666666)    
        person = NaturalPerson(
            laboral_income = 200000000,  # Approximately 17 minimum wages
            other_income = 2000000,
            withholding_source = 1000000,
            social_security_payments = 800000,
            pension_contributions = 600000,
            mortgage_payments = 500000,
            donations = 150000,
            educational_expenses = 250000,
            personal_info = personal_info

        )
        expected_value = 68895000.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calcular_valor_impuesto()
        self.assertEqual(result, expected_value)

    def testCasoExtra1(self):
            # High expenses compared to income
            personal_info = PersonalInfo("José Martínez", 887766554, "Diseñador", 77777777)
            person = NaturalPerson(
                laboral_income = 200000000,  # Approximately 17 minimum wages
                other_income = 30000000,
                withholding_source = 15000000,
                social_security_payments = 30000000,
                pension_contributions = 20000000,
                mortgage_payments = 12000000,
                donations = 10000000,
                educational_expenses = 10000000,
                personal_info= personal_info
            )
            expected_value = 36800000.0
            income_declaration = IncomeDeclaration(person)
            resultado = income_declaration.calcular_valor_impuesto()
            self.assertEqual(resultado, expected_value)
                

    def testCasoExtra2(self):
        # High income and high expenses in donations
        personal_info = PersonalInfo("Pedro Gómez", 334455667, "Programador", 88888888)
        person = NaturalPerson(
            laboral_income=250000000,
            other_income=50000000,
            withholding_source=20000000,
            social_security_payments=15000000,
            pension_contributions=10000000,
            mortgage_payments=8000000,
            donations=30000000,  # High compared to income
            educational_expenses=4000000,
            personal_info = personal_info
        )
        expected_value = 61550000.0
        income_declaration = IncomeDeclaration(person)
        resultado = income_declaration.calcular_valor_impuesto()
        self.assertEqual(resultado, expected_value)

    def testCasoExtra3(self):
        # High income with substantial education expenses
        personal_info = PersonalInfo("Elena Pérez", 556677889, "Veterinaria", 99999999)
        person = NaturalPerson(
            laboral_income=300000000,
            other_income=40000000,
            withholding_source=25000000,
            social_security_payments=20000000,
            pension_contributions=15000000,
            mortgage_payments=10000000,
            donations=5000000,
            educational_expenses=30000000,
            personal_info = personal_info    # Very high compared to other expenses
        )
        expected_value = 66000000.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calcular_valor_impuesto()
        self.assertEqual(result, expected_value)

    def testCasoExtra4(self):
        # Low income with very high social security expenses
        personal_info = PersonalInfo("Sofía Hernández", 112233445, "Psicóloga", 10101010)
        person = NaturalPerson(
            laboral_income=140000000,
            other_income=20000000,
            withholding_source=10000000,
            social_security_payments=70000000,  # Very high compared to income
            pension_contributions=5000000,
            mortgage_payments=3000000,
            donations=1500000,
            educational_expenses=2000000,
            personal_info = personal_info 
        )
        expected_value = 17475000.0
        income_declaration = IncomeDeclaration(person)
        resultado = income_declaration.calcular_valor_impuesto()
        self.assertEqual(resultado, expected_value)

    def testCasoExtra5(self):
        # Moderate income with high donations and credit payments
        personal_info = PersonalInfo("Miguel Torres", 223344556, "Abogado", 20202020)
        person = NaturalPerson(
            laboral_income=180000000,
            other_income=25000000,
            withholding_source=13000000,
            social_security_payments=9000000,
            pension_contributions=7000000,
            mortgage_payments=30000000,  # High compared to income
            donations=25000000,  # High compared to income
            educational_expenses=3000000,
            personal_info = personal_info
        )
        expected_value = 32850000.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calcular_valor_impuesto()
        self.assertEqual(result, expected_value)

    def testCasoExtra6(self):
        # High income with all expenses elevated
        personal_info = PersonalInfo("Isabel Díaz", 556677889, "Doctora", 30303030)
        person = NaturalPerson(
            laboral_income=350000000,
            other_income=50000000,
            withholding_source=30000000,
            social_security_payments=25000000,
            pension_contributions=20000000,
            mortgage_payments=15000000,
            donations=10000000,
            educational_expenses=15000000,
            personal_info = personal_info 
        )
        expected_value = 80250000.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calcular_valor_impuesto()
        self.assertEqual(result, expected_value)


    def test_negative_values(self):
        # Test negative values for any input field
        with self.assertRaises(NegativeValues):
            person = NaturalPerson(laboral_income=-50000, other_income=10000, withholding_source=5000,
                                   social_security_payments=2000, pension_contributions=1000, mortgage_payments=1500, 
                                   donations=3000, educational_expenses=1000, personal_info=None)

    def test_laboral_income_zero(self):
        # Test when laboral income is zero
        with self.assertRaises(LaboralIncomeZero):
            person = NaturalPerson(laboral_income=0, other_income=10000, withholding_source=5000,
                                   social_security_payments=2000, pension_contributions=1000, mortgage_payments=1500, 
                                   donations=3000, educational_expenses=1000, personal_info=None)

    def test_social_security_payments_zero(self):
        # Test when social security payments are zero
        with self.assertRaises(SocialSecurityPaymentsZero):
            person = NaturalPerson(laboral_income=50000, other_income=10000, withholding_source=5000,
                                   social_security_payments=0, pension_contributions=1000, mortgage_payments=1500, 
                                   donations=3000, educational_expenses=1000, personal_info=None)

    def test_social_security_exceed_income(self):
        # Test when social security payments exceed laboral income
        with self.assertRaises(SocialSecurityPaymentsExceedIncome):
            person = NaturalPerson(laboral_income=50000, other_income=10000, withholding_source=5000,
                                   social_security_payments=60000, pension_contributions=1000, mortgage_payments=1500, 
                                   donations=3000, educational_expenses=1000, personal_info=None)

    def test_pension_contributions_exceed_income(self):
        # Test when pension contributions exceed laboral income
        with self.assertRaises(PensionContributionsExceedIncome):
            person = NaturalPerson(laboral_income=50000, other_income=10000, withholding_source=5000,
                                   social_security_payments=2000, pension_contributions=60000, mortgage_payments=1500, 
                                   donations=3000, educational_expenses=1000, personal_info=None)

    def test_mortgage_payments_exceed_income(self):
        # Test when mortgage payments exceed laboral income
        with self.assertRaises(MortgagePaymentsExceedIncome):
            person = NaturalPerson(laboral_income=50000, other_income=10000, withholding_source=5000,
                                   social_security_payments=2000, pension_contributions=1000, mortgage_payments=60000, 
                                   donations=3000, educational_expenses=1000, personal_info=None)

    def test_donations_exceed_income(self):
        # Test when donations exceed laboral income
        with self.assertRaises(DonationsExceedIncome):
            person = NaturalPerson(laboral_income=50000, other_income=10000, withholding_source=5000,
                                   social_security_payments=2000, pension_contributions=1000, mortgage_payments=1500, 
                                   donations=70000, educational_expenses=1000, personal_info=None)

    def test_educational_expenses_exceed_income(self):
        # Test when educational expenses exceed sum of laboral and other income
        with self.assertRaises(EducationalExpensesExceedIncome):
            person = NaturalPerson(laboral_income=50000, other_income=10000, withholding_source=5000,
                                   social_security_payments=2000, pension_contributions=1000, mortgage_payments=1500, 
                                   donations=3000, educational_expenses=70000, personal_info=None)

    def test_withholding_source_negative(self):
        with self.assertRaises(NegativeValues):
            person = NaturalPerson(laboral_income=50000, other_income=10000, withholding_source=-5000,
                                   social_security_payments=2000, pension_contributions=1000, mortgage_payments=1500, 
                                   donations=3000, educational_expenses=1000, personal_info=None)


    def test_insufficient_income_for_deductions(self):
        # Establecemos deducciones mayores que los ingresos
        person = NaturalPerson(
            laboral_income=10000, 
            other_income=0, 
            withholding_source=0,
            social_security_payments=5000, 
            pension_contributions=2000, 
            mortgage_payments=3000, 
            donations=500, 
            educational_expenses=1000, 
            personal_info=None
        )

        # El total de las deducciones (5000 + 2000 + 3000 + 500 + 1000) = 11500
        # Dado que las deducciones (11500) exceden el ingreso laboral (10000), 
        # se debería lanzar la excepción InsufficientIncomeForDeductions
        with self.assertRaises(InsufficientIncomeForDeductions):
            icome_declaration = IncomeDeclaration(person)
            icome_declaration.calcular_valor_impuesto()

    def test_valid_person(self):
        # Test valid input without triggering any exceptions
        try:
            person = NaturalPerson(laboral_income=50000, other_income=10000, withholding_source=5000,
                                   social_security_payments=2000, pension_contributions=1000, mortgage_payments=1500, 
                                   donations=3000, educational_expenses=1000, personal_info=None)
            self.assertIsInstance(person, NaturalPerson)
        except CalculoException:
            self.fail("NaturalPerson raised CalculoException unexpectedly!")

    def test_below_limits_exception(self):
        # Update this test to use a non-zero value for social_security_payments
        person = NaturalPerson(laboral_income=50000, other_income=0, withholding_source=0,
                               social_security_payments=1000, pension_contributions=0, mortgage_payments=0, 
                               donations=0, educational_expenses=0, personal_info=None)
        income_declaration = IncomeDeclaration(person)
    
        with self.assertRaises(BelowLimits):
            income_declaration.calcular_valor_impuesto()




if __name__ == "__main__":
    unittest.main()