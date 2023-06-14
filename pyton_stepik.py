# объявление функции
def is_pangram(text):
    text = set(text)
    print(text, len(text))
    return len(text) >= 26

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))