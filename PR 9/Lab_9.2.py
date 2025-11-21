import json

#Файл, у який збережемо початковий JSON
DATA_FILE = "baggage.json"
RESULT_FILE = "baggage_result.json"

#Початкові дані (10 пасажирів) 
passengers = [
    {"name": "Ivanov", "items": 3, "weight": 12.5},
    {"name": "Petrenko", "items": 1, "weight": 4.2},
    {"name": "Shevchenko", "items": 4, "weight": 30.0},
    {"name": "Melnyk", "items": 2, "weight": 6.0},
    {"name": "Koval", "items": 5, "weight": 2.8},
    {"name": "Bondarenko", "items": 1, "weight": 18.0},
    {"name": "Tkachenko", "items": 3, "weight": 26.0},
    {"name": "Kravets", "items": 2, "weight": 24.9},
    {"name": "Lysenko", "items": 3, "weight": 3.5},
    {"name": "Hrytsenko", "items": 4, "weight": 40.0}
]

#Запис початкових даних у JSON
with open(DATA_FILE, "w") as f:
    json.dump(passengers, f, indent=4)

#Функції 

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def show_data():
    data = load_data()
    print("\nВміст JSON файлу")
    for p in data:
        print(p)

def add_record():
    data = load_data()
    name = input("Прізвище: ")
    items = int(input("Кількість речей: "))
    weight = float(input("Вага багажу: "))
    data.append({"name": name, "items": items, "weight": weight})
    save_data(data)
    print("Запис додано!")

def delete_record():
    data = load_data()
    name = input("Введіть прізвище для видалення: ")
    data = [p for p in data if p["name"] != name]
    save_data(data)
    print("Запис видалено!")

def search_record():
    data = load_data()
    name = input("Введіть прізвище для пошуку: ")
    result = [p for p in data if p["name"] == name]
    print(result if result else "Запис не знайдено.")

def solve_task():
    data = load_data()

    #Пасажири з >2 речей
    more_items = [p["name"] for p in data if p["items"] > 2]

    #Вагові категорії
    less_5 = len([p for p in data if p["weight"] < 5])
    between = len([p for p in data if 5 <= p["weight"] <= 25])
    more_25 = len([p for p in data if p["weight"] > 25])

    result = {
        "more_than_two_items": more_items,
        "weight_categories": {
            "<5kg": less_5,
            "5-25kg": between,
            ">25kg": more_25
        }
    }

    with open(RESULT_FILE, "w") as f:
        json.dump(result, f, indent=4)

    print("Результат записано у", RESULT_FILE)

#Меню
while True:
    print("\nМЕНЮ")
    print("1 - Показати JSON")
    print("2 - Додати запис")
    print("3 - Видалити запис")
    print("4 - Пошук запису")
    print("5 - Виконати завдання")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        show_data()
    elif choice == "2":
        add_record()
    elif choice == "3":
        delete_record()
    elif choice == "4":
        search_record()
    elif choice == "5":
        solve_task()
    elif choice == "0":
        break
    else:
        print("Невірний вибір!")
