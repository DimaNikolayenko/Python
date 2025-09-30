# -*- coding: utf-8 -*-

word = input("Введіть слово: ")

vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"

vowel_letters = ""
consonant_letters = ""

i = 0
while i < len(word):
    ch = word[i]
    if ch in vowels:
        vowel_letters = vowel_letters + ch + "\n"
    else:
        consonant_letters = consonant_letters + ch + "\n"
    i = i + 1

print("\nСлово:", word)

print("\nГолосні:")
print(vowel_letters)

print("Приголосні:")
print(consonant_letters)


