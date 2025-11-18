import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import string

#Завантажуємо потрібні ресурси NLTK
nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('stopwords')

#Вибираємо текст для аналізу
text_id = 'milton-paradise.txt'
words = gutenberg.words(text_id)

print("=== Аналіз тексту з архіву Gutenberg ===")
print("Текст:", text_id)

#Кількість слів у тексті
total_words = len(words)
print("\n1) Кількість слів у тексті:", total_words)

#Частотний аналіз без очищення (сирий текст)
fdist_raw = FreqDist(words)
top10_raw = fdist_raw.most_common(10)

print("\n2) Топ-10 слів (сирий текст):")
for w, c in top10_raw:
    print(w, ":", c)
    
#Побудова графіка для сирого тексту
raw_words = [w for w, c in top10_raw]
raw_counts = [c for w, c in top10_raw]

plt.bar(raw_words, raw_counts)
plt.title("Топ-10 слів (сирий текст)")
plt.xticks(rotation=40)
plt.tight_layout()
plt.savefig("diagram_raw.png")

#Очищення тексту: прибираємо стоп-слова та пунктуацію
stop_words = set(stopwords.words("english"))
punct = set(string.punctuation)

clean_words = []

for w in words:
    w_low = w.lower()
    if w_low.isalpha() and w_low not in stop_words:
        clean_words.append(w_low)

#Аналіз очищеного тексту
fdist_clean = FreqDist(clean_words)
top10_clean = fdist_clean.most_common(10)

print("\n3) Топ-10 слів після очищення:")
for w, c in top10_clean:
    print(w, ":", c)

#Побудова графіка для очищеного тексту
clean_labels = [w for w, c in top10_clean]
clean_counts = [c for w, c in top10_clean]

plt.figure()
plt.bar(clean_labels, clean_counts)
plt.title("Топ-10 слів (очищений текст)")
plt.xticks(rotation=40)
plt.tight_layout()
plt.savefig("diagram_clean.png")
