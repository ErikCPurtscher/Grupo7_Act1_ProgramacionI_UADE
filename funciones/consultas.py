from funciones.utilidades import seleccionar_actividad, completar_espacios, calcular_ancho_texto


def filtrar_por_actividad(socios, actividad):
 
    socios_por_actividad = []
    
    for i in range(len(socios)):
        if actividad == socios[i][2]:
            socios_por_actividad.append(socios[i])
    return socios_por_actividad      


def mostrar_socios(socios):
    print("MOSTRAR TODOS LOS SOCIOS")
    print()
    encabezados = ["CÓD", "NOMBRE", "ACTIVIDAD", "VALOR CUOTA", "ESTADO"]
    anchos = []
    
    for columna in range(len(socios[0])):
        ancho= calcular_ancho_texto(socios, columna, encabezados[columna])
        anchos.append(ancho)

    for i in range(len(encabezados)):
        print(completar_espacios(encabezados[i], anchos[i]), end="")

    print()

    for fila in range(len(socios)):
        for columna in range(len(socios[fila])):
            print(completar_espacios(socios[fila][columna], anchos[columna]), end="")
        print()

def consultar_por_actividad(socios, actividades):

    actividad = seleccionar_actividad(actividades)
    socios_filtrados = filtrar_por_actividad(socios, actividad)

    if len(socios_filtrados) > 0: 
        mostrar_socios(socios_filtrados)
    else:        
        print("No existe registro de socio actual con la actividad:" , actividad)
    
   