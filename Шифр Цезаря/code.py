alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def encryption(message, encrypted_message):
    for symbol in message:
        symbol = (31 + alphabet.index(symbol) + 3) % 31
        encrypted_message.append(alphabet[symbol])
    return encrypted_message

def decryption(encrypted_message, decrypted_message):
    for symbol in encrypted_message:
        symbol = (31 + alphabet.index(symbol) - 3) % 31
        decrypted_message.append(alphabet[symbol])
    return decrypted_message


message = input("Введите фразу: ")

encrypted_message = []
encryption(message, encrypted_message)
print(encrypted_message)

decrypted_message = []
decryption(encrypted_message, decrypted_message)
print(decrypted_message)
