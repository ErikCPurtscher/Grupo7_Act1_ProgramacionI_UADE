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