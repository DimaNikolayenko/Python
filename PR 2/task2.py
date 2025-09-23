def x(n):
    if n <= 1:
        return False
    suma_dilnykiv = 0
    for i in range(1, n):
        if n % i == 0:
            suma_dilnykiv += i
    return suma_dilnykiv == n