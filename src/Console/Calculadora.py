def CalcularCouta(labor_income: int, other_income: int, withholding_tax: int, social_security_payments: int, pension_contributions: int, mortgage_payments: int, donations: int, education_expenses: int):

    # Check for negative values
    if labor_income < 0 or other_income < 0 or withholding_tax < 0 or social_security_payments < 0 or pension_contributions < 0 or mortgage_payments < 0 or donations < 0 or education_expenses < 0:
        raise Exception("Los valores no pueden ser negativos.")

    # Validate that labor income is positive
    if labor_income <= 0:
        raise Exception("Los ingresos laborales deben ser mayores que cero.")

    # Ensure social security payments do not exceed labor income
    if social_security_payments > labor_income:
        raise Exception("Los pagos de seguridad social no pueden exceder los ingresos laborales.")

     # Ensure pension contributions do not exceed labor income
    if pension_contributions > labor_income:
        raise Exception("Los aportes a pensión no pueden exceder los ingresos laborales.")

    # Ensure mortgage payments do not exceed labor income
    if mortgage_payments > labor_income:
        raise Exception("Los pagos por créditos hipotecarios no pueden exceder los ingresos laborales.")

    # Ensure donations do not exceed labor income
    if donations > labor_income:
        raise Exception("Las donaciones no pueden exceder los ingresos laborales.")

    # Ensure education expenses do not exceed labor income
    if education_expenses > labor_income:
        raise Exception("Los gastos de educación no pueden exceder los ingresos laborales.")

    # Ensure education expenses do not exceed the sum of labor and other income
    if education_expenses > labor_income + other_income:
        raise Exception("Los gastos de educación no pueden exceder la suma de ingresos laborales y otros ingresos.")

    # Ensure withholding tax is not negative
    if withholding_tax < 0:
        raise Exception("Las retenciones de fuente no pueden ser negativas.")

     # Ensure social security payments are not zero
    if social_security_payments == 0:
        raise Exception("Los pagos de seguridad social no pueden ser cero.")

    # Validate that income is sufficient to cover expenses and deductions
    if labor_income < education_expenses + other_income + withholding_tax + social_security_payments + pension_contributions + mortgage_payments + donations:
        raise Exception("Los ingresos no son suficientes para cubrir los gastos y deducciones.")
    
    # Validates if the total tax amount is negative
    if ((((labor_income + other_income)-(social_security_payments + pension_contributions + mortgage_payments + donations + education_expenses))*0.19) - withholding_tax) < 0:
        raise Exception("Los impuestos son negativos, vuelva a intentar")
    
    else: 
        # Calculates the total tax amount
        return ((((labor_income + other_income)-(social_security_payments + pension_contributions + mortgage_payments + donations + education_expenses))*0.19) - withholding_tax)
  
    
