#Sistema gimnasio

''' Datos de registros:
Número de socio; Nombre; Actividad principal; Valor de la cuota; Estado.
'''
from funciones.menu import mostrar_menu, pedir_opcion


ACTIVIDADES_VALIDAS = ["Musculacion", "Funcional", "Pileta", "Yoga", "Spinning"]

socios = [
    [1, "Erik Purtscher", "Musculacion", 15000, "Activo"],
    [2, "Agostina Koya", "Pileta", 18000, "Activo"],
    [3, "Felipe Storni", "Funcional", 16000, "Inactivo"],
    [4, "Nicolas Defelippo", "Yoga", 14000, "Activo"],
    [5, "Nardone Fernandez", "Spinning", 15500, "Inactivo"],
]

mostrar_menu()
pedir_opcion()

opcion = ""
while opcion != 8:
    mostrar_menu()
    opcion = pedir_opcion()

    if opcion == 1:
        None
    elif opcion == 2:
        None
    elif opcion == 3:
        None
    elif opcion == 4:
        None
    elif opcion == 5:
        None
    elif opcion == 6:
        None
    elif opcion == 7:
        None