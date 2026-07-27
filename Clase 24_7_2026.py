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

    def insertBeginning(self, valor): #insertar al inicio
        new_node=Node(valor)
        new_node.next=self.head
        self.head=new_node

    def insertMiddle(self, valor): #insertar al medio
        new_node=Node(valor)
        if self.head is None: #si la lista esta vacia
            self.head=new_node
            return

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        new_node.next = slow.next
        slow.next = new_node
        
    def revers(self, node):
        if node.next is None:
            return node.data
        return str(self.revers(node.next))+" -> "+ str(node.data)
           

lista1 = SinglyLinkedList() #creamos una lista
lista1.insert(10) #insertamos un nodo con valor 10
lista1.insert(20) #insertamos un nodo con valor 20
lista1.insert(30) #insertamos un nodo con valor 30
lista1.insert(40)
lista1.insert(50)
lista1.insert(60)
lista1.insert(70)
lista1.insertBeginning(8) #insertamos un nodo con valor 5 al inicio
lista1.insertMiddle(100) #insertamos un nodo con valor 25 al medio
lista1.display() #mostramos la lista

print(lista1.revers(lista1.head)) #mostramos la lista al reves

#Tarea para el martes:
#1. crear la funcion de insertar al inicio (Listo)


#2. crear la funcion de insertar al medio (Listo)