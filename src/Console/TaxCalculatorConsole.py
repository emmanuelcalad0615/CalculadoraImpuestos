import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, NaturalPerson, IncomeDeclaration, CalculoException
def mostrar_menu():
    print("\n--- Menú de Declaración de Impuestos ---")
    print("1. Ingresar datos del contribuyente")
    print("2. Calcular impuestos")
    print("3. Salir")

def main():
    contribuyente = None

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                # Ingresar datos del contribuyente
                nombre = input("Ingrese el nombre: ")
                id = int(input("Ingrese el ID: "))
                ocupacion = input("Ingrese la ocupación: ")
                rut = int(input("Ingrese el RUT: "))
                
                laboral_income = int(input("Ingrese los ingresos laborales: "))
                other_income = int(input("Ingrese otros ingresos: "))
                withholding_source = int(input("Ingrese la retención de fuente: "))
                social_security_payments = int(input("Ingrese los pagos de seguridad social: "))
                pension_contributions = int(input("Ingrese los aportes a pensión: "))
                mortgage_payments = int(input("Ingrese los pagos por crédito hipotecario: "))
                donations = int(input("Ingrese las donaciones: "))
                educational_expenses = int(input("Ingrese los gastos de educación: "))
                
                personal_info = PersonalInfo(nombre, id, ocupacion, rut)
                
                contribuyente = NaturalPerson(
                    laboral_income, other_income, withholding_source,
                    social_security_payments, pension_contributions,
                    mortgage_payments, donations, educational_expenses,
                    personal_info
                )
                print("Datos del contribuyente ingresados con éxito.")

            except ValueError:
                print("Error: Por favor, ingrese valores numéricos válidos.")
            except CalculoException as e:
                print(f"Error de cálculo: {e}")

        elif opcion == '2':
            if contribuyente:
                try:
                    declaracion = IncomeDeclaration(person=contribuyente)

                    # Cálculo del impuesto
                    total_ingresos_gravados = declaracion.calcular_total_ingresos_gravados()
                    total_ingresos_no_gravados = declaracion.calcular_total_ingresos_no_gravados()
                    total_costos_deducibles = declaracion.calcular_total_costos_deducibles()
                    valor_impuesto = declaracion.calcular_valor_impuesto()

                    # Imprimir resultados
                    print(f"Total Ingresos Gravados: {total_ingresos_gravados}")
                    print(f"Total Ingresos No Gravados: {total_ingresos_no_gravados}")
                    print(f"Total Costos Deducibles: {total_costos_deducibles}")
                    print(f"Valor Impuesto: {valor_impuesto}")

                except CalculoException as e:
                    print(f"Error de cálculo: {e}")
            else:
                print("Error: No se han ingresado datos del contribuyente.")

        elif opcion == '3':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()
