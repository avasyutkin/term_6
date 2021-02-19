alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

#alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '.', ',', '-', '!', '?', ':', ';', '—', ' ', '(', ')']

def encryption(message, encrypted_message, key):
    for symbol in message:
        if alphabet.index(symbol) == 31:
            symbol = (alphabet.index(symbol) + int(key)) % 31 - 1
        else:
            symbol = (alphabet.index(symbol) + int(key)) % 31   # для расширенного алфавита - 76
        encrypted_message = encrypted_message + str(alphabet[symbol])
    return encrypted_message

def decryption(encrypted_message, decrypted_message, key):
    for symbol in encrypted_message:
        if alphabet.index(symbol) == 0:
            symbol = (alphabet.index(symbol) - int(key)) % 31 + 1
        else:
            symbol = (alphabet.index(symbol) - int(key)) % 31   # для расширенного алфавита - 76
        decrypted_message = decrypted_message + str(alphabet[symbol])
    return decrypted_message
