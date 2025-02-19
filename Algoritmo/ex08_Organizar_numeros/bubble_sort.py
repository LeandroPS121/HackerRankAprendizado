def bubble_sort(lista):
    n = len(lista)
    for _ in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

    print(lista)

lista = [312,3,31,2,3,5,8,9,0,-2,-3,4]

bubble_sort(lista)