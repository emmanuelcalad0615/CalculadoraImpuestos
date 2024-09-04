import Calculadora as Calculadora

# User inputs for income and deductions

labor_income = int(input("Ingrese sus ingresos laborales: "))
other_income = int(input("Ingrese sus ingresos adicionales (si tiene): "))
withholding_tax = int(input("Ingrese sus retenciones de fuente: "))
social_security_payments = int(input("Ingrese sus pagos a Seguridad Social: "))
pension_contributions = int(input("Ingrese sus aportes a pensión: "))
mortgage_payments = int(input("Ingrese sus pagos hipotecarios: "))
donations = int(input("Ingrese sus donaciones (si tiene): "))
education_expenses = int(input("Ingrese sus gastos educativos: "))


try:
     # Calculate the tax amount using the provided calculator

    result =  Calculadora.CalcularCouta(labor_income, other_income, withholding_tax, social_security_payments, pension_contributions, mortgage_payments, donations, education_expenses)
    print(f"El Valor a pagar es: {result}")

except Exception as el_error:
    print("Hubo un error")
    print(str(el_error))


