class CalculoException(Exception):
    def _init_(self, mensaje):
        super()._init_(mensaje)
class NegativeTaxes(Exception):
    pass
class BelowLimits(Exception):
    pass

class Person:
    def __init__(self, laboral_income: int, other_income: int, withholding_source: int, social_security_payments: int, pension_contributions: int, mortgage_payments: int, donations: int, educational_expenses:int ) -> None:
        # Check for negative values
        if laboral_income < 0 or other_income < 0 or withholding_source < 0 or social_security_payments < 0 or pension_contributions < 0 or mortgage_payments < 0 or donations < 0 or educational_expenses < 0:
            raise Exception("Los valores no pueden ser negativos.")

        # Validate that labor income is positive
        if laboral_income <= 0:
            raise Exception("Los ingresos laborales deben ser mayores que cero.")

        # Ensure social security payments are not zero
        if social_security_payments == 0:
            raise Exception("Los pagos de seguridad social no pueden ser cero.")
        
         # Check that social security payments do not exceed labor income
        if social_security_payments > laboral_income:
            raise Exception("Los pagos de seguridad social no pueden exceder los ingresos laborales.")

        # Check that pension contributions do not exceed labor income
        if pension_contributions > laboral_income:
            raise Exception("Los aportes a pensión no pueden exceder los ingresos laborales.")

        # Check that mortgage payments do not exceed labor income
        if mortgage_payments > laboral_income:
            raise Exception("Los pagos por créditos hipotecarios no pueden exceder los ingresos laborales.")

        # Check that donations do not exceed labor income
        if donations > laboral_income:
            raise Exception("Las donaciones no pueden exceder los ingresos laborales.")

        # Check that education expenses do not exceed the sum of labor and other income
        if educational_expenses > laboral_income + other_income:
            raise Exception("Los gastos de educación no pueden exceder la suma de ingresos laborales y otros ingresos.")

         # Ensure withholding tax is not negative
        if withholding_source < 0:
            raise Exception("Las retenciones de fuente no pueden ser negativas.")

        # Validate that income is sufficient to cover expenses and deductions
        if laboral_income < educational_expenses + social_security_payments + pension_contributions + mortgage_payments + donations:
            raise Exception("Los ingresos no son suficientes para cubrir los gastos y deducciones.")
        self.laboral_income: int = laboral_income
        self.other_income: int = other_income
        self.withholding_source: int = withholding_source
        self.social_security_payments: int = social_security_payments
        self.pension_contributions: int = pension_contributions
        self.mortgage_payments: int = mortgage_payments
        self.donations: int = donations
        self.educational_expenses: int = educational_expenses


class IncomeDeclaration:
    def __init__(self, person: Person) -> None:
        self.person: Person = person

    def calcular_total_ingresos_gravados(self):

        """
        Calculates the total taxable income.
        
        Returns:
        - Total taxable income (labor income + other income)
        """

        return self.person.laboral_income  + self.person.other_income

    def calcular_total_ingresos_no_gravados(self):

        """
        Calculates the total non-taxable income (deductions).
        
        Returns:
        - Total non-taxable income (social security payments + pension contributions + mortgage payments + donations + education expenses)
        """

        return self.person.social_security_payments + self.person.pension_contributions + self.person.mortgage_payments + self.person.donations + self.person.educational_expenses

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
        if total_taxable_income < 51000000:
            raise BelowLimits("Sus ingresos no superan los 51000000, no debe declar renta")
        total_deductible_costs = self.calcular_total_costos_deducibles()
        taxable_base = total_taxable_income - total_deductible_costs
        tax_amount = taxable_base * 0.35   # Assuming a 35% tax rate
        if tax_amount < 0:
            raise NegativeTaxes("El valor del impuesto no puede ser negativo.")
        return tax_amount - self.person.withholding_source 
          
person = Person(
    laboral_income=50000000,
    other_income=10000000,
    withholding_source=5000000,
    social_security_payments=4000000,
    pension_contributions=3000000,
    mortgage_payments=2000000,
    donations=1000000,
    educational_expenses=500000
)

declaration = IncomeDeclaration(person)
tax_value = declaration.calcular_valor_impuesto()

print(f"Impuesto a pagar: {tax_value}")          
