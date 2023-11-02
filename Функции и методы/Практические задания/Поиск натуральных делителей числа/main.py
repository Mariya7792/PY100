def get_list_number_divisors(number):
    list_ = []
    for i in range(1, number + 1):
        if number % i == 0:
            list_.append(i)

    return list_

print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))
