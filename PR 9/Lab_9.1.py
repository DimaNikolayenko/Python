import pandas as pd

# Читання CSV
df = pd.read_csv("C:/Users/USER/Downloads/data.csv")
print("Файл успішно відкрито!\n")

# Вивід оригінального CSV
print("=== Вміст CSV-файлу ===")
print(df)

# Спрощення назв колонок (наприклад: 2010 [YR2010] → 2010)
new_cols = []
for col in df.columns:
    if "[YR" in col:
        new_cols.append(col.split()[0])
    else:
        new_cols.append(col)
df.columns = new_cols

# Роки, які будемо аналізувати
years = [str(y) for y in range(2010, 2020)]

# Фільтруємо тільки потрібні колонки
df_filtered = df[["Country Name"] + years]

# 👉 Перетворення значень у числові, щоб уникнути помилки "float vs str"
for year in years:
    df_filtered[year] = pd.to_numeric(df_filtered[year], errors='coerce')

# Пошук мінімальної та максимальної інфляції
results = []

for year in years:
    min_country = df_filtered.loc[df_filtered[year].idxmin(), "Country Name"]
    min_value = df_filtered[year].min()

    max_country = df_filtered.loc[df_filtered[year].idxmax(), "Country Name"]
    max_value = df_filtered[year].max()

    results.append([year, min_country, min_value, max_country, max_value])

# Запис результатів у CSV
result_df = pd.DataFrame(results, columns=[
    "Year", "Country", "Min Value", "Country", "Max Value"
])

result_df.to_csv("inflation_results.csv", index=False)
print("\nРезультат збережено у файл inflation_results.csv")
