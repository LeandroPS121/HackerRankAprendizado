def staircase(n):
    concatena =''

    for i in range(1,n+1):
        concatena += f'{'#'*i:>{n}}' + '\n'

    print(concatena)