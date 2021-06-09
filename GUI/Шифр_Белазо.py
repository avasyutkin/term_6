alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '.', ',', '-', '!', '?', ':', ';', '—', '/', ' ', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encryption(message, key):
    encrypted_message = ''
    i = 0
    key_array = list(key)
    for symbol in message:
        symbol = (alphabet.index(symbol) + alphabet.index(key_array[i])) % 140
        encrypted_message = encrypted_message + alphabet[symbol]
        if i == len(key_array) - 1:
            i = 0
        else:
            i = i + 1
    return encrypted_message

def decryption(message, key):
    decrypted_message = ''
    i = 0
    key_array = list(key)
    for symbol in message:
        symbol = (alphabet.index(symbol) - alphabet.index(key_array[i])) % 140
        decrypted_message = decrypted_message + alphabet[symbol]
        if i == len(key_array) - 1:
            i = 0
        else:
            i = i + 1
    return decrypted_message


def validate(message, key, bool):
    for i in key:
        if i not in alphabet:
            key = key.replace(i, "")

    for i in message:
        if i not in alphabet:
            message = message.replace(i, "")

    if key == '':
        return 'Символы в ключе не поддерживаются кодировкой. Введите другой ключ.', key
    elif key == '':
        return 'Символы в сообщении не поддерживаются кодировкой.', key
    else:
        if bool == True:
            return encryption(message, key), str(key)
        else:
            return decryption(message, key), str(key)
