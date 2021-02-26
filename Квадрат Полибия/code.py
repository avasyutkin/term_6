alphabet = [['а', 'б', 'в', 'г', 'д', 'е'],
            ['ж', 'з', 'и', 'й', 'к', 'л'],
            ['м', 'н', 'о', 'п', 'р', 'с'],
            ['т', 'у', 'ф', 'х', 'ц', 'ч'],
            ['ш', 'щ', 'ъ', 'ы', 'ь', 'э'],
            ['ю', 'я']]

"""
alphabet = [['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з'],
            ['и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р'],
            ['с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'],
            ['ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В'],
            ['Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К'],
            ['Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У'],
            ['Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
            ['Э', 'Ю', 'Я', '.', ',', '-', '!', '?', ':'],
            [';', '—', ' ', '(', ')']]
"""

def encryption(message, encrypted_message):
    for symbol in message:
        for i in range(len(alphabet)):
            for j in range(len(alphabet[i])):
                if alphabet[i][j] == symbol:
                    encrypted_message = encrypted_message + str(i+1)+str(j+1) + ' '
    return encrypted_message

def decryption(encrypted_message, decrypted_message):
    encrypted_message_array = encrypted_message.split()
    for symbol in encrypted_message_array:
        for i in range(len(alphabet)):
            for j in range(len(alphabet[i])):
                if str(i+1)+str(j+1) == symbol:
                    decrypted_message = decrypted_message + str(alphabet[i][j])
    return decrypted_message


message = input("Введите фразу: ")

encrypted_message = ''
encrypted_message = encryption(message, encrypted_message)

print(encrypted_message)

decrypted_message = ''
decrypted_message = decryption(encrypted_message, decrypted_message)

print(decrypted_message)