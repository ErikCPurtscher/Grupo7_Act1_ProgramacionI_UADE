from funciones.utilidades import seleccionar_actividad
from funciones.validaciones import validar_positivo, validar_texto


def dar_alta(socios, actividades):
    print("Dar de alta un registro")

    codigo_maximo = 0
    for socio in socios:
        if socio[0] > codigo_maximo:
            codigo_maximo = socio[0]
    codigo = codigo_maximo + 1

    nombre = validar_texto("Nombre del socio: ")
    nombre_actividad= seleccionar_actividad(actividades)

    print("Ingrese el valor de la cuota")
    valor_cuota = validar_positivo()

    estado = "activo"

    socio = [codigo, nombre, nombre_actividad, valor_cuota, estado]
    socios.append(socio)

    print("Socio registrado con éxito:")
    print(socio)
    return

def consultar(socios):
    print("Consultar un registro")

    print("Indique el registro a consultar: ", end= "")
    registro= validar_positivo()   # <---- Nose si hace falta validar por positivo acá 
    encontrado = False

    while not encontrado:

        for fila in range(len(socios)):
            if registro == socios[fila][0]:

                print("Código:", socios[fila][0])
                print("Socio:", socios[fila][1])
                print("Actividad principal:", socios[fila][2])
                print("Valor de la cuota:", socios[fila][3])
                print("Estado:", socios[fila][4])

                encontrado = True
        if not encontrado:
            registro = int(input("No existe el número de registro, seleccione otro: "))


#función buscar_socio para aplicar en funciones consultar y modificar
def buscar_socio(socios, codigo):
    encontrado = False
    pos = 0
    while pos < len(socios) and not encontrado:
        if socios[pos][0] == codigo:
            encontrado = True
        else:
            pos += 1
    if not encontrado:
        pos = -1
    return pos



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

