import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import io

#Спеціальне зчитування "складного" CSV файлу
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'Children.csv')
    
    #Читаємо файл як текст і виправляємо форматування (видаляємо зайві лапки)
    processed_lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            #Якщо рядок загорнутий у лапки, знімаємо їх
            if line.startswith('"') and line.endswith('"'):
                line = line[1:-1]
            #Замінюємо подвійні лапки "" на одинарні "
            line = line.replace('""', '"')
            processed_lines.append(line)
            
    #Створюємо DataFrame з очищеного тексту
    df = pd.read_csv(io.StringIO('\n'.join(processed_lines)))
    print("Файл Children.csv успішно завантажено!")
    
except FileNotFoundError:
    print("Помилка: Файл Children.csv не знайдено!")
    exit()
except Exception as e:
    print(f"Помилка при обробці файлу: {e}")
    exit()

#Обробка даних
#Конвертуємо 'Value' в числа (значення ".." стануть NaN)
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

# Видаляємо рядки без даних
df = df.dropna(subset=['Value'])

#Оскільки цей файл вже у "довгому" форматі, melt() робити НЕ ТРЕБА.
#Просто переконаємося, що Time - це число
df['Time'] = pd.to_numeric(df['Time'])

print("\nПерші 5 рядків очищених даних:")
print(df.head())

#Отримуємо назву показника для графіків
series_name = df['Series Name'].iloc[0] if not df.empty else "Показник"


#Розділення даних по країнах
ukraine_data = df[df["Country Name"] == 'Ukraine'].sort_values('Time')
france_data = df[df["Country Name"] == 'France'].sort_values('Time')

print(f"\nДані для України: {len(ukraine_data)} років")
print(f"Дані для Франції: {len(france_data)} років")

#Графік динаміки (Лінійний)
plt.figure(figsize=(12, 6))

if not ukraine_data.empty:
    plt.plot(ukraine_data['Time'], ukraine_data['Value'], marker='o', linewidth=2, label='Україна', color='blue')
if not france_data.empty:
    plt.plot(france_data['Time'], france_data['Value'], marker='s', linewidth=2, label='Франція', color='red')

plt.xlabel('Рік', fontsize=12)
plt.ylabel('Кількість дітей', fontsize=12)
plt.title(f'Динаміка: {series_name}', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("diagram1.png")

#Стовпчаста діаграма (Вибір країни)
def plot_country_bar_chart():
    print("\nДоступні країни: Ukraine, France")
    #country_name = input("Введіть назву країни: ").strip() # Можна розкоментувати для введення
    country_name = 'Ukraine' # Поки що автоматично
    print(f"Будуємо графік для: {country_name}")

    country_data = df[df['Country Name'] == country_name].sort_values('Time')
    
    if country_data.empty:
        print(f"Немає даних для {country_name}")
        return
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(country_data['Time'], country_data['Value'], color='orange', alpha=0.7)
    
    plt.xlabel('Рік', fontsize=12)
    plt.ylabel('Кількість дітей', fontsize=12)
    plt.title(f'{series_name} - {country_name}', fontsize=14)
    
    #Підписи значень (форматуємо як цілі числа з роздільниками тисяч)
    for bar, value in zip(bars, country_data['Value']):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                 f'{int(value):,}', ha='center', va='bottom', fontsize=8, rotation=45)
    
    plt.xticks(country_data['Time'], rotation=45)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig("diagram2.png")

plot_country_bar_chart()

#Порівняння за останній спільний рік
#Знаходимо останній рік, який є і в України, і у Франції
common_years = np.intersect1d(ukraine_data['Time'], france_data['Time'])

if len(common_years) > 0:
    last_year = max(common_years)
    print(f"\nПорівняння за останній спільний рік: {last_year}")
    
    last_year_data = df[(df['Time'] == last_year) & (df['Country Name'].isin(['Ukraine', 'France']))]
    
    plt.figure(figsize=(8, 6))
    bars = plt.bar(last_year_data['Country Name'], last_year_data['Value'], 
            color=['red' if x == 'France' else 'blue' for x in last_year_data['Country Name']])
            
    plt.title(f'Порівняння країн за {last_year} рік', fontsize=14)
    plt.ylabel('Кількість дітей')
    
    for bar, value in zip(bars, last_year_data['Value']):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                 f'{int(value):,}', ha='center', va='bottom', fontsize=12)
                 
    plt.grid(axis='y', alpha=0.3)
    plt.savefig("diagram3.png")
else:
    print("Немає спільних років для порівняння.")