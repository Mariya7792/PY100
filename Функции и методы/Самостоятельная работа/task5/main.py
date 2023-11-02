# TODO реализовать функцию
def get_sentences_list(text):
    string = text.strip()
    list_ = string.split('.')
    list_2 = []
    for char in list_:
        if char != '':
            list_2.append(char)
    list_2[1] = list_2[1][1:]
    return list_2

print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
