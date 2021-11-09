import math


def merge(vet, left, mid, right):

    n1 = mid - left + 1
    n2 = right - mid

    indexLeft = [0] * (n1)
    indexRight = [0] * (n2)

    for i in range(0, n1):
        indexLeft[i] = vet[left + i]

    for j in range(0, n2):
        indexRight[j] = vet[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if indexLeft[i] <= indexRight[j]:
            vet[k] = indexLeft[i]
            i += 1
        else:
            vet[k] = indexRight[j]
            j += 1
        k += 1

    while i < n1:
        vet[k] = indexLeft[i]
        i += 1
        k += 1

    while j < n2:
        vet[k] = indexRight[j]
        j += 1
        k += 1


def mergeSort(vet, left, right):
    if left < right:

        mid = left+(right-left)//2

        mergeSort(vet, left, mid)
        mergeSort(vet, mid+1, right)
        merge(vet, left, mid, right)


def mudaSinal(vet, n):

    for i in range(0, n):
        vet[i] = -vet[i]

    return vet


def calculaPoints(vet, n):

    par = []

    for i in range(0, n - 1, 2):

        sub = vet[i] - vet[i+1]
        par.append(sub)

    return par


if __name__ == '__main__':
    n = int(input())

    i = 0

    points = []

    while i != n:

        point = int(input())

        points.append(point)

        i += 1

    mudaSinal(points, n)

    mergeSort(points, 0, n-1)

    mudaSinal(points, n)

    print(points)

    par = calculaPoints(points, n)

    print(par)

    midP = math.ceil(n/2) - 1

    mergeSort(par, 0, midP)

    for i in range(0, midP + 1):

        print(par[i])
