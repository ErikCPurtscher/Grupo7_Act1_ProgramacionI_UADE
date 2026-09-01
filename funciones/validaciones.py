def validar_texto(mensaje):
    texto = input(mensaje)
    while texto == "":
        texto = input(mensaje)

    return texto    


def validar_positivo():
    valor = int(input())
    while valor <0:
        print("El valor debe ser positivo", end=" ")
        valor = int(input())
    return  valor
