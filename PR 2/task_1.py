import math

def obchyslyty_z(m, n):
    try:
        z = (math.sqrt(m) - math.sqrt(n)) / m
        return z
    except ZeroDivisionError:
        return "Pomylka: m ne mozhe dorivnyuvaty 0"
    except ValueError:
        return "Pomylka: nemozhlyvo vziaty korin z vid’yemnoho chysla"

def chy_doskonałe(chyslo):
    if chyslo <= 1:
        return False
    suma_dilnykiv = 0
    for i in range(1, chyslo):
        if chyslo % i == 0:
            suma_dilnykiv += i
    return suma_dilnykiv == chyslo

if __name__ == "__main__":
    m = int(input("Vvedit m: "))
    n = int(input("Vvedit n: "))

    z = obchyslyty_z(m, n)
    print("Rezultat obchyslennya z =", z)
    n = -1
    while not 0<=n:
        n = int(input("Vvedit n:"))
    if chy_doskonałe(n):
        print(f"Chyslo {n} ye doskonalym")
    else:
        print(f"Chyslo {n} ne ye doskonalym")