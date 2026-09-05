
def consultar_actividades(actividades, largo_actividades, minimo):
    cont= minimo   
    for i in range(largo_actividades):
        print(cont ,"-", actividades[i])
        cont +=1

def seleccionar_actividad(actividades):
    print()
    print("Actividades disponibles")
    largo_actividades = len(actividades)
    minimo = 1
    consultar_actividades(actividades, largo_actividades, minimo)
    
    valor = int(input("Seleccione una actividad: "))
    while valor < minimo or valor > largo_actividades:
            print("El valor debe estar comprendido entre" , minimo, "y", len(actividades), end=": ")
            print()
            valor = int(input("Seleccione una actividad: "))

    print("Actividad seleccionada:", valor, end=" ")
    print("-", actividades[valor-1])
    print()
    return actividades[valor-1]


def completar_espacios(texto, ancho):
    cantidad_espacios = ancho - len(str(texto))
    texto_con_espacios = str(texto) + " " * cantidad_espacios
    return texto_con_espacios


def calcular_ancho_texto(datos, columna, encabezado):
    ancho = len(encabezado)
    for i in range(len(datos)):
        if len(str(datos[i][columna])) > ancho:
            ancho = len(str(datos[i][columna]))
    return ancho + 3
