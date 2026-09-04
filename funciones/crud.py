from funciones.utilidades import seleccionar_actividad
from funciones.validaciones import validar_positivo, validar_texto, validar_rango, validar_confirmacion

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
    registro= validar_positivo()   
    pos = buscar_socio(socios, registro)

        
    if pos !=-1 :
        print("Código:", socios[pos][0])
        print("Socio:", socios[pos][1])
        print("Actividad principal:", socios[pos][2])
        print("Valor de la cuota:", socios[pos][3])
        print("Estado:", socios[pos][4])
    else:
        print("El registro", registro, "no existe")
  

def modificar_socio(socios, actividades):
    print("Modificar un registro")
    # Lectura del registro
    registro = int(input("Indique el registro a modificar: "))
    # Búsqueda del registro. Si el registro existe, se solicitan los nuevos valores
    pos = buscar_socio(socios, registro)
    if pos != -1:
        print("Registro encontrado.")
        # Modificar nombre y apellido
        print("Nombre y Apellido: [" , socios[pos][1] ,"]")
        confirmacion = validar_confirmacion()
        if confirmacion == "S" or confirmacion == "s":
            nombre = validar_texto("Ingres nuevo nombre y apellido: ")
            socios[pos][1] = nombre
        
        # Modificar actividad
        print("Actividad principal: [" , socios[pos][2] , "]")
        confirmacion = validar_confirmacion()
        if confirmacion == "S" or confirmacion == "s":
            nueva_actividad = seleccionar_actividad(actividades)
            socios[pos][2] = nueva_actividad

        # Modificar valor de cuota
        print("Valor de cuota: [" , socios[pos][3] , "]")
        confirmacion = validar_confirmacion()
        if confirmacion == "S" or confirmacion == "s":
            valor_cuota = validar_positivo()
            socios[pos][3] = valor_cuota

        # Modificar estado
        print("Estado: [" , socios[pos][4] , "]")
        confirmacion = validar_confirmacion()
        if confirmacion == "S" or confirmacion == "s":
            if socios[pos][4] == 'activo':
                socios[pos][4] = 'inactivo'
            if socios[pos][4] == 'inactivo':
                socios[pos][4] = 'activo'

        # Mostrar registro modificado
        # === IDEA ===> ACÁ TAMBIÉN SE PODRÍA ESPERAR UNA ÚLTIMA CONFIRMACIÓN
            # Quizá si al inicio se utiliza un [while cont == 0] y que el cont solo aumente si en esta etapa se confirma la modificación del registro.
            # De esa manera se mantiene el ciclo de 
        print("Registro modificado.")   # === IDEA ===> ACÁ SE PODRÍA MOSTRAR EL REGISTRO MODIFICADO DE MANERA TABULADA
        print("Código:", socios[pos][0])
        print("Socio:", socios[pos][1])
        print("Actividad principal:", socios[pos][2])
        print("Valor de la cuota:", socios[pos][3])
        print("Estado:", socios[pos][4])
    else:
        
        print("El registro", registro, "no existe")

                

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
            socios.remove(socios[fila]) #No vimos la función remove en la materia, hay que usar pop
            return

