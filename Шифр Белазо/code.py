alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def encryption(message, encrypted_message, key):
    i = 0
    key_array = list(key)
    for symbol in message:
        symbol = (alphabet.index(symbol) + alphabet.index(key_array[i])) % 32
        encrypted_message = encrypted_message + alphabet[symbol]
        if i == len(key_array) - 1:
            i = 0
        else:
            i = i + 1
    return encrypted_message

def decryption(encrypted_message, decrypted_message, key):
    i = 0
    key_array = list(key)
    for symbol in encrypted_message:
        symbol = (alphabet.index(symbol) - alphabet.index(key_array[i])) % 32
        decrypted_message = decrypted_message + alphabet[symbol]
        if i == len(key_array) - 1:
            i = 0
        else:
            i = i + 1
    return decrypted_message


message = input('Введите сообщение: ')

encrypted_message = ''
key = input('Введите ключ: ')
encrypted_message = encryption(message, encrypted_message, key)

print(encrypted_message)

decrypted_message = ''
decrypted_message = decryption(encrypted_message,decrypted_message, key)
print(decrypted_message)

