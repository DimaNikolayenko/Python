def matrix_variant20():
    n = 7
    a = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if j >= i:
                a[i][j] = n - j + i
            else:
                a[i][j] = 0

    for row in a:
        print(*row)

matrix_variant20()