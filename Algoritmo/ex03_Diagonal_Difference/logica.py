matriz = [
    [1,2,3],
    [4,5,6],
    [8,8,9]
    ]


def somar_diagonais(matriz):
    soma_diag_princ = 0
    soma_diag_sec = 0

    # somando a diagonal principal
    for i, _ in enumerate(matriz):
        soma_diag_princ += matriz[i][i]

    # somando a diagonal secundária
    for i, _ in enumerate(matriz):
        soma_diag_sec += matriz[i][-(i+1)]

    calcular_diferenca_absoluta(soma_diag_princ,soma_diag_sec)

def calcular_diferenca_absoluta(diag1,diag2):
    resultado = abs((diag1-diag2))
    print(resultado)