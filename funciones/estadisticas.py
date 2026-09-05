def calcular_estadisticas(socios, actividades):
    print("=== ESTADÍSTICAS ===")

    #1. Cantidad total de registros
    total = len(socios)
    print("Cantidad total de socios:", total)

    #2. Cantidad de socios activos
    cantidad_activos = 0
    for socio in socios:
        if socio[4] == 'activo':
            cantidad_activos += 1
    print("Cantidad de socios activos:", cantidad_activos)

    #3. Cantidad de socios inactivos
    cantidad_inactivos = 0
    for socio in socios:
        if socio[4] == 'inactivo':
            cantidad_inactivos += 1
    print("Cantidad de socios inactivos:", cantidad_inactivos)

    #4. Estadística adicional: promedio de cuota
    suma_cuotas = 0
    for socio in socios:
        suma_cuotas += socio[3]
    promedio = suma_cuotas / total
    print("Valor promedio de cuota: $", promedio)

    #5. Cantidad por categoría (pide una categoría puntual)
    cont = 1
    for titulos in actividades:
        print(cont, "-", titulos)
        cont += 1
    actividad = int(input("Seleccione una actividad para ver cuántos socios tiene: "))
    while actividad > len(actividades) or actividad < 1:
        actividad = int(input("Seleccione un número de actividad existente: "))
    actividad = actividad - 1  #ajusto a índice real de la lista (arranca en 0)

    cantidad_actividad = 0
    for socio in socios:
        if socio[2] == actividades[actividad]:
            cantidad_actividad += 1
    print("Cantidad de socios en", actividades[actividad], ":", cantidad_actividad)
