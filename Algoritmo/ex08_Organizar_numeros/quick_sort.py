def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quick_sort(lista, inicio, p-1)
        quick_sort(lista, p+1, fim)
    print(lista)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

lista = [1,2,3,4,-1,-2,-3,-4,0,3,5,1,5]

quick_sort(lista)