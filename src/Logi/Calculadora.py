class CalculoException(Exception):
    def _init_(self, mensaje):
        super()._init_(mensaje)

def calcular_iva(base_imponible: float, tasa_iva: float) -> float:
    """Calcula el IVA a partir de la base imponible y la tasa de IVA."""
    return base_imponible * tasa_iva

def CalcularCouta(ingresos_laborales: int, otros_ingresos: int, retenciones_fuente: int, pagos_seguridad_social: int, aportes_pension: int, pagos_creditos_hipotecarios: int, donaciones: int, gastos_educacion: int, tasa_iva: float = 0.19):
    """Calcula la cuota de impuestos a partir de los ingresos y deducciones proporcionadas."""
    
    # Validaciones
    if ingresos_laborales < 0 or otros_ingresos < 0 or retenciones_fuente < 0 or pagos_seguridad_social < 0 or aportes_pension < 0 or pagos_creditos_hipotecarios < 0 or donaciones < 0 or gastos_educacion < 0:
        raise CalculoException("Los valores no pueden ser negativos.")

    if ingresos_laborales <= 0:
        raise CalculoException("Los ingresos laborales deben ser mayores que cero.")

    if pagos_seguridad_social > ingresos_laborales:
        raise CalculoException("Los pagos de seguridad social no pueden exceder los ingresos laborales.")

    if aportes_pension > ingresos_laborales:
        raise CalculoException("Los aportes a pensión no pueden exceder los ingresos laborales.")

    if pagos_creditos_hipotecarios > ingresos_laborales:
        raise CalculoException("Los pagos por créditos hipotecarios no pueden exceder los ingresos laborales.")

    if donaciones > ingresos_laborales:
        raise CalculoException("Las donaciones no pueden exceder los ingresos laborales.")

    if gastos_educacion > ingresos_laborales:
        raise CalculoException("Los gastos de educación no pueden exceder los ingresos laborales.")

    if gastos_educacion > ingresos_laborales + otros_ingresos:
        raise CalculoException("Los gastos de educación no pueden exceder la suma de ingresos laborales y otros ingresos.")

    if retenciones_fuente < 0:
        raise CalculoException("Las retenciones de fuente no pueden ser negativas.")

    if pagos_seguridad_social == 0:
        raise CalculoException("Los pagos de seguridad social no pueden ser cero.")

    if ingresos_laborales < gastos_educacion + otros_ingresos + retenciones_fuente + pagos_seguridad_social + aportes_pension + pagos_creditos_hipotecarios + donaciones:
        raise CalculoException("Los ingresos no son suficientes para cubrir los gastos y deducciones.")
    
    # Cálculo del impuesto antes de retenciones
    base_imponible = (ingresos_laborales + otros_ingresos) - (pagos_seguridad_social + aportes_pension + pagos_creditos_hipotecarios + donaciones + gastos_educacion)
    
    if base_imponible < 0:
        raise CalculoException("La base imponible es negativa, verifique los ingresos y deducciones.")

    # Calcular el IVA utilizando la función separada
    impuesto = calcular_iva(base_imponible, tasa_iva)
    impuesto_final = impuesto - retenciones_fuente

    if impuesto_final < 0:
        raise CalculoException("Los impuestos son negativos, vuelva a intentar.")

    return impuesto_final
    
