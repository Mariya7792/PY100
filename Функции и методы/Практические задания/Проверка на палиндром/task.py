# TODO Напишите функцию `is_palindrome`
def is_palidrome(phrase):
    phrase1 = phrase.lower().split()
    phrase2 = ''.join(phrase1)[::-1]
    if phrase2.lower() == phrase.lower():
        return True
    return False
