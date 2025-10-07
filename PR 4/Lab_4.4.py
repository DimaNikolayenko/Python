def replace_negatives():
    A = list(map(float, input("Введіть список чисел: ").split()))
    result = [0 if x < 0 else x for x in A]
    print("Результат:", result)
    return result

replace_negatives()
