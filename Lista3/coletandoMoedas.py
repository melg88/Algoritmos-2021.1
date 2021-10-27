class HashTable:

    def __init__(self, tam):
        self.array = [None] * tam
        self.totalCapacity = tam
        self.itemCapacity = [100] * tam

    def insertHash(self, HashTable, coins, key):
        if(self.array[key] == None):
            self.array[key] = []
            self.array[key].append(coins)
            self.itemCapacity[key] -= coins

        elif(coins <= self.itemCapacity[key]):

            self.array[key].append(coins)
            self.itemCapacity[key] -= coins

        else:
            key = reHashKey(coins, self.totalCapacity)
            if(self.array[key] != None):
                if(coins > self.itemCapacity[key]):
                    print("Nao foi possivel adicionar a mochila...")
                    return -1
                else:
                    key = HashTable.insertHash(HashTable, coins, key)
                    # return key
            else:
                key = HashTable.insertHash(HashTable, coins, key)
        return key

    def validaBackpackCheia(self, indice, vetCapacity):
        var = vetCapacity[indice]
        qtd = var
        inicial = 0
        i = 0
        x = 0

        for x in range(indice):
            inicial += vetCapacity[x]

        if(var == 26):
            for i in range(26):
                if(self.itemCapacity[inicial] == 0):
                    inicial += 1
                    bool = True
                else:
                    bool = False
            if(bool):
                print("Ghost Backpack esta cheia!")
        elif(var == 24):
            for i in range(24):
                if(self.itemCapacity[inicial] == 0):
                    inicial += 1
                    bool = True
                else:
                    bool = False
            if(bool):
                print("Winged Backpack esta cheia!")

        elif(var == 22):
            for i in range(22):
                if(self.itemCapacity[inicial] == 0):
                    inicial += 1
                    bool = True
                else:
                    bool = False
            if(bool):
                print("Jeweled Backpack esta cheia!")
        else:
            for i in range(20):
                if(self.itemCapacity[inicial] == 0):
                    inicial += 1
                    bool = True
                else:
                    bool = False
            if(bool):
                print("Ghost Backpack esta cheia!")

    def hashCapacity(self, key):
        capacity = self.itemCapacity[key]
        if(capacity == None):
            print()
        elif(capacity > 0):
            print("Contem " + str(capacity) + " espacos restantes.")
        else:
            print("Espaco Cheio!")
            return 0

        if(capacity == 100):
            print()
        else:

            Hash.hashHistoric(int(operation[1]))

    def hashHistoric(self, key):
        toPrint = ""
        for x in (self.array[key]):
            toPrint += str(x) + ' '
        toPrint = toPrint[:-1]
        print(toPrint)


def hashKey(coins, capacity):
    coin = int(coins)
    return (coin % capacity)


def reHashKey(coins, capacity):
    coin = int(coins)
    return int((((coin % capacity) + 100) * (coin % capacity)) % capacity)


def validaPos(key, indice, vetCapacity, backpackAllName, var):
    string = ''
    if(var == 0):
        var = vetCapacity[indice]

    if(key <= var):
        return indice
    else:
        indice += 1
        var += vetCapacity[indice]
        string = validaPos(key, indice, vetCapacity, backpackAllName, var)
    return string


if __name__ == '__main__':
    backpackNumber = int(input())
    backpackAllName = []
    vetCapacity = []
    arrayG = []

    totalCapacity = 0

    i = 0
    while(i <= backpackNumber - 1):
        backpackName = input()

        if(backpackName == 'Ghost Backpack'):
            vetCapacity.append(26)
            backpackAllName.append("Ghost Backpack")
            arrayG = arrayG + ["Ghost Backpack"] * 26

        elif(backpackName == 'Winged Backpack'):
            vetCapacity.append(24)
            backpackAllName.append("Winged Backpack")
            arrayG = arrayG + ["Winged Backpack"] * 24

        elif(backpackName == 'Jewelled Backpack'):
            vetCapacity.append(22)
            backpackAllName.append("Jewelled Backpack")
            arrayG = arrayG + ["Jewelled Backpack"] * 22

        elif(backpackName == 'Backpack'):
            vetCapacity.append(20)
            backpackAllName.append("Backpack")
            arrayG = arrayG + ["Backpack"] * 20

        totalCapacity = sum(vetCapacity)

        i += 1

    Hash = HashTable(totalCapacity)

    while True:
        try:
            indice = 0
            var = 0
            operation = input().split(' ')
            if(operation[0] == 'ADD'):
                if(int(operation[1]) > 100):
                    print("Nao foi possivel adicionar a mochila...")
                else:
                    key = hashKey(int(operation[1]), int(totalCapacity))

                    n = Hash.insertHash(Hash, int(operation[1]), key)
                    indice = validaPos(
                        n, indice, vetCapacity, backpackAllName, var)

                    if(n != -1):
                        print("Adicionadas em " + str(n) +
                              " na " + str(arrayG[n]) + ".")
                        Hash.validaBackpackCheia(indice, vetCapacity)

            elif(operation[0] == 'CAP'):
                Hash.hashCapacity(int(operation[1]))
            else:
                break

            if(operation == ['']):
                break
        except EOFError:
            break

