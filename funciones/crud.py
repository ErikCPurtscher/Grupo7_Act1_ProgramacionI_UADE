from funciones.utilidades import seleccionar_actividad
from funciones.validaciones import validar_positivo, validar_texto, validar_rango, validar_confirmacion
from funciones.consultas import mostrar_socios


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
    print("ALTA DE SOCIO")
    print()
    codigo_maximo = 0
    for socio in socios:
        if socio[0] > codigo_maximo:
            codigo_maximo = socio[0]
    codigo = codigo_maximo + 1

    nombre = validar_texto("Nombre del socio: ")
    nombre_actividad= seleccionar_actividad(actividades)

    print("Ingrese el valor de la cuota:", end=" ")
    valor_cuota = validar_positivo()
    print()

    estado = "activo"

    socio = [codigo, nombre, nombre_actividad, valor_cuota, estado]
    socios.append(socio)

    print("¡Socio registrado con éxito!")
    # mostrar_socios(socio)
    print(socio)


def consultar(socios):
    print("CONSULTAR SOCIO")
    print()
    print("Indique el registro a consultar: ", end= "")
    registro= validar_positivo()   
    pos = buscar_socio(socios, registro)
    socio_consultado = []
        
    if pos !=-1 :
        socio_consultado.append(socios[pos])
        mostrar_socios(socio_consultado)
    else:
        print("El registro", registro, "no existe")
  

def modificar_socio(socios, actividades):
    print("MODIFICAR SOCIO")
    print()
    # Lectura del registro
    print("Indique el registro a modificar: ", end= "")
    registro = validar_positivo() 
    # Búsqueda del registro. Si el registro existe, se solicitan los nuevos valores
    pos = buscar_socio(socios, registro)

    if pos != -1:
        print("Registro encontrado.")
        print()
        # Modificar nombre y apellido
        print("Nombre y Apellido: [" , socios[pos][1] ,"]")
        confirmacion = validar_confirmacion()
        if confirmacion == "S" or confirmacion == "s":
            nombre = validar_texto("Ingrese nuevo nombre y apellido: ")
            socios[pos][1] = nombre
        print()
        # Modificar actividad
        print("Actividad principal: [" , socios[pos][2] , "]")
        confirmacion = validar_confirmacion()
        if confirmacion == "S" or confirmacion == "s":
            nueva_actividad = seleccionar_actividad(actividades)
            socios[pos][2] = nueva_actividad
        print()
        # Modificar valor de cuota
        print("Valor de cuota: [" , socios[pos][3] , "]")
        confirmacion = validar_confirmacion()
        if confirmacion == "S" or confirmacion == "s":
            valor_cuota = validar_positivo()
            socios[pos][3] = valor_cuota
        print()
        # Modificar estado
        print("Estado: [" , socios[pos][4] , "]")
        confirmacion = validar_confirmacion()
        if confirmacion == "S" or confirmacion == "s":
            if socios[pos][4] == 'activo':
                socios[pos][4] = 'inactivo'
            if socios[pos][4] == 'inactivo':
                socios[pos][4] = 'activo'
        print()
        # Mostrar registro modificado
        # === IDEA ===> ACÁ TAMBIÉN SE PODRÍA ESPERAR UNA ÚLTIMA CONFIRMACIÓN
            # Quizá si al inicio se utiliza un [while cont == 0] y que el cont solo aumente si en esta etapa se confirma la modificación del registro.
            # De esa manera se mantiene el ciclo de 
        print("Registro modificado.")
        print()
        print("Código:", socios[pos][0])
        print("Socio:", socios[pos][1])
        print("Actividad principal:", socios[pos][2])
        print("Valor de la cuota:", socios[pos][3])
        print("Estado:", socios[pos][4])
    else:
        
        print("El registro", registro, "no existe")

                

def eliminar(socios):
    print("ELIMINAR SOCIO")
    print()
    print("Indique el registro a eliminar: ", end= "") 
    registro = validar_positivo()

    pos = buscar_socio(socios, registro)

    if pos != -1:

        socio_eliminado = socios.pop(pos)
        print("Socio eliminado con éxito:", socio_eliminado)
    else:
        print("El registro", registro, "no existe")
    
