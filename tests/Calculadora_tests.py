from Exceptions import (
    

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

class CalculadoraDeImpuestos:
    def __init__(self, labor_income, other_income, withholding_tax, social_security_payments, pension_contributions, mortgage_payments, donations, education_expenses):
        
        # Check for negative values
        if labor_income < 0 or other_income < 0 or withholding_tax < 0 or social_security_payments < 0 or pension_contributions < 0 or mortgage_payments < 0 or donations < 0 or education_expenses < 0:
            raise Exception("Los valores no pueden ser negativos.")

        # Validate that labor income is positive
        if labor_income <= 0:
            raise Exception("Los ingresos laborales deben ser mayores que cero.")

        # Ensure social security payments are not zero
        if social_security_payments == 0:
            raise Exception("Los pagos de seguridad social no pueden ser cero.")
        
         # Check that social security payments do not exceed labor income
        if social_security_payments > labor_income:
            raise Exception("Los pagos de seguridad social no pueden exceder los ingresos laborales.")

        # Check that pension contributions do not exceed labor income
        if pension_contributions > labor_income:
            raise Exception("Los aportes a pensión no pueden exceder los ingresos laborales.")

        # Check that mortgage payments do not exceed labor income
        if mortgage_payments > labor_income:
            raise Exception("Los pagos por créditos hipotecarios no pueden exceder los ingresos laborales.")

        # Check that donations do not exceed labor income
        if donations > labor_income:
            raise Exception("Las donaciones no pueden exceder los ingresos laborales.")

        # Check that education expenses do not exceed the sum of labor and other income
        if education_expenses > labor_income + other_income:
            raise Exception("Los gastos de educación no pueden exceder la suma de ingresos laborales y otros ingresos.")

         # Ensure withholding tax is not negative
        if withholding_tax < 0:
            raise Exception("Las retenciones de fuente no pueden ser negativas.")

        # Validate that income is sufficient to cover expenses and deductions
        if labor_income < education_expenses + social_security_payments + pension_contributions + mortgage_payments + donations:
            raise Exception("Los ingresos no son suficientes para cubrir los gastos y deducciones.")


        self.labor_income = labor_income
        self.other_income = other_income
        self.withholding_tax = withholding_tax
        self.social_security_payments = social_security_payments
        self.pension_contributions = pension_contributions
        self.mortgage_payments = mortgage_payments
        self.donations = donations
        self.education_expenses = education_expenses

    def calcular_total_ingresos_gravados(self):

        """
        Calculates the total taxable income.
        
        Returns:
        - Total taxable income (labor income + other income)
        """

        return self.labor_income + self.other_income

    def calcular_total_ingresos_no_gravados(self):

        """
        Calculates the total non-taxable income (deductions).
        
        Returns:
        - Total non-taxable income (social security payments + pension contributions + mortgage payments + donations + education expenses)
        """

        return self.social_security_payments + self.pension_contributions + self.mortgage_payments + self.donations + self.education_expenses

    def calcular_total_costos_deducibles(self):

        """
        Calculates the total deductible costs.
        
        Returns:
        - Total deductible costs (same as total non-taxable income)
        """

        return self.calcular_total_ingresos_no_gravados()

    def calcular_valor_impuesto(self):

        """
        Calculates the amount of tax owed.
        
        Returns:
        - The amount of tax owed after applying deductions and withholding tax.
        """

        total_taxable_income = self.calcular_total_ingresos_gravados()
        total_deductible_costs = self.calcular_total_costos_deducibles()
        taxable_base = total_taxable_income - total_deductible_costs
        tax_amount = taxable_base * 0.19   # Assuming a 19% tax rate
        if tax_amount < 0:
            raise NegativeTaxes("El valor del impuesto no puede ser negativo.")
        return tax_amount - self.withholding_tax
    


# Example usage
calculator = CalculadoraDeImpuestos(

    labor_income=50000000,
    other_income=10000000,
    withholding_tax=5000000,
    social_security_payments=4000000,
    pension_contributions=3000000,
    mortgage_payments=2000000,
    donations=1000000,
    education_expenses=500000
)

print(f"Valor a pagar por impuesto de renta: {calculator.calcular_valor_impuesto()}")

