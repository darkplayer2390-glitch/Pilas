class pila:
    class Nodo:
        def __init__(self, info: int):
            self.dato = info
            self.siguiente = None

    def __init__(self):
        self.tope = None

    def crear_pila(self):
        """Método interactivo para crear o poblar la pila con múltiples elementos"""
        print("\n--- Crear Pila ---")
        # Opcional: Reiniciar la pila si ya tenía elementos
        self.tope = None
        
        res = int(input("¿Deseas agregar un elemento a la pila? (1: Sí, 0: No): "))
        while res == 1:
            dato = int(input("Introduce el valor para el elemento: "))
            self.push(dato)
            res = int(input("¿Deseas agregar otro elemento? (1: Sí, 0: No): "))

    def push(self, dato: int):
        nuevo = self.Nodo(dato)
        nuevo.sig = self.tope
        self.tope = nuevo

    def is_empty(self) -> bool:
        return self.tope is None

    def pop(self) -> int | str:
        """Elimina y muestra el elemento de la cima"""
        if self.is_empty():
            return "Error: Underflow"

        informacion = self.tope.dato
        self.tope = self.tope.sig
        return informacion

    def imprimir(self):
        """Muestra los elementos de la pila"""
        if self.is_empty():
            print("[pila vacía]")
            return
        reco = self.tope
        while reco is not None:
            print(reco.dato)
            reco = reco.sig

    def peek(self) -> int | str:
        """Muestra el elemento de la cima sin eliminarlo"""
        if self.is_empty():
            return "Error: Underflow"
        return self.tope.dato

    def clean(self):
        """Elimina todos los elementos de la pila"""
        self.tope = None

    def size(self) -> int:
        """Devuelve el tamaño de la pila"""
        contador = 0
        reco = self.tope
        while reco is not None:
            contador += 1
            reco = reco.sig
        return contador

    def promedio(self) -> float | str:
            """Calcula el promedio de los elementos de la pila"""
            if self.is_empty():
                return "Error: Underflow"
    
            suma = 0
            contador = 0
            reco = self.tope
            while reco is not None:
                suma += reco.dato
                contador += 1
                reco = reco.sig
    
            return suma / contador

    def buscar(self, dato: int) -> bool:
        """Busca un valor en la pila y devuelve True si se encuentra, False en caso contrario"""
        reco = self.tope
        while reco is not None:
            if reco.dato == dato:
                return True
            reco = reco.sig
        return False

    def sumar_elementos(self) -> int:
        """Suma todos los elementos de la pila y devuelve el resultado"""
        suma = 0
        reco = self.tope
        while reco is not None:
            suma += reco.dato
            reco = reco.sig
        return suma