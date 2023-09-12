"""
Para cada empleado de una fabrica se debe calcular su liquidación de salario. Los empleados se encuentran precargados, 
pero se pueden agregar mas segun ingresaron antes de la liquidación mensual. 
Para cada empleado se conoce: nombre - paga por hora - faltas. Los empleados trabajan una jornada mensual de 160 hs. 
El salario neto a liquidar es el bruto (paga por hora * jornada mensual de hora ) menos las retenciones. 
Las retenciones son:
- 10% para jubilación 
- 6% para obra social 
- 2% sindicato 
- Se descuenta 1 día de paga por cada falta (el día se calcula como una jornada de 8hs) 
- Si el salario bruto es mayor a 400.000 se retiene un 35% sobre el monto excedido 
Mostrar un menú hasta que el usuario lo indica con las opciones: 
1-  nuevo empleado (agrega un empleado a la plantilla de empleado) 
2- Sumar falta empleado (buscar el empleado por nombre y le suma una falta)
3 - liquidar salarios (muestra un reporte con el salario bruto y neto a pagar a cada empleado) 
La funciones para calcular las retenciones se deben incluir en un módulo liquidacion.py
"""
import os
import retenciones

list_empleados = [{'nombre': 'Carlos Alvarez', 'paga_hora': float(4000), 'cant_faltas': 0},
                  {'nombre': 'Pedro Sanchez', 'paga_hora': float(3500.5), 'cant_faltas': 2},
                  {'nombre': 'Alfonso Pilato', 'paga_hora': float(4000), 'cant_faltas': 1}
]

respuesta=""
def menu():
    print("")
    print("---------------------------------")
    print("Sistema de liquidación de sueldos")
    print("---------------------------------")
    print("1 - Nuevo empleado")
    print("2 - Sumar falta empleado")
    print("3 - Liquidar salarios")
    print("4 - Salir")

while respuesta != "salir":
    menu()
    opcion = input("\n Ingrese la opción de menú: ")
    os.system ("cls")                                   #Limpiar pantalla
    if opcion.isnumeric():
        if int(opcion) == 1:
            os.system ("cls")
            empleado   =input("Ingrese el nombre del empleado: ")
            paga_hora  =input("Ingrese el monto a pagar por hora al nuevo empleado: ")
            list_empleados.append({'nombre':empleado, 'paga_hora': float(paga_hora), 'cant_faltas': 0})
            print("")
            input("Presione cualquier tecla para continuar....")    # Pausa
            os.system ("cls")                                   #Limpiar pantalla
        elif int(opcion) == 2:
            os.system ("cls")                                       # Limpia pantalla
            # Debo buscar empleado ---> si lo encuentra ---> agrega días falta a ese empleado
            empleado   =input("Ingrese el nombre del empleado: ")
            for nombre_empleado in list_empleados:
                if empleado==nombre_empleado["nombre"]:
                    nombre_empleado["cant_faltas"]+=1
                    print(f"Se sumó un día de inasistencia al empleado {nombre_empleado['nombre']}, sus faltas totales son {nombre_empleado['cant_faltas']}: ")
                    break
                else:
                    print(f"El empleado {empleado} ingresado no existe, por favor verifique")
                    break
            print("")
        elif int(opcion) == 3:
            os.system ("cls")                                       # Limpia pantalla
            # Cálculo del bruto (descontados los días faltados x el empleado)
            # Bruto = Horas trabajadas(sin faltas son 160hs) * salario hora trabajada
            # Debo descontar 8hs por cada día sin asistir al trabajo
            for empleado in list_empleados:
                cant_faltas=empleado['cant_faltas']
                print(f"Cantidad de días de inasistencias del empleado {empleado['nombre']}: {empleado['cant_faltas']}")
                horas_inasistencia=cant_faltas*8
                print(f"Cantidad de horas descontadas al sueldo bruto: {horas_inasistencia}")
                total_hs_trabajadas=160-horas_inasistencia
                print(f"Cantidad de horas liquidadas del empleado {empleado['nombre']}: {total_hs_trabajadas}")
                bruto_empleado=total_hs_trabajadas*empleado["paga_hora"]
                print(f"Total liquidación del empleado {empleado['nombre']} (Importe Bruto): $ {bruto_empleado}")
                if bruto_empleado>400000:
                    # Si el empleado gana más de 400mil se le descuenta el 35% del exceso
                    retencion=(bruto_empleado-400000)*0.35
                    print(f"La retención adicional sobre el bruto por superar los $ 400.000, es de $ {retencion}")
                    bruto_empleado-=retencion
                neto_a_cobrar=retenciones.calcular_retenciones(bruto_empleado)
                print(f"El neto a cobrar del empleado {empleado['nombre']} es: $ {neto_a_cobrar}")
                print("")
            input("Presione cualquier tecla para continuar....")    # Pausa
            os.system("cls")                                        # Limpia pantalla
        elif int(opcion) == 4:
            os.system ("cls")                                       # Limpia pantalla
            respuesta = "salir"
        else: print("Ingrese una opción válida")        # No ingresó ninguna de las opciones
    else:                                               # No ingresó un número
        print("Ingrese una opción numérica")

input("Presione cualquier tecla para continuar....")    # Pausa
os.system ("cls")

