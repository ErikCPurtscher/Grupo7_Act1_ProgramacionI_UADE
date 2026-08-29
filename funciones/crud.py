

def dar_alta(socios, actividades):
    print("Dar de alta un registro")

    codigo = len(socios) + 1
    nombre = input("Nombre del socio: ")
    cont =0
    for titulos in actividades:
         print(cont ,"-", titulos)
         cont +=1

    actividad = int(input("Selecione actividad: "))
    while actividad > len(actividades) or actividad <0:
        actividad = int(input("Seleccione un número de actividad existente: "))

    for activ in range(len(actividades)):
            nombre_actividad = actividades[actividad]
                    
    valor_cuota = int(input("Valor de cuota: "))
    estado = "activo"
    socio = [codigo, nombre, nombre_actividad, valor_cuota, estado]
    socios.append(socio)
    print(socio)
    return

def consultar(socios):
    print("Consultar un registro")
    
    registro = int(input("Seleccione el registro a consultar "))
    largo_socios = len(socios)

    while registro > largo_socios or registro <0:
        registro = int(input("No existe el número de registro, seleccione otro "))

    for fila in range(largo_socios):
        if registro == socios[fila][0]:
            print(socios[fila])

def modificar():
    None

def eliminar():
    None

