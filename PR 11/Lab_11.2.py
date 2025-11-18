import pandas as pd
import matplotlib.pyplot as plt

# Встановлюємо стиль графіка та розмір фігури
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 5)
#Завантаження CSV файлу
try:
    df = pd.read_csv("comptagevelo2010.csv", encoding="latin1", parse_dates=["Date"], dayfirst=True, index_col="Date")
except:
    df = pd.read_csv("comptagevelo2010.csv", sep=";", encoding="latin1", parse_dates=["Date"], dayfirst=True, index_col="Date")
#Перевірка даних
print(df.head())
print(df.info())
print(df.describe())

#Вибір числових стовпців та заповнення пропусків нулями
df_num = df.select_dtypes(include=["int64", "float64"]).fillna(0)
#Загальна кількість велосипедистів за рік
total_year = df_num.sum().sum()
print("\nЗагальна кількість велосипедистів за рік:", total_year)
#Кількість велосипедистів за рік на кожній доріжці
total_per_lane = df_num.sum().sort_values(ascending=False)
print("\nКількість велосипедистів на кожній доріжці:")
print(total_per_lane)
#Топ-3 доріжки за популярністю
top3 = total_per_lane.head(3).index.tolist()
monthly = df_num[top3].groupby(df.index.month_name()).sum()

for lane in top3:
    month = monthly[lane].idxmax()
    value = monthly[lane].max()
    print(f"\nДоріжка {lane}: популярний місяць — {month} ({value})")
#Графік для однієї доріжки
lane_plot = top3[0]
monthly_lane = df_num[lane_plot].groupby(df.index.month_name()).sum()

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
monthly_lane = monthly_lane.reindex(month_order)

monthly_lane.plot(kind="bar", color="skyblue")
plt.title(f'Завантаженість доріжки "{lane_plot}" по місяцях')
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.7)
plt.tight_layout()
plt.savefig("diagram.png")

