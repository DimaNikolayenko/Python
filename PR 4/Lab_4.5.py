def count_vowels_set():
    text = input("Введіть текст (латинські літери та цифри): ").lower()
    vowels = set("aeiouy")
    
    try:
        text_set = set(text)
       
        found_vowels = text_set & vowels
        
        print("Голосні, які є у тексті:", found_vowels)
        print("Кількість голосних літер:", sum(ch in vowels for ch in text))
    
    except TypeError:
        text_list = list(text)
        result = [ch for ch in text_list if ch in vowels]
        print("Перетворено на множину:", set(result))

count_vowels_set()