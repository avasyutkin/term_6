from textwrap import wrap
import numpy as np

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я']

def before_processing(message, key):  # предобработка
    message = list(message)
    new_message = ''
    i = -1

    for symbol in message:
        if symbol == message[i]:
            new_message = new_message + 'ф' + symbol  # ставим 'ф' между двумя повторяющимися буквами
        else:
            new_message = new_message + symbol
        i = i + 1

    if len(new_message) % 2 != 0:
        new_message = new_message + 'ф'  # если число букв во фразе нечетно, в конец ставим 'ф'

    new_message = letter_to_index(new_message, key)

    return new_message

def letter_to_index(message, key):
    key = key_generation(key)
    new_message = wrap(message, 2)  # разбиваем фразу на биграммы

    message = ''
    for symbol in new_message:
        for sym in symbol:
            for i in range(len(key)):
                for j in range(len(key[i])):
                    if sym == key[i][j]:
                        message = message + str(i) + str(j)  # создаем строку из порядковых номеров в матрице-ключе букв исходной фразы

    return message

def index_to_letter(message, key):
    key = key_generation(key)
    new_message = ''
    message = wrap(message, 2)  # разбиваем эту строку на биграммы, соответствующие позициям каждой буквы

    for i in message:
        for o in range(len(key)+1):
            for j in range(len(key)+1):
                if i == str(o)+str(j):
                    new_message = new_message + key[o][j]  # заменяем номера позиций на буквы и получаем зашифрованное/расшифрованное сообщение

    return new_message


def encryption(message, key):
    encrypted_message = ''
    message = wrap(message, 4)  # делим строку на строки по 4 символа (по две цифры для каждой буквы биграммы)

    for i in message:  # в цикле осуществляем преобразования для шифрования
        i = wrap(i, 1)
        if i[0] == i[2]:  # если две буквы биграммы в одной строке, перемещаем их право на одну позицию
            i[1] = (int(i[1]) + 1) % 6
            i[3] = (int(i[3]) + 1) % 6
        elif i[1] == i[3]:  # если две буквы биграммы в одном столбце, перемещаем их вниз на одну позицию
            i[0] = (int(i[0]) + 1) % 5
            i[2] = (int(i[2]) + 1) % 5

        else:  # если буквы в одной биграмме расположены в разных строках и столбцах
            _i = i[3]
            i[3] = i[1]
            i[1] = _i

        encrypted_message = encrypted_message + str(i[0]) + str(i[1]) + str(i[2]) + str(i[3])  # создаем строку с позициями букв в зишифрованном сообщении

    encrypted_message = index_to_letter(encrypted_message, key)


    return encrypted_message

def decryption(encrypted_message, key):
    decrypted_message = ''
    message = letter_to_index(encrypted_message, key)
    message = wrap(message, 4)

    for i in message:
        i = wrap(i, 1)
        if i[0] == i[2]:  # если две буквы биграммы в одной строке, перемещаем их влево на одну позицию
            i[1] = (int(i[1]) - 1) % 6
            i[3] = (int(i[3]) - 1) % 6
        elif i[1] == i[3]:  # если две буквы биграммы в одном столбце, перемещаем их вверх на одну позицию
            i[0] = (int(i[0]) - 1) % 5
            i[2] = (int(i[2]) - 1) % 5
        else:  # если буквы в одной биграмме расположены в разных строках и столбцах
            m = i[3]
            i[3] = i[1]
            i[1] = m
        decrypted_message = decrypted_message + str(i[0]) + str(i[1]) + str(i[2]) + str(i[3])

    decrypted_message = index_to_letter(decrypted_message, key)

    return decrypted_message

def key_generation(key):
    key_set = set()
    key = [x for x in list(key) + alphabet if not (x in key_set or key_set.add(x))]  # создание массива ключ+оставишиеся буквы алфавита (без повторов)
    key_matrix = [[0]*6 for i in range(5)]  # создние n-мерного массива для записи в него ключа
    k = 0
    for i in range(5):
        for j in range(6):
            key_matrix[i][j] = key[k]
            k = k + 1
    return key_matrix

"""
message = list(input('Введите сообщение: '))
key = input('Введите ключ: ')

print('Ваш ключ: \n', np.array(key_generation(key)))

encrypted_message = encryption(before_processing(message, key), key)
print('Зашифрованное сообщение: ', encrypted_message)

decrypted_message = decryption(encrypted_message, key)
print('Расшифрованное сообщение: ', decrypted_message)

"""