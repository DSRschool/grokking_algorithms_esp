def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivote = array[0]
        menores = [i for i in array[1:] if i <= pivote]
        mayores = [i for i in array[1:] if i > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

print(quicksort([10, 5, 2, 3]))
