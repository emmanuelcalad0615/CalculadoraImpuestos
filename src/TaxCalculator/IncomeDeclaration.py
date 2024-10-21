class CalculoException(Exception):
    pass

class NegativeTaxes(CalculoException):
    pass

class BelowLimits(CalculoException):
    pass

class NegativeValues(CalculoException):
    pass

class LaboralIncomeZero(CalculoException):
    pass

class SocialSecurityPaymentsZero(CalculoException):
    pass

class SocialSecurityPaymentsExceedIncome(CalculoException):
    pass

class PensionContributionsExceedIncome(CalculoException):
    pass

class MortgagePaymentsExceedIncome(CalculoException):
    pass

class DonationsExceedIncome(CalculoException):
    pass

class EducationalExpensesExceedIncome(CalculoException):
    pass

class WithholdingSourceNegative(CalculoException):
    pass

class InsufficientIncomeForDeductions(CalculoException):
    pass


class PersonalInfo:
    def __init__(self, nombre: str, id: int, ocupacion: str, rut: int) -> None:
        self.nombre: str = nombre
        self.id: int = id
        self.ocupacion: str = ocupacion
        self.rut: int = rut


class Person:
    def __init__(self, laboral_income: int, other_income: int, withholding_source: int, social_security_payments: int, 
                 pension_contributions: int, mortgage_payments: int, donations: int, educational_expenses: int, 
                 personal_info: PersonalInfo) -> None:
        
        # Check for negative values
        if laboral_income < 0 or other_income < 0 or withholding_source < 0 or social_security_payments < 0 or \
           pension_contributions < 0 or mortgage_payments < 0 or donations < 0 or educational_expenses < 0:
            raise NegativeValues("Los valores no pueden ser negativos.")

        # Validate that labor income is positive
        if laboral_income <= 0:
            raise LaboralIncomeZero("Los ingresos laborales deben ser mayores que cero.")

        # Ensure social security payments are not zero
        if social_security_payments == 0:
            raise SocialSecurityPaymentsZero("Los pagos de seguridad social no pueden ser cero.")
        
        # Check that social security payments do not exceed labor income
        if social_security_payments > laboral_income:
            raise SocialSecurityPaymentsExceedIncome("Los pagos de seguridad social no pueden exceder los ingresos laborales.")

        # Check that pension contributions do not exceed labor income
        if pension_contributions > laboral_income:
            raise PensionContributionsExceedIncome("Los aportes a pensión no pueden exceder los ingresos laborales.")

        # Check that mortgage payments do not exceed labor income
        if mortgage_payments > laboral_income:
            raise MortgagePaymentsExceedIncome("Los pagos por créditos hipotecarios no pueden exceder los ingresos laborales.")

        # Check that donations do not exceed labor income
        if donations > laboral_income:
            raise DonationsExceedIncome("Las donaciones no pueden exceder los ingresos laborales.")

        # Check that education expenses do not exceed the sum of labor and other income
        if educational_expenses > laboral_income + other_income:
            raise EducationalExpensesExceedIncome("Los gastos de educación no pueden exceder la suma de ingresos laborales y otros ingresos.")

        # Ensure withholding tax is not negative
        if withholding_source < 0:
            raise WithholdingSourceNegative("Las retenciones de fuente no pueden ser negativas.")

        # Validate that income is sufficient to cover expenses and deductions
        if laboral_income < educational_expenses + social_security_payments + pension_contributions + mortgage_payments + donations:
            raise InsufficientIncomeForDeductions("Los ingresos no son suficientes para cubrir los gastos y deducciones.")

        # Assign values to the attributes
        self.laboral_income: int = laboral_income
        self.other_income: int = other_income
        self.withholding_source: int = withholding_source
        self.social_security_payments: int = social_security_payments
        self.pension_contributions: int = pension_contributions
        self.mortgage_payments: int = mortgage_payments
        self.donations: int = donations
        self.educational_expenses: int = educational_expenses
        self.personal_info: PersonalInfo = personal_info


class IncomeDeclaration:
    def __init__(self, person: Person) -> None:
        self.person: Person = person

    def calcular_total_ingresos_gravados(self):
        """
        Calculates the total taxable income.
        """
        return self.person.laboral_income + self.person.other_income

    def calcular_total_ingresos_no_gravados(self):
        """
        Calculates the total non-taxable income (deductions).
        """
        return (self.person.social_security_payments + self.person.pension_contributions + 
                self.person.mortgage_payments + self.person.donations + self.person.educational_expenses)

    def calcular_total_costos_deducibles(self):
        """
        Calculates the total deductible costs.
        """
        return self.calcular_total_ingresos_no_gravados()

    def calcular_valor_impuesto(self):
        """
        Calculates the amount of tax owed.
        """
        total_taxable_income = self.calcular_total_ingresos_gravados()
        if total_taxable_income < 51000000:
            raise BelowLimits("Sus ingresos no superan los 51,000,000, no debe declarar renta")
        
        total_deductible_costs = self.calcular_total_costos_deducibles()
        taxable_base = total_taxable_income - total_deductible_costs
        tax_amount = taxable_base * 0.35  # Assuming a 35% tax rate
        
        if tax_amount < 0:
            raise NegativeTaxes("El valor del impuesto no puede ser negativo.")
        
        return tax_amount - self.person.withholding_source