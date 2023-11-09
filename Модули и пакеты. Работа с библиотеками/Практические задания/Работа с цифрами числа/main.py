number = 2342354235235

list_digits = [int(num) for num in str(number)]


print(sum(list_digits))
print(sum([num for num in list_digits if num % 2 ==0]))
print(len(list_digits))
print(min(list_digits))  # TODO найти минимальную цифру
print(list_digits[0] - list_digits[-1])  # TODO найти разность между первой и последней цифрой
