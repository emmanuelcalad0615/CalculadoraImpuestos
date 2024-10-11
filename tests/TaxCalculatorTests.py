import unittest
from Calculadora_tests import CalculadoraDeImpuestos
from Exceptions import(
    NegativeValuesError,
    LaborIncomeLessThanZero,
    SocialSecurityPaymentsGreaterThanIncome,
    PensionContributionsGreaterThanIncome,
    MortgagePaymentsGreaterThanIncome,
    DonationsGreaterThanIncome,
    EducationExpensesGreaterThanTotalIncome,
    NegativeWithholdingTax,
    ZeroSocialSecurityPayments,
    InsufficientIncome,
    NegativeTaxes

)

class TestCalculadoraDeImpuestos(unittest.TestCase):

    def setUp(self):
        calculadora = CalculadoraDeImpuestos(
            labor_income=50000000,
            other_income=10000000,
            withholding_tax=5000000,
            social_security_payments=4000000,
            pension_contributions=3000000,
            mortgage_payments=2000000,
            donations=1000000,
            education_expenses=500000
        )
        valor_esperado = 4405000.0 
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoNormal1(self):
        # Average monthly income with some additional income
        calculadora = CalculadoraDeImpuestos(
            labor_income = 14000000,
            other_income = 2000000,
            withholding_tax = 1000000,
            social_security_payments = 800000,
            pension_contributions = 500000,
            mortgage_payments = 300000,
            donations = 150000,
            education_expenses = 200000

    )
        valor_esperado = 1669500.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoNormal2(self):
         # Income for a worker with additional income
        calculadora = CalculadoraDeImpuestos(
            labor_income = 20000000,  # Approximately 17 minimum wages
            other_income = 3000000,
            withholding_tax = 1500000,
            social_security_payments = 1200000,
            pension_contributions = 800000,
            mortgage_payments = 500000,
            donations = 200000,
            education_expenses = 300000
        )
        valor_esperado = 2300000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoNormal3(self):
        # Income for a high-salaried worker
        calculadora = CalculadoraDeImpuestos(
            labor_income = 25000000,  # Approximately 22 minimum wages
            other_income = 2500000,
            withholding_tax = 2000000,
            social_security_payments = 1500000,
            pension_contributions = 1000000,
            mortgage_payments = 800000,
            donations = 300000,
            education_expenses = 400000
        )
        valor_esperado = 2465000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoNormal4(self):
       # Income for a person with an average salary and some additional income
        calculadora = CalculadoraDeImpuestos(
            labor_income = 16000000,  # Approximately 14 minimum wages
            other_income = 2500000,
            withholding_tax = 1200000,
            social_security_payments = 1000000,
            pension_contributions = 600000,
            mortgage_payments = 400000,
            donations = 200000,
            education_expenses = 250000

        )
        valor_esperado = 1849500.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoNormal5(self):
        
           # Low income with moderate education expenses
        calculadora = CalculadoraDeImpuestos(
            labor_income = 12000000,  # Approximately 10 minimum wages
            other_income = 1500000,
            withholding_tax = 800000,
            social_security_payments = 600000,
            pension_contributions = 400000,
            mortgage_payments = 300000,
            donations = 100000,
            education_expenses = 150000
        )
        valor_esperado = 1470500.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)
        

    def testCasoNormal6(self):
        
            # Average income with various expenses
        calculadora = CalculadoraDeImpuestos(
            labor_income = 20000000,  # Approximately 17 minimum wages
            other_income = 2000000,
            withholding_tax = 1000000,
            social_security_payments = 800000,
            pension_contributions = 600000,
            mortgage_payments = 500000,
            donations = 150000,
            education_expenses = 250000,

        )
        valor_esperado = 2743000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoExtra1(self):
            # High expenses compared to income
            calculadora = CalculadoraDeImpuestos(
                labor_income = 20000000,  # Approximately 17 minimum wages
                other_income = 3000000,
                withholding_tax = 1500000,
                social_security_payments = 3000000,
                pension_contributions = 2000000,
                mortgage_payments = 1200000,
                donations = 1000000,
                education_expenses = 1000000
            )
            valor_esperado = 1312000.0
            resultado = calculadora.calcular_valor_impuesto()
            self.assertEqual(resultado, valor_esperado)
                

    def testCasoExtra2(self):
        # High income and high expenses in donations
        calculadora = CalculadoraDeImpuestos(
            labor_income=25000000,
            other_income=5000000,
            withholding_tax=2000000,
            social_security_payments=1500000,
            pension_contributions=1000000,
            mortgage_payments=800000,
            donations=3000000,  # High compared to income
            education_expenses=400000
        )
        valor_esperado = 2427000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoExtra3(self):
        # High income with substantial education expenses
        calculadora = CalculadoraDeImpuestos(
            labor_income=30000000,
            other_income=4000000,
            withholding_tax=2500000,
            social_security_payments=2000000,
            pension_contributions=1500000,
            mortgage_payments=1000000,
            donations=500000,
            education_expenses=3000000  # Very high compared to other expenses
        )
        valor_esperado = 2440000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoExtra4(self):
        # Low income with very high social security expenses
        calculadora = CalculadoraDeImpuestos(
            labor_income=14000000,
            other_income=2000000,
            withholding_tax=1000000,
            social_security_payments=7000000,  # Very high compared to income
            pension_contributions=500000,
            mortgage_payments=300000,
            donations=150000,
            education_expenses=200000
        )
        valor_esperado = 491500.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoExtra5(self):
        # Moderate income with high donations and credit payments
        calculadora = CalculadoraDeImpuestos(
            labor_income=18000000,
            other_income=2500000,
            withholding_tax=1300000,
            social_security_payments=900000,
            pension_contributions=700000,
            mortgage_payments=3000000,  # High compared to income
            donations=2500000,  # High compared to income
            education_expenses=300000
        )
        valor_esperado = 1189000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoExtra6(self):
        # High income with all expenses elevated
        
        calculadora = CalculadoraDeImpuestos(
            labor_income=35000000,
            other_income=5000000,
            withholding_tax=3000000,
            social_security_payments=2500000,
            pension_contributions=2000000,
            mortgage_payments=1500000,
            donations=1000000,
            education_expenses=1500000
        )
        valor_esperado = 2985000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)


    def testCasoErrorValoresNegativos(self):
            CalculadoraDeImpuestos(
                labor_income=15000000,
                other_income=2000000,
                withholding_tax=1000000,
                social_security_payments=200000,
                pension_contributions=600000,
                mortgage_payments=400000,
                donations=150000,
                education_expenses=200000
            )

    def testCasoErrorIngresosLaboralesCero(self):
            CalculadoraDeImpuestos(
                labor_income=12000000,
                other_income=3000000,
                withholding_tax=1000000,
                social_security_payments=1200000,
                pension_contributions=800000,
                mortgage_payments=500000,
                donations=200000,
                education_expenses=300000
            )

    def testCasoErrorPagosSeguridadSocial(self):
            CalculadoraDeImpuestos(
                labor_income=25000000,
                other_income=2000000,
                withholding_tax=1500000,
                social_security_payments=30000,
                pension_contributions=500000,
                mortgage_payments=600000,
                donations=200000,
                education_expenses=400000
            )

    def testCasoErrorAportesPension(self):
            CalculadoraDeImpuestos(
                labor_income=20000000,
                other_income=1000000,
                withholding_tax=800000,
                social_security_payments=500000,
                pension_contributions=21000,
                mortgage_payments=300000,
                donations=100000,
                education_expenses=150000
            )

    def testCasoErrorPagosHipotecarios(self):
            CalculadoraDeImpuestos(
                labor_income=15000000,
                other_income=1000000,
                withholding_tax=700000,
                social_security_payments=600000,
                pension_contributions=400000,
                mortgage_payments=16000,
                donations=80000,
                education_expenses=100000
            )

    def testCasoErrorDonaciones(self):
            CalculadoraDeImpuestos(
                labor_income=5000000,
                other_income=200000,
                withholding_tax=300000,
                social_security_payments=200000,
                pension_contributions=100000,
                mortgage_payments=50000,
                donations=60000,
                education_expenses=70000
            )

    def testCasoErrorGastosEducacion(self):
            CalculadoraDeImpuestos(
                labor_income=12000000,
                other_income=500000,
                withholding_tax=900000,
                social_security_payments=400000,
                pension_contributions=300000,
                mortgage_payments=200000,
                donations=100000,
                education_expenses=13000
            )

    def testCasoErrorRetencionFuenteNegativa(self):
            CalculadoraDeImpuestos(
                labor_income=10000000,
                other_income=500000,
                withholding_tax=100000,
                social_security_payments=300000,
                pension_contributions=200000,
                mortgage_payments=100000,
                donations=50000,
                education_expenses=60000
            )



if __name__ == "__main__":
    unittest.main()