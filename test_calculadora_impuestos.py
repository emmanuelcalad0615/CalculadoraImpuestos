import unittest
from calculadora_impuestos import CalculadoraDeImpuestos

class TestCalculadoraDeImpuestos(unittest.TestCase):

    def setUp(self):
        self.calculadora = CalculadoraDeImpuestos(

            ingresos_laborales=50000000,
            otros_ingresos=10000000,
            retenciones_fuente=5000000,
            pagos_seguridad_social=4000000,
            aportes_pension=3000000,
            pagos_creditos_hipotecarios=2000000,
            donaciones=1000000,
            gastos_educacion=500000
        )

    def testCasoNormal1(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Ingreso mensual medio con algunos ingresos adicionales


            ingresos_laborales = 14000000, # Aproximadamente 12 salarios mínimos
            otros_ingresos = 2000000,
            retenciones_fuente = 1000000,
            pagos_seguridad_social = 800000,
            aportes_pension = 500000,
            pagos_creditos_hipotecarios = 300000,
            donaciones = 150000,
            gastos_educacion = 200000
        )

    def testCasoNormal2(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Ingreso para un trabajador con ingresos adicionales

            ingresos_laborales = 20000000,  # Aproximadamente 17 salarios mínimos
            otros_ingresos = 3000000,
            retenciones_fuente = 1500000,
            pagos_seguridad_social = 1200000,
            aportes_pension = 800000,
            pagos_creditos_hipotecarios = 500000,
            donaciones = 200000,
            gastos_educacion = 300000

        )

    def testCasoNormal3(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Ingreso para un trabajador con salario alto

            ingresos_laborales = 25000000,  # Aproximadamente 22 salarios mínimos
            otros_ingresos = 2500000,
            retenciones_fuente = 2000000,
            pagos_seguridad_social = 1500000,
            aportes_pension = 1000000,
            pagos_creditos_hipotecarios = 800000,
            donaciones = 300000,
            gastos_educacion = 400000

        )

    def testCasoNormal4(self):
        self.calculadora =  CalculadoraDeImpuestos(
            #Ingreso para una persona con salario medio y algunos ingresos extras

            ingresos_laborales = 16000000,  # Aproximadamente 14 salarios mínimos
            otros_ingresos = 2500000,
            retenciones_fuente = 1200000,
            pagos_seguridad_social = 1000000,
            aportes_pension = 600000,
            pagos_creditos_hipotecarios = 400000,
            donaciones = 200000,
            gastos_educacion = 250000


        )

    def testCasoNormal5(self):
        self.calculadora =  CalculadoraDeImpuestos(
           # Ingreso bajo con gastos de educación moderados

            ingresos_laborales = 12000000,  # Aproximadamente 10 salarios mínimos
            otros_ingresos = 1500000,
            retenciones_fuente = 800000,
            pagos_seguridad_social = 600000,
            aportes_pension = 400000,
            pagos_creditos_hipotecarios = 300000,
            donaciones = 100000,
            gastos_educacion = 150000


        )

    def testCasoNormal6(self):
        self.calculadora =  CalculadoraDeImpuestos(
            #Ingreso promedio con gastos diversos

            ingresos_laborales = 20000000,  # Aproximadamente 17 salarios mínimos
            otros_ingresos = 2000000,
            retenciones_fuente = 1000000,
            pagos_seguridad_social = 800000,
            aportes_pension = 600000,
            pagos_creditos_hipotecarios = 500000,
            donaciones = 150000,
            gastos_educacion = 250000,


       )
        
    def testCasoExtra1(self):
        self.calculadora =  CalculadoraDeImpuestos(
            #Altos gastos en comparación con sus ingresos
            
            ingresos_laborales = 20000000,  # Aproximadamente 17 salarios mínimos
            otros_ingresos = 3000000,
            retenciones_fuente = 1500000,
            pagos_seguridad_social = 3000000,
            aportes_pension = 2000000,
            pagos_creditos_hipotecarios = 1200000,
            donaciones = 1000000,
            gastos_educacion = 1000000


        )

    def testCasoExtra2(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Ingresos y gastos altos en donaciones

            ingresos_laborales = 25000000,  # Aproximadamente 22 salarios mínimos
            otros_ingresos = 5000000,
            retenciones_fuente = 2000000,
            pagos_seguridad_social = 1500000,
            aportes_pension = 1000000,
            pagos_creditos_hipotecarios = 800000,
            donaciones = 3000000, # Alto en comparación con los ingresos
            gastos_educacion = 400000


        )

    def testCasoExtra3(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Grandes ingresos con gastos elevados en educación
            
            ingresos_laborales = 30000000,  # Aproximadamente 26 salarios mínimos
            otros_ingresos = 4000000,
            retenciones_fuente = 2500000,
            pagos_seguridad_social = 2000000,
            aportes_pension = 1500000,
            pagos_creditos_hipotecarios = 1000000,
            donaciones = 500000,
            gastos_educacion = 3000000  # Muy alto en comparación con otros gastos


        )

    def testCasoExtra4(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Ingreso bajo con gastos muy altos en seguridad social

            ingresos_laborales = 14000000,  # Aproximadamente 12 salarios mínimos
            otros_ingresos = 2000000,
            retenciones_fuente = 1000000,
            pagos_seguridad_social = 7000000,  # Muy alto en comparación con los ingresos
            aportes_pension = 500000,
            pagos_creditos_hipotecarios = 300000,
            donaciones = 150000,
            gastos_educacion = 200000


        )

    def testCasoExtra5(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Ingresos con alta cantidad de pagos por créditos hipotecarios

            ingresos_laborales = 18000000,  # Aproximadamente 15 salarios mínimos
            otros_ingresos = 2500000,
            retenciones_fuente = 1200000,
            pagos_seguridad_social = 1000000,
            aportes_pension = 600000,
            pagos_creditos_hipotecarios = 2000000,  # Alto en comparación con otros gastos
            donaciones = 200000,
            gastos_educacion = 300000


        )
    
    def testCasoExtra6(self):
        self.calculadora = CalculadoraDeImpuestos(
            #Ingreso medio con grandes donaciones y gastos de educación
           
            ingresos_laborales = 16000000,  # Aproximadamente 14 salarios mínimos
            otros_ingresos = 2000000,
            retenciones_fuente = 1200000,
            pagos_seguridad_social = 1000000,
            aportes_pension = 700000,
            pagos_creditos_hipotecarios = 500000,
            donaciones = 2500000,  # Alto en comparación con los ingresos
            gastos_educacion = 500000,


        )

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

