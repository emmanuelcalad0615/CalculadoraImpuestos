import CalculadoraConsole

ingresos_laborales = int(input("Ingrese sus ingresos laborales: "))
otros_ingresos = int(input("Ingrese sus ingresos adicionales (si tiene): "))
retenciones_fuente = int(input("Ingrese sus retenciones de fuente: "))
pagos_seguridad_social = int(input("Ingrese sus pagos a Seguridad Social: "))
aportes_pension = int(input("Ingrese sus aportes a pensión: "))
pagos_creditos_hipotecarios = int(input("Ingrese sus pagos hipotecarios: "))
donaciones = int(input("Ingrese sus donaciones (si tiene): "))
gastos_educacion = int(input("Ingrese sus gastos educativos: "))


try:
    resultado =  CalculadoraConsole.CalcularCouta(ingresos_laborales, otros_ingresos, retenciones_fuente, pagos_seguridad_social, aportes_pension, pagos_creditos_hipotecarios, donaciones, gastos_educacion)
    print(f"El Valor a pagar es: {resultado}")

except Exception as el_error:
    print("Hubo un error")
    print(str(el_error))