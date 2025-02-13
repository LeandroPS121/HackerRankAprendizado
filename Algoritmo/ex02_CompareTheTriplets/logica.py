def comparar_triplos(a,b):
    resultado = [0,0]
    for i in range(3):
        if a[i] > b[i]:
            resultado[0] += 1
        elif a[i] < b[i]:
            resultado[1] += 1
        else:
            pass
    return resultado