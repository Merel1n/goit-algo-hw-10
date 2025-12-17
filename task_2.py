# Обчислення визначеного інтеграла

import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Кількість випадкових точок
N = 100_000

# Максимальне значення функції на відрізку [a, b]
f_max = f(b)

# Лічильник точок під кривою
M = 0

# Генерація випадкових точок
for _ in range(N):
    x_rand = random.uniform(a, b)
    y_rand = random.uniform(0, f_max)

    if y_rand <= f(x_rand):
        M += 1

# Площа прямокутника
rectangle_area = (b - a) * f_max

# Обчислення інтеграла методом Монте-Карло
integral_mc = (M / N) * rectangle_area

print(f"Інтеграл (Монте-Карло): {integral_mc}")

result, error = spi.quad(f, a, b)

print("Інтеграл (quad):", result)
print("Оцінка похибки:", error)