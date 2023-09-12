def calcular_retenciones(bruto_empleado):
    # El salario neto a liquidar es el bruto (el dato viene del llamado a la función)
    # menos las retenciones:
    # - 10% jubilación
    # - 6% obra social
    # - 2% sindicato
    jubilacion=bruto_empleado*0.10
    obra_social=bruto_empleado*0.06
    sindicato=bruto_empleado*0.02
    neto_a_cobrar=bruto_empleado-(jubilacion+obra_social+sindicato)
    return(neto_a_cobrar)