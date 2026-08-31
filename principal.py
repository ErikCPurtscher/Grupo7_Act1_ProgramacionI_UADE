#Sistema gimnasio

''' Datos de registros:
Número de socio; Nombre; Actividad principal; Valor de la cuota; Estado.
'''
from funciones.menu import mostrar_menu, pedir_opcion
from funciones.crud import dar_alta, consultar, modificar, eliminar


ACTIVIDADES = ["Musculacion", "Funcional", "Pileta", "Yoga", "Spinning"]

socios = [
    [1, "Erik Purtscher", "Musculacion", 15000, "activo"],
    [2, "Agostina Koya", "Pileta", 18000, "activo"],
    [3, "Felipe Storni", "Funcional", 16000, "inactivo"],
    [4, "Nicolas Defelippo", "Yoga", 14000, "activo"],
    [5, "Nardone Fernandez", "Spinning", 15500, "inactivo"],
]

opcion = 0
while opcion != 8:
    mostrar_menu()
    opcion = pedir_opcion()

    if opcion == 1:
        dar_alta(socios, ACTIVIDADES)
    elif opcion == 2:
        consultar(socios)
    elif opcion == 3:
        modificar(socios, ACTIVIDADES)
    elif opcion == 4:
        eliminar(socios)
    elif opcion == 5:
        None
        #mostrar_todos(socios)
    # 6 y 7 cuando estén listas
    elif opcion == 6:
        None
    elif opcion == 7:
        None
    elif opcion == 8:
        print("Saliendo...")