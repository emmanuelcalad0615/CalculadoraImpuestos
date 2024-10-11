class CalculoException(Exception):
    def _init_(self, mensaje):
        super()._init_(mensaje)
class NegativeTaxes:
    pass

class Person:
    def __init__(self, laboral_income: int, other_income: int, withholding_source: int, social_security_payments: int, pension_contributions: int, mortgage_payments: int, donations: int, educational_expenses:int ) -> None:
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
        total_deductible_costs = self.calcular_total_costos_deducibles()
        taxable_base = total_taxable_income - total_deductible_costs
        tax_amount = taxable_base * 0.19   # Assuming a 19% tax rate
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
