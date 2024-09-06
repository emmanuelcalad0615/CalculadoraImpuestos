class NegativeValuesError(Exception):
    """Raised when a negative value is encountered."""
    pass

class LaborIncomeLessThanZero(Exception):
    """Raised when labor income is less than zero."""
    pass

class SocialSecurityPaymentsGreaterThanIncome(Exception):
    """Raised when social security payments exceed income."""
    pass

class PensionContributionsGreaterThanIncome(Exception):
    """Raised when pension contributions exceed income."""
    pass

class MortgagePaymentsGreaterThanIncome(Exception):
    """Raised when mortgage payments exceed income."""
    pass

class DonationsGreaterThanIncome(Exception):
    """Raised when donations exceed income."""
    pass

class EducationExpensesGreaterThanTotalIncome(Exception):
    """Raised when education expenses exceed all income."""
    pass

class NegativeWithholdingTax(Exception):
    """Raised when withholding tax is negative."""
    pass

class ZeroSocialSecurityPayments(Exception):
    """Raised when social security payments are zero."""
    pass

class InsufficientIncome(Exception):
    """Raised when income is insufficient."""
    pass

class NegativeTaxes(Exception):
    """Raised when the calculated taxes are negative."""
    pass
