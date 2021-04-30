from textwrap import wrap


def encryption(message, key):
    message = message_to_code(message)
    encrypted_message = ''
    for symbol in message:
        if symbol == 1114:
            symbol = str('0' * (4 - len(str((int(symbol) + key) % 1114 - 1))) + str((int(symbol) + key) % 1114 - 1))
        else:
            symbol = str('0' * (4 - len(str((int(symbol) + key) % 1114))) + str((int(symbol) + key) % 1114))
        encrypted_message = encrypted_message + str(symbol)
    encrypted_message = code_to_message(encrypted_message)
    return encrypted_message


def decryption(encrypted_message, key):
    encrypted_message = message_to_code(encrypted_message)
    decrypted_message = ''
    for symbol in encrypted_message:
        if symbol == 0:
            symbol = str('0' * (4 - len(str((int(symbol) - key) % 1114 + 1))) + str((int(symbol) + key) % 1114 + 1))
        else:
            symbol = str('0' * (4 - len(str((int(symbol) - key) % 1114))) + str((int(symbol) - key) % 1114))
        decrypted_message = decrypted_message + str(symbol)
    decrypted_message = code_to_message(decrypted_message)
    return decrypted_message


def message_to_code(message):
    message_arr = []
    for i in message:
        message_arr.append('0' * (4 - len(str(ord(i)))) + str(ord(i)))

    return message_arr


def code_to_message(bin_message):
    bin_message = wrap(bin_message, 4)
    text = ''
    for i in bin_message:
        text += chr(int(i))

    return text


def validate(message, key, bool):
    if key.isnumeric():
        key = int(key) % 1114
        if bool == True:
            return encryption(message, key), str(key)
        else:
            return decryption(message, key), str(key)
    else:
        return 'Введите целое число от -1114 до 1114', key
