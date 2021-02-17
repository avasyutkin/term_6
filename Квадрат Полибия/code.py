alphabet = [['а', 'б', 'в', 'г', 'д', 'е'],
            ['ж', 'з', 'и', 'й', 'к', 'л'],
            ['м', 'н', 'о', 'п', 'р', 'с'],
            ['т', 'у', 'ф', 'х', 'ц', 'ч'],
            ['ш', 'щ', 'ъ', 'ы', 'ь', 'э'],
            ['ю', 'я']]

def encryption(message, encrypted_message):
    for symbol in message:
        for i in range(len(alphabet)):
            for j in range(len(alphabet[i])):
                if alphabet[i][j] == symbol:
                    encrypted_message.append(str(i+1)+str(j+1))
    return encrypted_message

def decryption(encrypted_message, decrypted_message):
    for symbol in encrypted_message:
        for i in range(len(alphabet)):
            for j in range(len(alphabet[i])):
                if str(i+1)+str(j+1) == symbol:
                    decrypted_message.append(alphabet[i][j])
    return decrypted_message


message = input("Введите сообщение: ")

encrypted_message = []
encryption(message, encrypted_message)
print(encrypted_message)

decrypted_message = []
decryption(encrypted_message, decrypted_message)
print(decrypted_message)
