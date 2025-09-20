def maxmin(arr):
    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    mid = len(arr) // 2
    min1, max1 = maxmin(arr[:mid])
    min2, max2 = maxmin(arr[mid:])
    return min(min1, min2), max(max1, max2)


numeros = [7, 2, 9, 4, 12, 1, 8, 10]
minimo, maximo = maxmin(numeros)
print(f"Mínimo: {minimo}, Máximo: {maximo}")
