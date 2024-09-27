import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Logi.Calculadora as Calculadora

def obtener_entradas():
    """Función para obtener las entradas del usuario y devolverlas como un diccionario."""
    try:
        entradas = {
            'labor_income': int(input("Ingrese sus ingresos laborales: ")),
            'other_income': int(input("Ingrese sus ingresos adicionales (si tiene): ")),
            'withholding_tax': int(input("Ingrese sus retenciones de fuente: ")),
            'social_security_payments': int(input("Ingrese sus pagos a Seguridad Social: ")),
            'pension_contributions': int(input("Ingrese sus aportes a pensión: ")),
            'mortgage_payments': int(input("Ingrese sus pagos hipotecarios: ")),
            'donations': int(input("Ingrese sus donaciones (si tiene): ")),
            'education_expenses': int(input("Ingrese sus gastos educativos: "))
        }
        return entradas
    except ValueError as e:
        print("Valor ingresado incorrecto, por favor ingrese números enteros.")
        print(str(e))
        return None

def calcular_impuesto(entradas):
    """Función para calcular el impuesto usando las entradas proporcionadas."""
    return Calculadora.CalcularCouta(
        entradas['labor_income'],
        entradas['other_income'],
        entradas['withholding_tax'],
        entradas['social_security_payments'],
        entradas['pension_contributions'],
        entradas['mortgage_payments'],
        entradas['donations'],
        entradas['education_expenses']
    )

def main():
    entradas = obtener_entradas()
    if entradas:
        result = calcular_impuesto(entradas)
        print(f"El Valor a pagar es: {result}")

if __name__ == "__main__":
    main()

    

