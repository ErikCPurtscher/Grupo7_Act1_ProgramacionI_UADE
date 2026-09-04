def validar_texto(mensaje):
    texto = input(mensaje)
    while texto == "":
        print("El valor no puede estar vacío.")
        texto = input(mensaje)
    return texto    


def validar_positivo():
    valor = int(input())
    while valor <0:
        print("El valor debe ser positivo", end=" ")
        valor = int(input())
    return  valor

def validar_rango(minimo,maximo):
    print("Seleccione una actividad.")
    print("Ingrese un número entre", minimo, "y", maximo, end=": ")
    valor = int(input())
    while valor < minimo or valor > maximo:
        print("Seleccione una actividad.")
        print("Ingrese un número entre", minimo, "y", maximo, end=": ")
        valor = int(input())
    return valor

def validar_confirmacion():
    confirmacion = input("¿Desea modificar modificar el valor? S/N : ")
    while confirmacion != 'S' or confirmacion != 's' or confirmacion != 'N' or confirmacion != 'n':
        print("Valor inválido. Ingrese S o N.")
        confirmacion = str(input("¿Desea modificar modificar el valor? S/N : "))
    return confirmacion
