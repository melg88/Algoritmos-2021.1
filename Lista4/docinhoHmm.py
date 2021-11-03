def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j][0] >= pivot[0]:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):

    if len(arr) == 1:
        return arr
    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

    return arr


if __name__ == '__main__':
    products = []
    x = input().split(' ')

    total = int(x[0])
    n = 0
    combo = int(x[1])

    while n < total:
        value = int(input())
        products.append((value, n))
        n += 1

    lenght = len(products)
    sortList = quickSort(products, 0, lenght - 1)
    i = 0
    sum = 0
    listproducts = ""
    while i < combo:
        sum += sortList[i][0]
        listproducts = listproducts + \
            (" " if listproducts != "" else "") + str(sortList[i][1])
        i += 1
    sum -= 1 * combo
    print("O combo vai custar {a} reais, e os produtos escolhidos foram: {b}".format(
        a=sum, b=listproducts))
