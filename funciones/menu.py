def menu():
  print("1 - ")
  print("2 - ")
  print("3 - ")
  print("4 - ")
  print("5 - ")
  print("6 - ")
  print("7 - ")
  op = int(input("Ingrese el númeor de una opción: "))
  while (op <= 0 or op > 7) and op != -1:
    print("Opción inválida - Ingrese un número del 1 al 7 (-1 para salir)")
  
