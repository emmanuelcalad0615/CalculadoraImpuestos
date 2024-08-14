class CalculadoraDeImpuestos:
    def __init__(self, ingresos_laborales, otros_ingresos, retenciones_fuente, pagos_seguridad_social, aportes_pension, pagos_creditos_hipotecarios, donaciones, gastos_educacion):
        
        self.ingresos_laborales = ingresos_laborales
        self.otros_ingresos = otros_ingresos
        self.retenciones_fuente = retenciones_fuente
        self.pagos_seguridad_social = pagos_seguridad_social
        self.aportes_pension = aportes_pension
        self.pagos_creditos_hipotecarios = pagos_creditos_hipotecarios
        self.donaciones = donaciones
        self.gastos_educacion = gastos_educacion

    def calcular_total_ingresos_gravados(self):
        return self.ingresos_laborales + self.otros_ingresos

    def calcular_total_ingresos_no_gravados(self):
        return self.pagos_seguridad_social + self.aportes_pension + self.pagos_creditos_hipotecarios + self.donaciones + self.gastos_educacion

    def calcular_total_costos_deducibles(self):
        return self.calcular_total_ingresos_no_gravados()

    def calcular_valor_impuesto(self):
        total_ingresos_gravados = self.calcular_total_ingresos_gravados()
        total_costos_deducibles = self.calcular_total_costos_deducibles()
        base_gravable = total_ingresos_gravados - total_costos_deducibles
        valor_impuesto = base_gravable * 0.19  # Supongamos una tasa de impuesto del 19%
        return valor_impuesto - self.retenciones_fuente
    
class SeguridadInvalida(Exception):
        pass

class RetencionesInvalidas(Exception):
    pass

class ValoresNegativos(Exception):
    pass

class DonacionesExcesivas(Exception):
    pass

class TipoDatoIncorrecto(Exception):
    pass

class IngresoLaboralInvalido(Exception):
    pass

class SeguridadSocialInvalida(Exception):
    pass

# Ejemplo de uso
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

print(f"Valor a pagar por impuesto de renta: {calculadora.calcular_valor_impuesto()}")

