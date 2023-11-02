# TODO реализовать функцию
def get_unique_words(sentence):
    list_ = list(set(sentence.split()))
    list_.sort()

    return list_



print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
