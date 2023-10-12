# Склеивание строк
words = ['Hello', 'World', 'Python']
result = ' '.join(words)
print(result)  # Hello World Python

# Разбиение строки по пробелам и любым непечатаемым символам
text = "Python is an amazing language"
words = text.split()
print(words)  # ['Python', 'is', 'an', 'amazing', 'language']

# Разбиение строки указанному разделителю
data = "apple,orange,banana"
fruits = data.split(',')
print(fruits)  # ['apple', 'orange', 'banana']

# Приведение первого символа строки к нижнему регистру, а остальных к нижнему
text = "hello, World"
result = text.capitalize()
print(result)  # Hello, world
