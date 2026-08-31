def dar_alta(socios, actividades):
    print("Dar de alta un registro")

    #El tema es que si usamos eliminar esto fallaria
    #codigo = len(socios) + 1

    codigo_maximo = 0
    for socio in socios:
        if socio[0] > codigo_maximo:
            codigo_maximo = socio[0]
    codigo = codigo_maximo + 1

    nombre = input("Nombre del socio: ")
    cont =0
    for titulos in actividades:
        print(cont ,"-", titulos)
        cont +=1

    actividad = int(input("Selecione actividad: "))
    while actividad >= len(actividades) or actividad <0:
        actividad = int(input("Seleccione un número de actividad existente: "))

    #for activ in range(len(actividades)):
    #    nombre_actividad = actividades[actividad]
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

    encontrado = False
    for fila in range(len(socios)):
        if registro == socios[fila][0]:
            print(socios[fila])
            encontrado = True

    while encontrado == False:
        registro = int(input("No existe el número de registro, seleccione otro: "))
        for fila in range(len(socios)):
            if registro == socios[fila][0]:
                print(socios[fila])
                encontrado = True

def modificar(socios, actividades):
    print("Modificar un registro")

    registro = int(input("Indique el registro a modificar: "))

    #si borro un socio, len(socios) ya no sirve para validar, busco por código
    encontrado = False
    for fila in range(len(socios)):
        if registro == socios[fila][0]:
            encontrado = True

    while encontrado == False:
        registro = int(input("No existe el número de registro, seleccione otro: "))
        for fila in range(len(socios)):
            if registro == socios[fila][0]:
                encontrado = True

    for fila in range(len(socios)):
            if registro == socios[fila][0]:
                print(socios[fila])
                print()
                #Modificar nombre
                confirmacion = str(input("¿Modificar nombre? S/N : "))
                while confirmacion != 'S' and confirmacion != 'N':
                    print("Valor inválido. Ingrese S o N.")
                    confirmacion = str(input("¿Modificar nombre? S/N : "))
                if confirmacion == 'S':
                    socios[fila][1] = str(input("Ingrese nuevo nombre del socio: "))
                print()
                #Modificar actividad
                confirmacion = str(input("¿Modificar actividad principal? S/N : "))
                while confirmacion != 'S' and confirmacion != 'N':
                    print("Valor inválido. Ingrese S o N.")
                    confirmacion = str(input("¿Modificar actividad? S/N : "))
                if confirmacion == 'S':
                    #Print de las actividades validas
                    cont = 0
                    for titulos in actividades:
                        print(cont ,"-", titulos)
                        cont += 1
                    #Indicar actividad y validacion
                    actividad = int(input("Selecione actividad: "))
                    while actividad >= len(actividades) or actividad < 0:
                        actividad = int(input("Seleccione un número de actividad existente: "))
                    socios[fila][2] = actividades[actividad]
                print()
                #Modificar valor de cuota
                confirmacion = str(input("¿Modificar valor de cuota? S/N : "))
                while confirmacion != 'S' and confirmacion != 'N':
                    print("Valor inválido. Ingrese S o N.")
                    confirmacion = str(input("¿Modificar valor de cuota? S/N : "))
                if confirmacion == 'S':
                    socios[fila][3] = int(input("Ingrese nuevo valor de cuota: "))
                print()
                #Modificar estado
                confirmacion = str(input("¿Modificar estado? S/N : "))
                while confirmacion != 'S' and confirmacion != 'N':
                    print("Valor inválido. Ingrese S o N.")
                    confirmacion = str(input("¿Modificar estado? S/N : "))
                if confirmacion == 'S':
                    if socios[fila][4] == 'activo':
                        socios[fila][4] = 'inactivo'
                    if socios[fila][4] == 'inactivo':
                        socios[fila][4] = 'activo'
                print()
                #Mostrar nuevo registro
                print("Registro modificado:")
                print(socios[fila])

def eliminar(socios):
    print("Eliminar un registro")

    registro = int(input("Indique el registro a eliminar: "))

    #mismo tema que en modificar, valido buscando el código
    encontrado = False
    for fila in range(len(socios)):
        if registro == socios[fila][0]:
            encontrado = True

    while encontrado == False:
        registro = int(input("No existe el número de registro, seleccione otro: "))
        for fila in range(len(socios)):
            if registro == socios[fila][0]:
                encontrado = True

    for fila in range(len(socios)):
        if registro == socios[fila][0]:
            print("Socio eliminado con éxito:", socios[fila])
            socios.remove(socios[fila])
            return

