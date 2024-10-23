import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import PersonalInfo, NaturalPerson, IncomeDeclaration, CalculoException
from Controller.IncomeDeclarationController import IncomeDeclarationController
from Controller.PersonalInfoController import PersonalInfoController
from Controller.NaturalPersonController import NaturalPersonController


def mostrar_menu():
    print("\n--- Menú de Declaración de Impuestos ---")
    print("1. Ingresar datos del contribuyente")
    print("2. Calcular impuestos")
    print("3. Guardar en base de datos")
    print("4. Actualizar en base de datos")
    print("5. Eliminar en base de datos")
    print("6. Salir")

def main():
    natural_person = None
    personal_info = None
    declaracion = None
    PersonalInfoController.create_table()
    NaturalPersonController.create_table()
    IncomeDeclarationController.create_table()

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
                
                natural_person = NaturalPerson(
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
            if natural_person:
                try:
                    declaracion = IncomeDeclaration(person=natural_person)

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
            if natural_person and personal_info and declaracion:
                try:

                    # Guardar información personal
                    PersonalInfoController.insert_personal_info(personal_info)
                    # Guardar persona natural
                    NaturalPersonController.insert_natural_person(natural_person, personal_info.id, personal_info.rut)
                    # Guardar declaración de ingresos
                    IncomeDeclarationController.insert_income_declaration(declaracion, natural_person.personal_info.rut)

                    print("Datos guardados en la base de datos con éxito.")

                except Exception as e:
                    print(f"Error al guardar en la base de datos: {e}")
            else:
                print("Error: Debe ingresar datos del contribuyente y calcular la hipoteca antes de guardar.")
        elif opcion == '4':
            if natural_person and declaracion:
                try:
                    cedula = (personal_info.id)
                    rut = natural_person.personal_info.rut
                    print(f"Ingresando nuevos datos para el contribuyente con RUT: {rut}")
                    
                    # Actualizar datos de PersonalInfo
                    nuevo_nombre = input("Ingrese el nuevo nombre (dejar vacío para no cambiar): ")
                    nuevo_ocupacion = input("Ingrese la nueva ocupación (dejar vacío para no cambiar): ")

                    PersonalInfoController.update_personal_info(
                        cedula=cedula,
                        nombre=nuevo_nombre if nuevo_nombre else None,
                        ocupacion=nuevo_ocupacion if nuevo_ocupacion else None
                    )
                    try:
                        # Actualizar también los datos de NaturalPerson
                        nuevo_ingreso_laboral = input("Ingrese los nuevos ingresos laborales (dejar vacío para no cambiar): ")
                        nuevo_ingreso_laboral = int(nuevo_ingreso_laboral) if nuevo_ingreso_laboral else None

                        nuevo_otros_ingresos = input("Ingrese los nuevos otros ingresos (dejar vacío para no cambiar): ")
                        nuevo_otros_ingresos = int(nuevo_otros_ingresos) if nuevo_otros_ingresos else None

                        nueva_retencion = input("Ingrese la nueva retención de fuente (dejar vacío para no cambiar): ")
                        nueva_retencion = int(nueva_retencion) if nueva_retencion else None

                        nuevos_pagos_seguridad = input("Ingrese los nuevos pagos de seguridad social (dejar vacío para no cambiar): ")
                        nuevos_pagos_seguridad = int(nuevos_pagos_seguridad) if nuevos_pagos_seguridad else None

                        nuevos_aportes_pension = input("Ingrese los nuevos aportes a pensión (dejar vacío para no cambiar): ")
                        nuevos_aportes_pension = int(nuevos_aportes_pension) if nuevos_aportes_pension else None

                        nuevos_pagos_hipotecarios = input("Ingrese los nuevos pagos por crédito hipotecario (dejar vacío para no cambiar): ")
                        nuevos_pagos_hipotecarios = int(nuevos_pagos_hipotecarios) if nuevos_pagos_hipotecarios else None

                        nuevas_donaciones = input("Ingrese las nuevas donaciones (dejar vacío para no cambiar): ")
                        nuevas_donaciones = int(nuevas_donaciones) if nuevas_donaciones else None

                        nuevos_gastos_educacion = input("Ingrese los nuevos gastos de educación (dejar vacío para no cambiar): ")
                        nuevos_gastos_educacion = int(nuevos_gastos_educacion) if nuevos_gastos_educacion else None

                    # Actualiza los datos de NaturalPerson utilizando el controlador
                        
                        NaturalPersonController.update_natural_person(
                            rut=rut,
                            laboral_income=nuevo_ingreso_laboral,
                            other_income=nuevo_otros_ingresos,
                            withholding_source=nueva_retencion,
                            social_security_payments=nuevos_pagos_seguridad,
                            pension_contributions=nuevos_aportes_pension,
                            mortgage_payments=nuevos_pagos_hipotecarios,
                            donations=nuevas_donaciones,
                            educational_expenses=nuevos_gastos_educacion
                        )
                    except Exception as e:
                        print(f"Error: {e}")
                        return        

                    # Recalcular la declaración de impuestos
                    declaracion = IncomeDeclaration(person=natural_person)
                    total_ingresos_gravados = declaracion.calcular_total_ingresos_gravados()
                    total_ingresos_no_gravados = declaracion.calcular_total_ingresos_no_gravados()
                    total_costos_deducibles = declaracion.calcular_total_costos_deducibles()
                    valor_impuesto = declaracion.calcular_valor_impuesto()

                    IncomeDeclarationController.update_income_declaration(personal_info.rut, total_ingresos_gravados, total_ingresos_no_gravados,total_costos_deducibles, valor_impuesto)

                    # Imprimir resultados
                    print(f"Total Ingresos Gravados: {total_ingresos_gravados}")
                    print(f"Total Ingresos No Gravados: {total_ingresos_no_gravados}")
                    print(f"Total Costos Deducibles: {total_costos_deducibles}")
                    print(f"Valor Impuesto: {valor_impuesto}")

                    print("Datos actualizados correctamente.")

                except Exception as e:
                    print(f"Error actualizando datos: {e}")
            else:
                print("Error: No se han ingresado datos del contribuyente, ni se ha calculado la declaracion.")
        elif opcion == '5':
            try: 
                id = int(input("Ingrese su cédula: "))
                PersonalInfoController.delete_personal_info(id) 
            except Exception as e:
                print(f"Error al eliminar{e}")     
                      
        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()
