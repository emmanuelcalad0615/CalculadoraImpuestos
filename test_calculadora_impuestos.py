import unittest
from calculadora_impuestos import CalculadoraDeImpuestos

class TestCalculadoraDeImpuestos(unittest.TestCase):

    def setUp(self):
        calculadora = CalculadoraDeImpuestos(
            ingresos_laborales=50000000,
            otros_ingresos=10000000,
            retenciones_fuente=5000000,
            pagos_seguridad_social=4000000,
            aportes_pension=3000000,
            pagos_creditos_hipotecarios=2000000,
            donaciones=1000000,
            gastos_educacion=500000
        )
        valor_esperado = 4405000.0 
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoNormal1(self):
        # Ingreso mensual medio con algunos ingresos adicionales
        calculadora = CalculadoraDeImpuestos(
            ingresos_laborales = 14000000,
            otros_ingresos = 2000000,
            retenciones_fuente = 1000000,
            pagos_seguridad_social = 800000,
            aportes_pension = 500000,
            pagos_creditos_hipotecarios = 300000,
            donaciones = 150000,
            gastos_educacion = 200000

    )
        valor_esperado = 1669500.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoNormal2(self):
         #Ingreso para un trabajador con ingresos adicionales
        calculadora = CalculadoraDeImpuestos(
            ingresos_laborales = 20000000,  # Aproximadamente 17 salarios mínimos
            otros_ingresos = 3000000,
            retenciones_fuente = 1500000,
            pagos_seguridad_social = 1200000,
            aportes_pension = 800000,
            pagos_creditos_hipotecarios = 500000,
            donaciones = 200000,
            gastos_educacion = 300000
        )
        valor_esperado = 2300000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoNormal3(self):
        #Ingreso para un trabajador con salario alto
        calculadora = CalculadoraDeImpuestos(
            ingresos_laborales = 25000000,  # Aproximadamente 22 salarios mínimos
            otros_ingresos = 2500000,
            retenciones_fuente = 2000000,
            pagos_seguridad_social = 1500000,
            aportes_pension = 1000000,
            pagos_creditos_hipotecarios = 800000,
            donaciones = 300000,
            gastos_educacion = 400000
        )
        valor_esperado = 2465000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoNormal4(self):
       #Ingreso para una persona con salario medio y algunos ingresos extras
        calculadora = CalculadoraDeImpuestos(
            ingresos_laborales = 16000000,  # Aproximadamente 14 salarios mínimos
            otros_ingresos = 2500000,
            retenciones_fuente = 1200000,
            pagos_seguridad_social = 1000000,
            aportes_pension = 600000,
            pagos_creditos_hipotecarios = 400000,
            donaciones = 200000,
            gastos_educacion = 250000

        )
        valor_esperado = 1849500.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoNormal5(self):
        
           # Ingreso bajo con gastos de educación moderados
        calculadora = CalculadoraDeImpuestos(
            ingresos_laborales = 12000000,  # Aproximadamente 10 salarios mínimos
            otros_ingresos = 1500000,
            retenciones_fuente = 800000,
            pagos_seguridad_social = 600000,
            aportes_pension = 400000,
            pagos_creditos_hipotecarios = 300000,
            donaciones = 100000,
            gastos_educacion = 150000
        )
        valor_esperado = 1470500.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)
        

    def testCasoNormal6(self):
        
            #Ingreso promedio con gastos diversos
        calculadora = CalculadoraDeImpuestos(
            ingresos_laborales = 20000000,  # Aproximadamente 17 salarios mínimos
            otros_ingresos = 2000000,
            retenciones_fuente = 1000000,
            pagos_seguridad_social = 800000,
            aportes_pension = 600000,
            pagos_creditos_hipotecarios = 500000,
            donaciones = 150000,
            gastos_educacion = 250000,

        )
        valor_esperado = 2743000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoExtra1(self):
            #Altos gastos en comparación con sus ingresos
            calculadora = CalculadoraDeImpuestos(
                ingresos_laborales = 20000000,  # Aproximadamente 17 salarios mínimos
                otros_ingresos = 3000000,
                retenciones_fuente = 1500000,
                pagos_seguridad_social = 3000000,
                aportes_pension = 2000000,
                pagos_creditos_hipotecarios = 1200000,
                donaciones = 1000000,
                gastos_educacion = 1000000
            )
            valor_esperado = 1312000.0
            resultado = calculadora.calcular_valor_impuesto()
            self.assertEqual(resultado, valor_esperado)
                

    def testCasoExtra2(self):
        # Ingresos y gastos altos en donaciones
        calculadora = CalculadoraDeImpuestos(
            ingresos_laborales=25000000,
            otros_ingresos=5000000,
            retenciones_fuente=2000000,
            pagos_seguridad_social=1500000,
            aportes_pension=1000000,
            pagos_creditos_hipotecarios=800000,
            donaciones=3000000,  # Alto en comparación con los ingresos
            gastos_educacion=400000
        )
        valor_esperado = 2427000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoExtra3(self):
        # Grandes ingresos con gastos elevados en educación
        calculadora = CalculadoraDeImpuestos(
            ingresos_laborales=30000000,
            otros_ingresos=4000000,
            retenciones_fuente=2500000,
            pagos_seguridad_social=2000000,
            aportes_pension=1500000,
            pagos_creditos_hipotecarios=1000000,
            donaciones=500000,
            gastos_educacion=3000000  # Muy alto en comparación con otros gastos
        )
        valor_esperado = 2440000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoExtra4(self):
        # Ingreso bajo con gastos muy altos en seguridad social
        calculadora = CalculadoraDeImpuestos(
            ingresos_laborales=14000000,
            otros_ingresos=2000000,
            retenciones_fuente=1000000,
            pagos_seguridad_social=7000000,  # Muy alto en comparación con los ingresos
            aportes_pension=500000,
            pagos_creditos_hipotecarios=300000,
            donaciones=150000,
            gastos_educacion=200000
        )
        valor_esperado = 491500.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoExtra5(self):
        # Ingreso moderado con donaciones y pagos de créditos elevados
        calculadora = CalculadoraDeImpuestos(
            ingresos_laborales=18000000,
            otros_ingresos=2500000,
            retenciones_fuente=1300000,
            pagos_seguridad_social=900000,
            aportes_pension=700000,
            pagos_creditos_hipotecarios=3000000,  # Elevado en comparación con los ingresos
            donaciones=2500000,  # Alto en comparación con los ingresos
            gastos_educacion=300000
        )
        valor_esperado = 1189000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)

    def testCasoExtra6(self):
        # Ingresos altos con todos los gastos elevados
        
        calculadora = CalculadoraDeImpuestos(
            ingresos_laborales=35000000,
            otros_ingresos=5000000,
            retenciones_fuente=3000000,
            pagos_seguridad_social=2500000,
            aportes_pension=2000000,
            pagos_creditos_hipotecarios=1500000,
            donaciones=1000000,
            gastos_educacion=1500000
        )
        valor_esperado = 2985000.0
        resultado = calculadora.calcular_valor_impuesto()
        self.assertEqual(resultado, valor_esperado)


    def testCasoError1(self):
                self.calculadora = CalculadoraDeImpuestos(
                    #Gastos de seguridad social superiores a los ingresos

                    ingresos_laborales = 15000000,  # Aproximadamente 13 salarios mínimos
                    otros_ingresos = 2000000,
                    retenciones_fuente = 1000000,
                    pagos_seguridad_social = 20000000,  # Muy alto en comparación con los ingresos
                    aportes_pension = 600000,
                    pagos_creditos_hipotecarios = 400000,
                    donaciones = 150000,
                    gastos_educacion = 200000


                )
            

    def testCasoError2(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Retenciones negativas

            ingresos_laborales = 20000000,  # Aproximadamente 17 salarios mínimos
            otros_ingresos = 3000000,
            retenciones_fuente = -1000000,  # Valor negativo
            pagos_seguridad_social = 1200000,
            aportes_pension = 800000,
            pagos_creditos_hipotecarios = 500000,
            donaciones = 200000,
            gastos_educacion = 300000


        )

    def testCasoError3(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Gastos de seguridad social y aportes negativos

            ingresos_laborales = 25000000,  # Aproximadamente 22 salarios mínimos
            otros_ingresos = 2000000,
            retenciones_fuente = 1500000,
            pagos_seguridad_social = -1000000,  # Valor negativo
            aportes_pension = -500000,  # Valor negativo
            pagos_creditos_hipotecarios = 600000,
            donaciones = 200000,
            gastos_educacion = 400000


        )

    def testCasoError4(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Donaciones extremadamente altas en comparación con ingreso

            ingresos_laborales = 20000000,  # Aproximadamente 17 salarios mínimos
            otros_ingresos = 3000000,
            retenciones_fuente = 1000000,
            pagos_seguridad_social = 800000,
            aportes_pension = 600000,
            pagos_creditos_hipotecarios = 400000,
            donaciones = 10000000,  # Muy alto en comparación con los ingresos
            gastos_educacion = 200000



        )
    
    def testCasoError5(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Campos con valores de tipo incorrecto

            ingresos_laborales = "cincuenta millones",  # Tipo de dato incorrecto
            otros_ingresos = 3000000,
            retenciones_fuente = 1500000,
            pagos_seguridad_social = 1000000,
            aportes_pension = 500000,
            pagos_creditos_hipotecarios = 600000,
            donaciones = 200000,
            gastos_educacion = 300000


        )

    def testCasoError6(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Ingresos laborales menores o iguales a cero

            ingresos_laborales = 0,  # Valor no válido
            otros_ingresos = 2000000,
            retenciones_fuente = 1000000,
            pagos_seguridad_social = 800000,
            aportes_pension = 600000,
            pagos_creditos_hipotecarios = 400000,
            donaciones = 150000,
            gastos_educacion = 200000



        )

    def testCasoError7(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Gastos en seguridad social menores o iguales a cero

            ingresos_laborales = 15000000,
            otros_ingresos = 2000000,
            retenciones_fuente = 1000000,
            pagos_seguridad_social = 0,  # Gastos no pueden ser cero
            aportes_pension = 600000,
            pagos_creditos_hipotecarios = 400000,
            donaciones = 150000,
            gastos_educacion = 200000


        )
    
    
    

if __name__ == '__main__':
    unittest.main()



