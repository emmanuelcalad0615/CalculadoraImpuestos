def CalcularCouta(ingresos_laborales: int, otros_ingresos: int, retenciones_fuente: int, pagos_seguridad_social: int, aportes_pension: int, pagos_creditos_hipotecarios: int, donaciones: int, gastos_educacion: int):

    if ingresos_laborales < 0 or otros_ingresos < 0 or retenciones_fuente < 0 or pagos_seguridad_social < 0 or aportes_pension < 0 or pagos_creditos_hipotecarios < 0 or donaciones < 0 or gastos_educacion < 0:
        raise Exception("Los valores no pueden ser negativos.")

    if ingresos_laborales <= 0:
        raise Exception("Los ingresos laborales deben ser mayores que cero.")

    if pagos_seguridad_social > ingresos_laborales:
        raise Exception("Los pagos de seguridad social no pueden exceder los ingresos laborales.")

    if aportes_pension > ingresos_laborales:
        raise Exception("Los aportes a pensión no pueden exceder los ingresos laborales.")

    if pagos_creditos_hipotecarios > ingresos_laborales:
        raise Exception("Los pagos por créditos hipotecarios no pueden exceder los ingresos laborales.")

    if donaciones > ingresos_laborales:
        raise Exception("Las donaciones no pueden exceder los ingresos laborales.")

    if gastos_educacion > ingresos_laborales:
        raise Exception("Los gastos de educación no pueden exceder los ingresos laborales.")

    if gastos_educacion > ingresos_laborales + otros_ingresos:
        raise Exception("Los gastos de educación no pueden exceder la suma de ingresos laborales y otros ingresos.")

    if retenciones_fuente < 0:
        raise Exception("Las retenciones de fuente no pueden ser negativas.")

    if pagos_seguridad_social == 0:
        raise Exception("Los pagos de seguridad social no pueden ser cero.")

    if ingresos_laborales < gastos_educacion + otros_ingresos + retenciones_fuente + pagos_seguridad_social + aportes_pension + pagos_creditos_hipotecarios + donaciones:
        raise Exception("Los ingresos no son suficientes para cubrir los gastos y deducciones.")
    
    if ((((ingresos_laborales + otros_ingresos)-(pagos_seguridad_social + aportes_pension + pagos_creditos_hipotecarios + donaciones + gastos_educacion))*0.19) - retenciones_fuente) < 0:
        raise Exception("Los impuestos son negativos, vuelva a intentar")
    
    else: 
        return ((((ingresos_laborales + otros_ingresos)-(pagos_seguridad_social + aportes_pension + pagos_creditos_hipotecarios + donaciones + gastos_educacion))*0.19) - retenciones_fuente)
  
    
