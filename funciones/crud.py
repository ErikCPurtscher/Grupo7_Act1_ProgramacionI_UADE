

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
    
    registro = int(input("Indique el registro a consultar: "))
    largo_socios = len(socios)

    while registro > largo_socios or registro <0:
        registro = int(input("No existe el número de registro, seleccione otro "))

    for fila in range(largo_socios):
        if registro == socios[fila][0]:
            print(socios[fila])

def modificar(socios,actividades):
    print("Modificar un registro")
    #Cantidad de registros totales
    largo_socios = len(socios)
    print("Registros totales:",largo_socios)
    #Lectura de registro por teclado y validacion
    registro = int(input("Indique el registro a modificar: "))
    while registro > largo_socios or registro < 0:
        registro = int(input("No existe el número de registro, seleccione otro "))
    #Recorro matriz de socios hasta encotrar el registro buscado
    for fila in range(largo_socios):
            if registro == socios[fila][0]:
                print(socios[fila])
                print()
                #Modificar nombre
                confirmacion = str(input("¿Modificar nombre? S/N : "))
                while confirmacion != 'S' or confirmacion != 'N':
                    print("Valor inválido. Ingrese S o N.")
                    confirmacion = str(input("¿Modificar nombre? S/N : "))
                if confirmacion == 'S':
                    socios[fila][1] = str(input("Ingrese nuevo nombre del socio: "))
                print()
                #Modificar actividad
                confirmacion = str(input("¿Modificar actividad principal? S/N : "))
                while confirmacion != 'S' or confirmacion != 'N':
                    print("Valor inválido. Ingrese S o N.")
                    confirmacion = str(input("¿Modificar actividad? S/N : "))
                if confirmacion == 'S':
                    #Print de las actividades validas
                    for titulos in actividades:
                        print(cont ,"-", titulos)
                    #Indicar actividad y validacion
                    actividad = int(input("Selecione actividad: "))
                    while actividad > len(actividades) or actividad < 0:
                        actividad = int(input("Seleccione un número de actividad existente: "))
                    socios[fila][2] = actividad
                print()
                #Modificar valor de cuota
                confirmacion = str(input("¿Modificar valor de cuota? S/N : "))
                while confirmacion != 'S' or confirmacion != 'N':
                    print("Valor inválido. Ingrese S o N.")
                    confirmacion = str(input("¿Modificar valor de cuota? S/N : "))
                if confirmacion == 'S':
                    socios[fila][3] = int(input("Ingrese nuevo valor de cuota: "))
                print()
                #Modificar estado
                confirmacion = str(input("¿Modificar estado? S/N : "))
                while confirmacion != 'S' or confirmacion != 'N':
                    print("Valor inválido. Ingrese S o N.")
                    confirmacion = str(input("¿Modificar estado? S/N : "))
                if confirmacion == 'S':
                    if socios[fila][4] == 'activo'
                        socios[fila][4] = 'inactivo'
                    if socios[fila][4] == 'inactivo'
                        socios[fila][4] = 'activo'
                print()
                #Mostrar nuevo registro
                print("Registro modificado:")
                print(socios[fila])


def eliminar():
    None

