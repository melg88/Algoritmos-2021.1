from os import curdir


class Node ():
    def __init__(self, point, name, left, right, parent, pre, suc):
        self.point = point
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent
        self.pre = pre
        self.suc = suc


class Tree:

    def __init__(self):
        self.root = None
        self.minimo = 0
        self.maximo = 0

        #self.size = 0

    def addNode(self, name, n):
        addOk = True
        newNode = Node(n, name, None, None, None, None, None)

        if(self.root == None):
            self.root = newNode
            self.minimo = newNode.point
            self.maximo = newNode.point
            return addOk

        else:
            current = self.root

            while current != None:
                previous = current
                if n == current.point or name == current.name:
                    addOk = False
                    return addOk
                elif(n < current.point):
                   # current = current.left  # se entrar aqui vai pra esquerda
                    if(current.left == None):
                        previous.left = newNode
                        newNode.parent = current

                        if(newNode.point < self.minimo):
                            self.minimo = newNode.point

                        return addOk
                    current = current.left

                elif(n > current.point):
                    #current = current.right
                    if(current.right == None):
                        current.right = newNode
                        newNode.parent = current

                        if(newNode.point > self.maximo):
                            self.maximo = newNode.point

                        return addOk
                    current = current.right

    def find(self, point):
        current = self.findNode(self.root, point)
        return current

    def findNode(self, currentNode, point):
        if(currentNode == None):
            return False

        elif(point == currentNode.point):
            return currentNode
        elif(point < currentNode.point):
            return self.findNode(currentNode.left, point)
        else:
            return self.findNode(currentNode.right, point)

    def findPreSuc(self, currentNode, key, pre=None, suc=None):

        if currentNode is None:
            return None

        if currentNode.point == key:

            if currentNode.left is not None:
                tmp = currentNode.left
                while(tmp.right):
                    tmp = tmp.right
                pre = tmp

            if currentNode.right is not None:
                tmp = currentNode.right
                while(currentNode.left):
                    tmp = tmp.left
                suc = tmp

            return pre, suc

        if currentNode.point > key:
            suc = currentNode
            self.findPreSuc(currentNode.left, key, pre, suc)

        else:
            pre = currentNode
            self.findPreSuc(currentNode.right, key, pre, suc)

    def getNameBypoint(self, point):
        currentNode = self.find(point)
        return currentNode.name

    def getNameByNode(self, current):
        currentNode = current
        return currentNode.name

    def getpoint(self, current):
        return current.point

    def getAlone(self):
        current = self.root
        if(current.left == None and current.right == None):
            return True
        else:
            return False

    def getFirstNode(self):
        return self.root


if __name__ == '__main__':
    root = Tree()

    pre = None
    suc = None

    numberOperations = int(input())

    while(numberOperations > 0):

        operation = input().split(' ')

        if(operation[0] == 'ADD'):
            add = root.addNode(str(operation[1]), int(operation[2]))

            if(add):
                print(operation[1] + " inserido com sucesso!")
            else:
                print(operation[1] + " ja esta no sistema.")

        elif(operation[0] == 'PROX'):

            pointMin = root.minimo
            pointMax = root.maximo

            op = int(operation[1])

            node = root.find(op)

            #predSuc = root.findPreSuc(node, op)

            isAlone = root.getAlone()
            if(isAlone == True):

                name = root.getNameBypoint(op)
                print("Apenas " + str(name) + " existe no sistema...")

            else:
                nodeRaiz = root.getFirstNode()
                preSuc = root.findPreSuc(nodeRaiz, op, pre, suc)

                if(op == pointMin):

                    nameMin = root.getNameBypoint(op)

                    nameSuc = root.getNameByNode(preSuc[1])

                    print(str(nameMin) +
                          " e o menor! e logo apos vem " + str(nameSuc))

                elif(op == pointMax):
                    if(preSuc == None):
                        nameMax = root.getNameBypoint(op)
                        namePred = root.getNameBypoint(pointMin)

                    else:
                        nameMax = root.getNameBypoint(op)
                        namePred = root.getNameByNode(preSuc[0])

                    print(str(nameMax) +
                          " e o maior! e logo atras vem " + str(namePred))

                else:

                    if(preSuc == None):
                        current = root.find(op)
                        preSuc = root.findPreSuc(current.parent, op, pre, suc)

                        namePred = root.getNameByNode(preSuc[0])
                        nameSuc = root.getNameByNode(preSuc[1])

                        print(str(name) + " vem apos " +
                              str(namePred) + " e antes de " + str(nameSuc))
                    else:

                        namePred = root.getNameByNode(preSuc[0])
                        nameSuc = root.getNameByNode(preSuc[1])

                        print(str(name) + " vem apos " + str(namePred) +
                              " e antes de " + str(nameSuc))

        numberOperations -= 1
