#alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '.', ',', '-', '!', '?', ':', ';', '—', ' ', '(', ')']

def encryption(message, encrypted_message):
    i = 1
    for symbol in message:
        symbol = (alphabet.index(symbol) + i) % 77
        encrypted_message = encrypted_message + alphabet[symbol]
        if i == len(alphabet) - 1:
            i = 1
        else:
            i = i + 1
    return encrypted_message

def decryption(encrypted_message, decrypted_message):
    i = 1
    for symbol in encrypted_message:
        symbol = (alphabet.index(symbol) - i) % 77
        decrypted_message = decrypted_message + alphabet[symbol]
        if i == len(alphabet) - 1:
            i = 1
        else:
            i = i + 1
    return decrypted_message
