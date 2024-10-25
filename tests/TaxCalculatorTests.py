import unittest
import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import (
    PersonalInfo, NaturalPerson, IncomeDeclaration,
    NegativeValues, LaboralIncomeZero, SocialSecurityPaymentsZero,
    SocialSecurityPaymentsExceedIncome, PensionContributionsExceedIncome,
    MortgagePaymentsExceedIncome, DonationsExceedIncome,
    EducationalExpensesExceedIncome, WithholdingSourceNegative,
    InsufficientIncomeForDeductions, CalculoException, BelowLimits,
    NegativeTaxes
)

class TestCalculadoraDeImpuestos(unittest.TestCase):

    def testCasoNormal1(self):
        # Average monthly income with some additional income
        information = PersonalInfo("Juan Pérez", 123456789, "Ingeniero")

        person = NaturalPerson(
            rut=11111111,
            laboral_income=140000000,
            other_income=2000000,
            withholding_source=1000000,
            social_security_payments=800000,
            pension_contributions=500000,
            mortgage_payments=300000,
            donations=150000,
            educational_expenses=200000,
            personal_info=information
        )

        expected_value = 48017500.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calculate_tax_value()

        self.assertEqual(result, expected_value)

    def testCasoNormal2(self):
        # Income for a worker with additional income
        personal_info = PersonalInfo("María García", 987654321, "Abogada")
        person = NaturalPerson(
            rut=22222222,
            laboral_income=200000000,
            other_income=3000000,
            withholding_source=1500000,
            social_security_payments=1200000,
            pension_contributions=800000,
            mortgage_payments=500000,
            donations=200000,
            educational_expenses=300000,
            personal_info=personal_info
        )
        expected_value = 68500000.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calculate_tax_value()
        self.assertEqual(result, expected_value)

    def testCasoNormal3(self):
        # Income for a high-salaried worker
        personal_info = PersonalInfo("Carlos Sánchez", 112233445, "Médico")
        person = NaturalPerson(
            rut=33333333,
            laboral_income=250000000,
            other_income=2500000,
            withholding_source=2000000,
            social_security_payments=1500000,
            pension_contributions=1000000,
            mortgage_payments=800000,
            donations=300000,
            educational_expenses=400000,
            personal_info=personal_info
        )
        expected_value = 84975000.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calculate_tax_value()
        self.assertEqual(result, expected_value)

    def testCasoNormal4(self):
        # Income for a person with an average salary and some additional income
        personal_info = PersonalInfo("Ana Rodríguez", 556677889, "Profesor")
        person = NaturalPerson(
            rut=44444444,
            laboral_income=51100000,
            other_income=2500000,
            withholding_source=1200000,
            social_security_payments=1000000,
            pension_contributions=600000,
            mortgage_payments=400000,
            donations=200000,
            educational_expenses=250000,
            personal_info=personal_info
        )
        expected_value = 16702500.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calculate_tax_value()
        print(result)
        self.assertEqual(result, expected_value)

    def testCasoNormal5(self):
        personal_info = PersonalInfo("Luis Fernández", 998877665, "Arquitecto")
        person = NaturalPerson(
            rut=55555555,
            laboral_income=120000000,
            other_income=1500000,
            withholding_source=800000,
            social_security_payments=600000,
            pension_contributions=400000,
            mortgage_payments=300000,
            donations=100000,
            educational_expenses=150000,
            personal_info=personal_info
        )
        expected_value = 41182500.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calculate_tax_value()
        self.assertEqual(result, expected_value)

    def testCasoNormal6(self):
        personal_info = PersonalInfo("Laura López", 223344556, "Contadora")
        person = NaturalPerson(
            rut=66666666,
            laboral_income=200000000,
            other_income=2000000,
            withholding_source=1000000,
            social_security_payments=800000,
            pension_contributions=600000,
            mortgage_payments=500000,
            donations=150000,
            educational_expenses=250000,
            personal_info=personal_info
        )
        expected_value = 68895000.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calculate_tax_value()
        self.assertEqual(result, expected_value)

    def testCasoExtra1(self):
        personal_info = PersonalInfo("José Martínez", 887766554, "Diseñador")
        person = NaturalPerson(
            rut=77777777,
            laboral_income=200000000,
            other_income=30000000,
            withholding_source=15000000,
            social_security_payments=30000000,
            pension_contributions=20000000,
            mortgage_payments=12000000,
            donations=10000000,
            educational_expenses=10000000,
            personal_info=personal_info
        )
        expected_value = 36800000.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calculate_tax_value()
        self.assertEqual(result, expected_value)

    def testCasoExtra2(self):
        personal_info = PersonalInfo("Pedro Gómez", 334455667, "Programador")
        person = NaturalPerson(
            rut=88888888,
            laboral_income=250000000,
            other_income=50000000,
            withholding_source=20000000,
            social_security_payments=15000000,
            pension_contributions=10000000,
            mortgage_payments=8000000,
            donations=30000000,
            educational_expenses=4000000,
            personal_info=personal_info
        )
        expected_value = 61550000.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calculate_tax_value()
        self.assertEqual(result, expected_value)

    def testCasoExtra3(self):
        personal_info = PersonalInfo("Elena Pérez", 556677889, "Veterinaria")
        person = NaturalPerson(
            rut=99999999,
            laboral_income=300000000,
            other_income=40000000,
            withholding_source=25000000,
            social_security_payments=20000000,
            pension_contributions=15000000,
            mortgage_payments=10000000,
            donations=5000000,
            educational_expenses=30000000,
            personal_info=personal_info
        )
        expected_value = 66000000.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calculate_tax_value()
        self.assertEqual(result, expected_value)

    def testCasoExtra4(self):
        personal_info = PersonalInfo("Sofía Hernández", 112233445, "Psicóloga")
        person = NaturalPerson(
            rut=10101010,
            laboral_income=140000000,
            other_income=20000000,
            withholding_source=10000000,
            social_security_payments=70000000,
            pension_contributions=5000000,
            mortgage_payments=3000000,
            donations=1500000,
            educational_expenses=2000000,
            personal_info=personal_info
        )
        expected_value = 17475000.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calculate_tax_value()
        self.assertEqual(result, expected_value)

    def testCasoExtra5(self):
        personal_info = PersonalInfo("Miguel Torres", 223344556, "Abogado")
        person = NaturalPerson(
            rut=20202020,
            laboral_income=180000000,
            other_income=25000000,
            withholding_source=13000000,
            social_security_payments=9000000,
            pension_contributions=7000000,
            mortgage_payments=30000000,
            donations=25000000,
            educational_expenses=3000000,
            personal_info=personal_info
        )
        expected_value = 32850000.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calculate_tax_value()
        self.assertEqual(result, expected_value)

    def testCasoExtra6(self):
        personal_info = PersonalInfo("Isabel Díaz", 556677889, "Doctora")
        person = NaturalPerson(
            rut=30303030,
            laboral_income=350000000,
            other_income=50000000,
            withholding_source=30000000,
            social_security_payments=25000000,
            pension_contributions=20000000,
            mortgage_payments=15000000,
            donations=10000000,
            educational_expenses=15000000,
            personal_info=personal_info
        )
        expected_value = 80250000.0
        income_declaration = IncomeDeclaration(person)
        result = income_declaration.calculate_tax_value()
        self.assertEqual(result, expected_value)

    

    def test_laboral_income_zero(self):
        with self.assertRaises(LaboralIncomeZero):
            NaturalPerson(
                rut=1,
                laboral_income=0,
                other_income=10000,
                withholding_source=5000,
                social_security_payments=2000,
                pension_contributions=1000,
                mortgage_payments=1500,
                donations=3000,
                educational_expenses=1000
            )

    def test_social_security_payments_zero(self):
        with self.assertRaises(SocialSecurityPaymentsZero):
            NaturalPerson(
                rut=1,
                laboral_income=50000,
                other_income=10000,
                withholding_source=5000,
                social_security_payments=0,
                pension_contributions=1000,
                mortgage_payments=1500,
                donations=3000,
                educational_expenses=1000
            )

    def test_social_security_exceed_income(self):
        with self.assertRaises(SocialSecurityPaymentsExceedIncome):
            NaturalPerson(
                rut=1,
                laboral_income=50000,
                other_income=10000,
                withholding_source=5000,
                social_security_payments=60000,
                pension_contributions=1000,
                mortgage_payments=1500,
                donations=3000,
                educational_expenses=1000
            )

    def test_pension_contributions_exceed_income(self):
        with self.assertRaises(PensionContributionsExceedIncome):
            NaturalPerson(
                rut=1,
                laboral_income=50000,
                other_income=10000,
                withholding_source=5000,
                social_security_payments=2000,
                pension_contributions=60000,
                mortgage_payments=1500,
                donations=3000,
                educational_expenses=1000
            )

    def test_mortgage_payments_exceed_income(self):
        with self.assertRaises(MortgagePaymentsExceedIncome):
            NaturalPerson(
                rut=1,
                laboral_income=50000,
                other_income=10000,
                withholding_source=5000,
                social_security_payments=2000,
                pension_contributions=1000,
                mortgage_payments=60000,
                donations=3000,
                educational_expenses=1000
            )

    def test_donations_exceed_income(self):
        with self.assertRaises(DonationsExceedIncome):
            NaturalPerson(
                rut=1,
                laboral_income=50000,
                other_income=10000,
                withholding_source=5000,
                social_security_payments=2000,
                pension_contributions=1000,
                mortgage_payments=1500,
                donations=70000,
                educational_expenses=1000
            )

    def test_educational_expenses_exceed_income(self):
        with self.assertRaises(EducationalExpensesExceedIncome):
            NaturalPerson(
                rut=1,
                laboral_income=50000,
                other_income=10000,
                withholding_source=5000,
                social_security_payments=2000,
                pension_contributions=1000,
                mortgage_payments=1500,
                donations=3000,
                educational_expenses=70000
            )

    def test_withholding_source_negative(self):
        with self.assertRaises(WithholdingSourceNegative):
            NaturalPerson(
                rut=1,
                laboral_income=50000,
                other_income=10000,
                withholding_source=-5000,
                social_security_payments=2000,
                pension_contributions=1000,
                mortgage_payments=1500,
                donations=3000,
                educational_expenses=1000
            )

    def test_insufficient_income_for_deductions(self):
        with self.assertRaises(InsufficientIncomeForDeductions):
            NaturalPerson(
                rut=1,
                laboral_income=50000,
                other_income=10000,
                withholding_source=5000,
                social_security_payments=2000,
                pension_contributions=1000,
                mortgage_payments=1500,
                donations=3000,
                educational_expenses=60000
            )

    def test_below_limits_exception(self):
        person = NaturalPerson(
            rut=12345678,                       # RUT del contribuyente
            laboral_income=50000000,            # Ingreso laboral (60 millones, válido para declaración)
            other_income=0,                # Otros ingresos (5 millones)
            withholding_source=7000000,          # Retenciones en la fuente (7 millones)
            social_security_payments=2000000,    # Pagos de seguridad social (2 millones)
            pension_contributions=1000000,        # Aportaciones a pensiones (1 millón)
            mortgage_payments=3000000,           # Pagos de hipoteca (3 millones)
            donations=1000000,                    # Donaciones (1 millón)
            educational_expenses=2000000,        # Gastos educativos (2 millones)
            personal_info=None          
        )
        with self.assertRaises(BelowLimits):
            income_declaration = IncomeDeclaration(person)
            income_declaration.calculate_tax_value()

if __name__ == "__main__":
    unittest.main()
