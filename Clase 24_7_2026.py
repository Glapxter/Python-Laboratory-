import os
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

    def errase_Position(self, position):
        # Lista vacía
        if self.head is None:
            print("La lista está vacía.")
            return
        # Eliminar el primer nodo
        if position == 0:
            self.head = self.head.next
            return
        actual = self.head
        contador = 0
        # Buscar el nodo anterior a la posición
        while actual.next is not None and contador < position - 1:
            actual = actual.next
            contador += 1
        # Verificar si la posición existe
        if actual.next is None:
            print("Posición fuera de rango.")
            return
        # Saltar el nodo que se desea eliminar
        actual.next = actual.next.next

# Eliminar al inicio
    def errase_beginning(self):
        # Verificar si la lista esta vacia
        if self.head is None:
            print("\nLista vacia")
            return
        # Eliminar el primer nodo
        self.head = self.head.next

    def queHace(self): # El metodo elimina al final de la lista
        if self.inicio is None: # Verifica si la cabeza de la lista esta vacia
            print("La lista está vacía.")
            return

        if self.inicio.next is None: # Verifica si al que apunta head esta vacio
            self.inicio = None # de estar vacio el siguiente de head elimina la cabeza de la lista
            return

        actual = self.inicio 

        while actual.next.next is not None: # recorre la lista hasta el final y elimina el ultimo
            actual = actual.next
        actual.next = None

    # Define si la lista esta vacia
    def define_if_list_is_Empty(self):
        if self.head is None: # Verifica si la cabeza de la lista esta vacia
            print("La lista está vacía.")
            return
        print("La lista no esta vacía")

    # Busca un elemento de la lista
    def search_in_list(self, data):
        current = self.head
        while (current):
            if current.data == data:
                print("Valor encontrado")
                return
            current = current.next
        print("El valor no se encuentra en la lista")

# Menú de la lista
def Menu_list():
        print("\n---- List Menu ----")
        print("1. Insert number")
        print("2. Insert number at beginning")
        print("3. Insert number in midle")
        print("4. Errase number at beginning")
        print("5. Errase by position")
        print("6. Search a value")
        print("7. Display list")
        print("8. Display inverted list")
        print("9. Exit\n")

        option= int(input("ingrese una opción del menú: "))
        match option:
            #insert options
            case 1:
                lista1.insert(int(input("Ingrese un numero: ")))
            case 2:
                lista1.insertBeginning(int(input("Ingrese un numero: ")))
            case 3:
                lista1.insertMiddle(int(input("Ingrese un numero: ")))
            #errase options
            case 4:
                lista1.errase_beginning()
            case 5:
                lista1.errase_Position()
            #search option
            case 6:
                lista1.search_in_list(int(input("Ingrese un numero a buscar: ")))
            #display options
            case 7:
                lista1.display()
            case 8:
                print(lista1.revers(lista1.head)) #mostramos la lista al reves
            #exit option
            case 9:
                print("\nFinalizando sessión")
                return False

        while (Menu_list()):
            os.system('pause')
            os.system('cls')
          
 # implementación de metodos                    
lista1 = SinglyLinkedList() #creamos una lista
Menu_list()