def split_list():
    A = list(input("Введіть елементи списку (без пробілів): "))
    digits = [x for x in A if x.isdigit()]
    letters = [x for x in A if x.isalpha()]
    print("Цифри:", digits)
    print("Літери:", letters)
    return digits, letters

split_list()