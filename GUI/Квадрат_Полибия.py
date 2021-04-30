alphabet = [['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п'],
            ['р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А'],
            ['Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р'],
            ['С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '.', ','],
            ['-', '!', '?', ':', ';', '—', '/', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8'],
            ['9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],
            ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
            ['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'],
            ['Y', 'Z']]


def encryption(message):
    new_message = ''
    for symbol in message:
        for i in range(len(alphabet)):
            for j in range(len(alphabet[i])):
                if alphabet[i][j] == symbol:
                    new_message = new_message + str(i+1)+str(j+1) + ' '
    return new_message


def decryption(encrypted_message):
    new_message = ''
    encrypted_message_array = encrypted_message.split()
    for symbol in encrypted_message_array:
        for i in range(len(alphabet)):
            for j in range(len(alphabet[i])):
                if str(i+1)+str(j+1) == symbol:
                    new_message = new_message + str(alphabet[i][j])
    return new_message

