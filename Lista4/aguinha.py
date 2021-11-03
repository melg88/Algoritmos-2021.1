import sys


class MaxHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    def parent(self, pos):

        return pos // 2

    def leftChild(self, pos):

        return 2 * pos

    def rightChild(self, pos):

        return (2 * pos) + 1

    def isLeaf(self, pos):

        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):

        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
                                            self.Heap[fpos])

    def maxHeapify(self, pos):

        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] < self.Heap[self.rightChild(pos)]):

                if (self.Heap[self.leftChild(pos)] >
                        self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    def insert(self, element):

        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] >
               self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def isEmpty(self):
        if self.size == 0:
            return True

    def findAndRemoveMax(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)

        return popped


class Player:
    def __init__(self, destiny, water):
        self.destiny = destiny
        self.water = water
        self.parada = 0
        self.paradas = []

    def initHeap(self):
        maxH = MaxHeap(self.destiny)

        return maxH

    def run(self, indice):

        maxH = self.initHeap()

        if(self.water >= self.destiny):
            return self.parada

        if self.water < self.destiny:

            while indice <= self.water:
                if self.paradas[indice] != 0:
                    maxH.insert(self.paradas[indice])
                    indice += 1

                else:
                    indice += 1

            #self.water -= indice

            return self.attWater(indice, maxH)

    def attWater(self, indice, maxH):

        if(maxH.isEmpty()):
            return False

        else:

            root = maxH.findAndRemoveMax()

            if(root == None):
                return False

            else:

                self.water += root
                #indiceMax += root
                self.parada += 1

                return self.run(indice)


if __name__ == '__main__':
    n = 0

    x = input().split(' ')

    player = Player(int(x[0]), int(x[1]))

    total = int(input())

    n = 0
    i = 0

    player.paradas = [0] * int(x[0])

    while n < total:
        y = input().split(' ')

        player.paradas.insert(int(y[0]), int(y[1]))

        n += 1

    paradaFinal = player.run(0)

    if paradaFinal != False:
        print("E preciso no minimo " + str(paradaFinal) +
              " paradas para chegar no destino.")
    else:
        print("Nao e possivel chegar no destino, RIP.")
