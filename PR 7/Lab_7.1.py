import random
import string

def Open(file_name, mode):
    """Функція безпечного відкриття файлу з обробкою помилок"""
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("Файл", file_name, "не вдалося відкрити!")
        return None
    else:
        print("Файл", file_name, "успішно відкрито в режимі", mode)
        return file


# --- а) Створюємо текстовий файл TF26_1.txt ---
file1_name = "TF26_1.txt"
file2_name = "TF26_2.txt"

file_1_w = Open(file1_name, "w")

if file_1_w is not None:
    # Створюємо 10 рядків випадкових латинських букв різної довжини (від 5 до 15)
    for _ in range(10):
        length = random.randint(5, 15)
        random_string = ''.join(random.choices(string.ascii_letters, k=length))
        file_1_w.write(random_string + "\n")

    print("Дані успішно записані у TF26_1.txt")
    file_1_w.close()
    print("Файл TF26_1.txt закрито.")


# --- б) Зчитуємо TF26_1, перетворюємо великі літери на малі, записуємо у TF26_2 ---
file_1_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_1_r is not None and file_2_w is not None:
    for line in file_1_r:
        lowercase_line = line.lower()
        file_2_w.write(lowercase_line)

    file_1_r.close()
    file_2_w.close()
    print("Дані з TF26_1.txt перетворені та записані у TF26_2.txt")


# --- в) Зчитуємо TF26_2 і виводимо по рядках ---
print("\nВміст файлу TF26_2.txt:")
file_3_r = Open(file2_name, "r")

if file_3_r is not None:
    for line in file_3_r:
        print(line.strip())
    file_3_r.close()
    print("Файл TF26_2.txt закрито.")
