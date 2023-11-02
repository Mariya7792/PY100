# TODO реализовать функцию
def remove_whitespace(phrase):
    res = []
    word = ""
    count = 0
    for char in phrase:
        if char != " ":
            word += char
            count += 1
        elif char == " " and count:
            res.append(word)
            word = ""
            count = 0
    # list_phrase = phrase.split()
    if word:
        res.append(word)
    final_string = ' '.join(res)

    # return final_string
    return final_string

str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))