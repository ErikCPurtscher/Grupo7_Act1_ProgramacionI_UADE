def mostrar_menu():
    print("\n=== GESTIÓN DE GIMNASIO ===")
    print("1. Dar de alta un socio")
    print("2. Consultar un socio")
    print("3. Modificar un socio")
    print("4. Eliminar un socio")
    print("5. Mostrar todos los socios")
    print("6. Consultar socios por actividad")
    print("7. Ver estadísticas")
    print("8. Salir")

def pedir_opcion():
    opcion = input("Seleccione una opción: ")
    return opcion

  #op = int(input("Ingrese el númeor de una opción: "))
  #while (op <= 0 or op > 7) and op != -1:
  #  print("Opción inválida - Ingrese un número del 1 al 8")
  #  =op int(input("Ingrese el númeor de una opción: "))
