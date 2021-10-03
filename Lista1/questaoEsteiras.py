class Node:
    def __init__(self, name):
        self.name = name  # nome
        self.previous = None  # anterior
        self.next = None  # proximo

    def __str__(self):
        return "{product}".format(product=self.name)



class Queue:
    def __init__(self):
        self.head = None  # aponta pra o primeiro
        self.tail = None  # aponta pra o rabo
        self.size = 0  # aponta

    def isEmpty(self):
        return self.size == 0  # se for vazia retorna falso

    def insert(self, product):
        newNode = Node(product)
        if(self.size == 0):  
            self.head = newNode
            self.tail = self.head
        else:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    def dequeue(self):
        element = self.head
        self.head = self.head.next
        self.size -= 1
        return element

    def printList(self):
        currentNode = self.head
        var = ""
        while(currentNode != None):
          var += (str(currentNode) + ' ')
          currentNode = currentNode.next
        var = var[:-1]
        return var
          



class Product:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{person}".format(person=self.name)



class conveyorBelt:
    def __init__(self, num):
        self.queue = Queue()
        self.num = num

    def __str__(self):
      return str(self.num)

    def addProduct(self, product):
      self.queue.insert(product)
        
    def printQueue(self):
      toPrint = self.queue.printList()
      print(toPrint)


    def removeProduct(self):
      dequeueProduct = self.queue.dequeue()
      return dequeueProduct
        


if __name__ == '__main__':
    number = int(input())
    counter = 1
    fileira = []
    running = True


    while(counter <= number):
      obj = conveyorBelt(counter)
      fileira.append(obj)
      counter += 1


    while(running):
        command = str(input(""))
        command = command.split(" ")


        if(command[0] == "INS"):
          product = Product(command[2])
          a = fileira[int(command[1])]
          a.addProduct(product)
          print('O produto: "{name}" foi adicionado na esteira {num}.'.format(name=product, num=command[1]))


        elif(command[0] == "RMV"):
          a = fileira[int(command[1])]

          if(a.queue.isEmpty()):
            print("Nao ha produtos para empacotar na esteira {esteira}!".format(esteira=command[1]))

          else:
            element = a.removeProduct()
            print('O produto: "{name}" foi empacotado com sucesso!'.format(
              name=element))

            if(a.queue.isEmpty()):
              print("A esteira {num} ficou vazia...".format(num = command[1]))
          
        
        elif(command[0] == "MOV"):

          if((int(command[1]) > number or int(command[2]) > number)):
            print("Erro ao mover produto.")
            
          else:
            a = fileira[int(command[1])]

            if(a.queue.isEmpty()):
              print("Erro ao mover produto.")

            else:
              element = a.removeProduct()
              b = fileira[int(command[2])]
              b.addProduct(element)
              print('O produto: "{name}" movido para a esteira {num}.'.format(name = element, num = command[2]))


        elif(command[0] == "SHW"):
          a = fileira[int(command[1])]
          print("Esteira " + command[1] + ": ")
          if(a.queue.isEmpty()):
              print()
          else:
            a.printQueue()

        else:
          running = False