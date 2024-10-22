# Custom exception hierarchy for handling different error scenarios in income calculation
class CalculoException(Exception):
    pass

# Specific exceptions for various tax calculation errors
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


# Class to store personal information related to the taxpayer
class PersonalInfo:
    def __init__(self, nombre: str, id: int, ocupacion: str, rut: int) -> None:
        """
        Initializes the personal information of a taxpayer.

        :param nombre: Full name of the taxpayer.
        :param id: ID number of the taxpayer.
        :param ocupacion: Occupation of the taxpayer.
        :param rut: Chilean RUT (Unique Taxpayer Roll) number of the taxpayer.
        """
        self.nombre: str = nombre
        self.id: int = id
        self.ocupacion: str = ocupacion
        self.rut: int = rut


# Class to represent an individual taxpayer and their financial details
class NaturalPerson:
    def __init__(self, laboral_income: int, other_income: int, withholding_source: int, social_security_payments: int, 
                 pension_contributions: int, mortgage_payments: int, donations: int, educational_expenses: int, 
                 personal_info: PersonalInfo = None) -> None:
        """
        Initializes a natural person (taxpayer) object, checking all financial values and conditions.

        :param laboral_income: The taxpayer's labor income (e.g., salary).
        :param other_income: Other income apart from labor income.
        :param withholding_source: Amount of tax withheld at the source.
        :param social_security_payments: Amount paid for social security.
        :param pension_contributions: Amount paid for pension contributions.
        :param mortgage_payments: Mortgage payment amount.
        :param donations: Amount donated for charitable causes.
        :param educational_expenses: Expenses for educational purposes.
        :param personal_info: An object containing personal details about the taxpayer (optional).
        """
        # Check for negative values for any financial information (invalid input)
        if laboral_income < 0 or other_income < 0 or withholding_source < 0 or social_security_payments < 0 or \
           pension_contributions < 0 or mortgage_payments < 0 or donations < 0 or educational_expenses < 0:
            raise NegativeValues("Values cannot be negative.")
        
        # Validate that labor income is positive (non-zero)
        if laboral_income <= 0:
            raise LaboralIncomeZero("Labor income must be greater than zero.")
        
        # Ensure social security payments are not zero (must be greater than zero)
        if social_security_payments == 0:
            raise SocialSecurityPaymentsZero("Social security payments cannot be zero.")
        
        # Validate that social security payments do not exceed labor income
        if social_security_payments > laboral_income:
            raise SocialSecurityPaymentsExceedIncome("Social security payments cannot exceed labor income.")
        
        # Ensure pension contributions do not exceed labor income
        if pension_contributions > laboral_income:
            raise PensionContributionsExceedIncome("Pension contributions cannot exceed labor income.")
        
        # Validate that mortgage payments do not exceed labor income
        if mortgage_payments > laboral_income:
            raise MortgagePaymentsExceedIncome("Mortgage payments cannot exceed labor income.")
        
        # Ensure donations do not exceed labor income
        if donations > laboral_income:
            raise DonationsExceedIncome("Donations cannot exceed labor income.")
        
        # Validate that educational expenses do not exceed the sum of labor and other income
        if educational_expenses > laboral_income + other_income:
            raise EducationalExpensesExceedIncome("Educational expenses cannot exceed the sum of labor and other income.")
        
        # Ensure withholding tax is not negative
        if withholding_source < 0:
            raise WithholdingSourceNegative("Withholding tax cannot be negative.")
        
        # Check if the income is sufficient to cover all deductible costs
        if laboral_income < educational_expenses + social_security_payments + pension_contributions + mortgage_payments + donations:
            raise InsufficientIncomeForDeductions("Income is insufficient to cover expenses and deductions.")
        
        # Assign the financial data and personal information to the object's attributes
        self.laboral_income: int = laboral_income
        self.other_income: int = other_income
        self.withholding_source: int = withholding_source
        self.social_security_payments: int = social_security_payments
        self.pension_contributions: int = pension_contributions
        self.mortgage_payments: int = mortgage_payments
        self.donations: int = donations
        self.educational_expenses: int = educational_expenses
        self.personal_info: PersonalInfo = personal_info


# Class to handle income tax declaration and calculations
class IncomeDeclaration:
    def __init__(self, person: NaturalPerson) -> None:
        """
        Initializes the IncomeDeclaration class for a specific natural person (taxpayer).

        :param person: An object of type NaturalPerson representing the taxpayer.
        """
        self.person: NaturalPerson = person

    def calcular_total_ingresos_gravados(self):
        """
        Calculates the total taxable income (labor income + other income).
        Returns the sum of all taxable income.
        """
        return self.person.laboral_income + self.person.other_income

    def calcular_total_ingresos_no_gravados(self):
        """
        Calculates the total non-taxable income (deductions).
        This includes social security payments, pension contributions,
        mortgage payments, donations, and educational expenses.
        """
        return (self.person.social_security_payments + self.person.pension_contributions + 
                self.person.mortgage_payments + self.person.donations + self.person.educational_expenses)

    def calcular_total_costos_deducibles(self):
        """
        Calculates the total deductible costs, which are the same as non-taxable income.
        This will include all deductions as per the tax regulations.
        """
        return self.calcular_total_ingresos_no_gravados()

    def calcular_valor_impuesto(self):
        """
        Calculates the total amount of tax owed.
        If the total taxable income is below 51 million, the user is not required to declare taxes.
        If the taxable base is negative, an error is raised.
        Returns the calculated tax amount minus the withholding tax.
        """
        # Calculate total taxable income
        total_taxable_income = self.calcular_total_ingresos_gravados()
        
        # Check if the total income is below the limit for tax declaration
        if total_taxable_income < 51000000:
            raise BelowLimits("Your income does not exceed 51,000,000. No need to declare taxes.")
        
        # Calculate the deductible costs
        total_deductible_costs = self.calcular_total_costos_deducibles()
        
        # Calculate the taxable base by subtracting deductions from taxable income
        taxable_base = total_taxable_income - total_deductible_costs
        
        # Calculate the tax owed at a 35% tax rate
        tax_amount = taxable_base * 0.35  # Assuming a 35% tax rate
        
        # Raise an error if the tax amount is negative
        if tax_amount < 0:
            raise NegativeTaxes("Tax amount cannot be negative.")
        
        # Return the final tax amount after subtracting the withholding tax
        return tax_amount - self.person.withholding_source

