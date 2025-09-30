# -*- coding: utf-8 -*-

sentence = "Мова програмування Python дуже популярна"
words = sentence.split()

print("Речення:", sentence)
print("\nКількість літер у словах:")
for w in words:
    count = sum(1 for ch in w if ch.isalpha())  
    print(f"{w}: {count}")

