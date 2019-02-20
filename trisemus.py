from collections import OrderedDict


def offset():
    return 9  # Почему так? Потому что табличка в методичке. Можно сделать функцию.


alphabet = set(["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"])
marks = [".", " ", ",", "!"]

print("Шифр Трисемуса")
key = list(OrderedDict.fromkeys((input("Введите ключ:\n"))))
message = input("Введите сообщение:\n")
cryptotable = (key + sorted(alphabet - set(key))) + marks
print(cryptotable)

cryptogram = ""
for char in message:
    crypted_char = cryptotable[(cryptotable.index(char) + offset()) % len(cryptotable)]
    cryptogram += crypted_char
print(cryptogram)
