# Оптимізація виробництва

import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Drinks_Production", pulp.LpMaximize)

# Змінні рішення
# Кількість напоїв (цілі числа, не від'ємні)
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Функція цілі
# Максимізуємо загальну кількість вироблених напоїв
model += lemonade + juice, "Total_Drinks"

# Обмеження ресурсів

# Вода: 2 од. на лимонад, 1 од. на сік, всього 100
model += 2 * lemonade + 1 * juice <= 100, "Water_Constraint"

# Цукор: 1 од. тільки на лимонад, всього 50
model += 1 * lemonade <= 50, "Sugar_Constraint"

# Лимонний сік: 1 од. тільки на лимонад, всього 30
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"

# Фруктове пюре: 2 од. тільки на фруктовий сік, всього 40
model += 2 * juice <= 40, "Fruit_Puree_Constraint"

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Статус:", pulp.LpStatus[model.status])
print("Виробляти лимонаду:", lemonade.varValue)
print("Виробляти фруктового соку:", juice.varValue)
print("Загальна кількість напоїв:", lemonade.varValue + juice.varValue)
