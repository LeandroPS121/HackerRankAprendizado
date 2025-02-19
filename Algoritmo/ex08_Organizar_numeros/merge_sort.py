def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (fim + inicio)//2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    esq = lista[inicio:meio]
    dir = lista[meio:fim]

    topo_esq, topo_dir = 0, 0
    for k in range(inicio, fim):
        if topo_esq >= len(esq):
            lista[k] = dir[topo_dir]
            topo_dir += 1
        elif topo_dir >= len(dir):
            lista[k] = esq[topo_esq]
            topo_esq += 1
        elif esq[topo_esq] < dir[topo_dir]:
            lista[k] = esq[topo_esq]
            topo_esq += 1
        else:
            lista[k] = dir[topo_dir]
            topo_dir += 1

lista = [123,0,-3,-3,-5,-11,123,345,7,8,1,4,76,-10]

merge_sort(lista)