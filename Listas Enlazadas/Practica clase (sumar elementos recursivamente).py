class Node:
    def __init__(self, valor): #init: nos permite representar un numero
        self.data = valor
        self.next = None #el puntero siguiente None== Null
#Fin de la clase Nodo

#creacion de la lista
class SinglyLinkedList:
    def __init__ (self):
        self.head = None #el puntero cabeza es None

    def insert(self, valor): # el caso de insertar cuando no existe
        new_node =Node(valor) #creamos un nuevo nodo
        if (self.head is None): #si esta vacia la lista
            self.head = new_node
            return
        current = self.head # Current puntero que nos permite recorrer la lista
        while (current.next): #mientras el puntero siguiente no sea None
            current = current.next #avanzamos al siguiente nodo
        current.next = new_node #cuando llegamos al final, insertamos el nuevo nodo

    def display(self): #se asemeja al recorrido de un to string
        current = self.head
        while (current): #recorre uno por uno cada nodo
            print(current.data, end=" -> ")
            current = current.next # lo que permite es navegar por la lista
        print("None") #cuando llegamos al final, imprimimos None

    def suma_elementos(self, nodo):
        if nodo.next is None:
            return nodo.data
        
        return self.suma_elementos(nodo.next) + nodo.data 

lista = SinglyLinkedList()
lista.insert(10)
lista.insert(20)
lista.insert(30)
lista.insert(40)
lista.insert(50)
lista.insert(60)

lista.display()
print(lista.suma_elementos(lista.head))

        
