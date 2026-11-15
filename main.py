from Pilas import pila

if __name__ == "__main__":
    pila1 = pila()
    op = -1

    while op != 0:
        print("\n--- Operaciones de la pila ---")
        print("1. Crear pila")
        print("2. Mostrar pila")
        print("3. Insertar elemento en la pila")
        print("4. Eliminar elemento de la pila")
        print("5. Mostrar elemento de la cima de la pila")
        print("6. Limpiar pila")
        print("7. Tamaño de la pila")
        print("8. Promedio de la pila")
        print("9. Buscar elemento")
        print("10. Sumar elementos")
        print("0. Salir")

        try:
            op = int(input("Seleccione una opción: "))
            match op:
                case 1:
                  pila1.crear_pila()
                  print("Pila creada exitosamente.")
                case 2:
                    pila1.imprimir()
                case 3:
                    dato = int(input("Ingrese el elemento a insertar: "))
                    pila1.push(dato)
                case 4:
                    eliminado = pila1.pop()
                    if eliminado == "Error: Underflow":
                        print(eliminado)
                    else:
                        print(f"Elemento {eliminado} eliminado de la pila.")
                case 5:
                    cima = pila1.peek()
                    if cima == "Error: Underflow":
                        print(cima)
                    else:
                        print(f"Elemento en la cima de la pila: {cima}")
                case 6:
                    pila1.clean()
                    print("Pila limpiada.")
                case 7:
                    tamano = pila1.size()
                    print(f"Tamaño de la pila: {tamano}")
                case 8:
                    prom = pila1.promedio()
                    if prom == "Error: Underflow":
                        print(prom)
                    else:
                        print(f"Promedio de los elementos de la pila: {prom}")
                case 9:
                    dato = int(input("Ingrese el elemento a buscar: "))
                    encontrado = pila1.buscar(dato)
                    if encontrado:
                        print(f"Elemento {dato} encontrado en la pila.")
                    else:
                        print(f"Elemento {dato} no encontrado en la pila.")
                case 10:
                    suma = pila1.sumar_elementos()
                    print(f"Suma de los elementos de la pila: {suma}")
                case 0:
                    print("Saliendo del programa.")
                case _:
                    print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
    
