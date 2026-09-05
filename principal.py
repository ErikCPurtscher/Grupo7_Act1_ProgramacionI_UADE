
from funciones.menu import mostrar_menu, pedir_opcion
from funciones.crud import dar_alta, consultar, modificar_socio, eliminar
from funciones.consultas import  mostrar_socios, consultar_por_actividad
from funciones.estadisticas import calcular_estadisticas
from datos import actividades, socios


opcion = 0
while opcion != 8:
    mostrar_menu()
    opcion = pedir_opcion()

    if opcion == 1:
        dar_alta(socios, actividades)
    elif opcion == 2:
        consultar(socios)
    elif opcion == 3:
        modificar_socio(socios, actividades)
    elif opcion == 4:
        eliminar(socios)
    elif opcion == 5:
        mostrar_socios(socios)
    elif opcion == 6:
        consultar_por_actividad(socios, actividades)
    elif opcion == 7:
        calcular_estadisticas(socios, actividades)
    elif opcion == 8:
        print("Saliendo...")