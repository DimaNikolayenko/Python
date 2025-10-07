def min_negative():
    n = int(input("Введіть кількість елементів масиву N = "))
    arr = [float(input(f"Елемент {i+1}: ")) for i in range(n)]
    negatives = [x for x in arr if x < 0]

    if negatives:
        print("Мінімальний від’ємний елемент:", min(negatives))
    else:
        print("В масиві немає від’ємних елементів")

min_negative()