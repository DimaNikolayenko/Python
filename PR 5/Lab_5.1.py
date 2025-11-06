def print_all(baggage):
    """Вивести всі записи словника"""
    for key, value in baggage.items():
        print(f"{key}: {value}")

def add_record(baggage):
    """Додати новий запис до словника"""
    try:
        num = int(input("Введіть номер пасажира: "))
        count = int(input("Кількість речей: "))
        weight = float(input("Загальна вага (кг): "))
        baggage[num] = {"кількість": count, "вага": weight}
        print("Запис додано.")
    except ValueError:
        print("Помилка: введіть коректні числові значення.")

def delete_record(baggage):
    """Видалити запис із словника"""
    try:
        num = int(input("Введіть номер пасажира для видалення: "))
        del baggage[num]
        print("Запис видалено.")
    except KeyError:
        print("Такого пасажира не існує.")
    except ValueError:
        print("Помилка: введіть число.")

def print_sorted(baggage):
    """Вивести записи у відсортованому порядку за ключем"""
    for key in sorted(baggage.keys()):
        print(f"{key}: {baggage[key]}")

def analyze_baggage(baggage):
    """Виконати аналіз згідно з варіантом"""
    # а) кількість пасажирів, які мають більше двох речей
    more_than_two = sum(1 for b in baggage.values() if b["кількість"] > 2)
    print(f"а) Пасажирів із більше ніж двома речами: {more_than_two}")

    # б) чи є пасажир із 1 річчю вагою < 25 кг
    one_item_under_25 = any(b["кількість"] == 1 and b["вага"] < 25 for b in baggage.values())
    print("б) Є пасажир з 1 річчю вагою < 25 кг:", "так" if one_item_under_25 else "ні")

    # в) знайти багаж, де середня вага речі ≈ середній по всіх (±0.5 кг)
    total_items = sum(b["кількість"] for b in baggage.values())
    total_weight = sum(b["вага"] for b in baggage.values())
    avg_weight_per_item = total_weight / total_items
    print(f"Середня вага однієї речі серед усіх: {avg_weight_per_item:.2f} кг")

    matching_bags = [num for num, b in baggage.items()
                     if abs(b["вага"] / b["кількість"] - avg_weight_per_item) <= 0.5]

    if matching_bags:
        print("в) Номери багажів, що відповідають умові:", matching_bags)
    else:
        print("в) Таких багажів немає.")

def main():
    baggage = {
        1: {"кількість": 3, "вага": 45.0},
        2: {"кількість": 1, "вага": 23.0},
        3: {"кількість": 5, "вага": 72.5},
        4: {"кількість": 2, "вага": 40.0},
        5: {"кількість": 4, "вага": 58.0},
        6: {"кількість": 3, "вага": 46.2},
        7: {"кількість": 1, "вага": 28.0},
        8: {"кількість": 2, "вага": 39.5},
        9: {"кількість": 3, "вага": 44.0},
        10: {"кількість": 1, "вага": 24.5}
    }

    while True:
        print("\nМеню:")
        print("1 - Показати всі записи")
        print("2 - Додати запис")
        print("3 - Видалити запис")
        print("4 - Переглянути за відсортованими ключами")
        print("5 - Аналіз даних")
        print("0 - Вихід")

        choice = input("Оберіть дію: ")

        if choice == "1":
            print_all(baggage)
        elif choice == "2":
            add_record(baggage)
        elif choice == "3":
            delete_record(baggage)
        elif choice == "4":
            print_sorted(baggage)
        elif choice == "5":
            analyze_baggage(baggage)
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()

