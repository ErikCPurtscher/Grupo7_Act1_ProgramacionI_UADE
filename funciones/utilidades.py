
def consultar_actividades(actividades, largo_actividades, minimo):
    cont= minimo   
    for i in range(largo_actividades):
        print(cont ,"-", actividades[i])
        cont +=1

def seleccionar_actividad(actividades):
    
    print("Actividades disponibles")
    largo_actividades = len(actividades)
    minimo = 1
    consultar_actividades(actividades, largo_actividades, minimo)

    valor = int(input("Seleccione una actividad: "))
    while valor < minimo or valor > largo_actividades:
            print("El valor debe estar combrendido entre" , minimo, "y", len(actividades), end=": ")
            valor = int(input("Seleccione una actividad: "))

    print("el valor seleccionado", valor)
    return actividades[valor-1]

