def soma_max_min(arr):
    arr.sort()

    soma = 0
    for i in arr:
        soma+=i
    print(f'{soma-arr[-1]} {soma-arr[0]}')