# TODO Напишите функцию decimal_to_hex
def decimal_to_hex(decimal_numbers):
    dict_compressed = {key:hex(key) for key in range(decimal_numbers)}

    return dict_compressed

if __name__ == '__main__':
    print(decimal_to_hex(16))
