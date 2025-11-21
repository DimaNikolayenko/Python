import numpy as np
import matplotlib.pyplot as plt

# Область визначення
x = np.linspace(1, 10, 500)

# Функція
y = 5 * np.sin(x) * np.cos(x**2 + 1/x)**2

# Побудова графіка
plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label='Y(x)')

# Підписи осей
plt.xlabel('x')
plt.ylabel('Y(x)')

# Назва графіка
plt.title('Графік функції Y(x) = 5*sin(x)*cos(x^2 + 1/x)^2')

# Легенда
plt.legend()

# Показати графік
plt.grid(True)
plt.savefig("graph.png")