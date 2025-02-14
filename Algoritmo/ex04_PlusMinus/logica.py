def calcular_taxa_aparicao(arr):
    qnt_positivo = 0
    qnt_negativo = 0
    qnt_nulo = 0

    denominador = len(arr)
    for i in arr:
        if i>0:
            qnt_positivo+=1
        elif i<0:
            qnt_negativo+=1
        else:
            qnt_nulo+=1
    
    taxa_positivo = f'{qnt_positivo/denominador:.6f}'
    taxa_negativo = f'{qnt_negativo/denominador:.6f}'
    taxa_nulo = f'{qnt_nulo/denominador:.6f}'

    print(taxa_positivo)
    print(taxa_negativo)
    print(taxa_nulo)