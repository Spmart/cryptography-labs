print("Шифр Гронсфельда")
key = list(input("Введите ключ:\n"))
message = list(input("Введите сообщение:\n"))
alphabet = list(["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"])
cryptogram = ""
for i in range(len(message)):
    offset = int(key[i % len(key)])
    char_index = alphabet.index(message[i])
    cryptogram += alphabet[(char_index - offset) % len(alphabet)]
print(cryptogram)