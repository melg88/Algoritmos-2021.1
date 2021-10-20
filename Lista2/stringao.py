def binarySearch(vet, number):
    left = 0
    right = len(vet) - 1

    while left < right:

        mid = (left + right) // 2

        if vet[left] == number:
            return True
        if vet[right] == number:
            return True
        if vet[mid] == number:
            return True

        if vet[mid] < number:
            left = mid + 1
        else:
            right = mid

    if left > 0 and vet[left - 1] == number:
        return True
    else:
        return False


if __name__ == '__main__':
    find = ""

    line = input().split()
    line2 = input().split()

    vet = [int(numero) for numero in line]
    vetSearch = [int(numero) for numero in line2]

    for i in vetSearch:
        hasElement = binarySearch(vet, i)

        if(hasElement):
            find = find + str(i)

        else:
            find += '0'

    print(find)
