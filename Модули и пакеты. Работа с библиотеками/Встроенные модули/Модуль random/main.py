import random

# Генерация случайного целого числа от 1 до 10
num1 = random.randint(1, 10)
print(num1)

# Генерация случайного вещественного числа от 0 до 1
num2 = random.random()
print(num2)

# Генерация случайного вещественного числа от 0.5 до 2.5
num3 = random.uniform(0.5, 2.5)
print(num3)

# Выбор случайного элемента из списка
fruits = ['apple', 'banana', 'orange']
random_fruit = random.choice(fruits)
print(random_fruit)
