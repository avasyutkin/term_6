sides = [[[0, 1], [1, 0], [1, 4], [1, 6], [1, 7], [2, 1], [2, 5], [2, 9], [3, 3], [3, 7], [4, 1], [5, 2], [5, 5], [5, 6], [5, 9]],
          [[0, 0], [0, 3], [0, 4], [0, 7], [1, 8], [2, 2], [2, 6], [3, 0], [3, 4], [3, 8], [4, 2], [4, 3], [4, 5], [4, 9], [5, 8]],
          [[0, 2], [0, 5], [0, 6], [0, 9], [1, 1], [2, 3], [2, 7], [3, 1], [3, 5], [3, 9], [4, 0], [4, 4], [4, 6], [4, 7], [5, 1]],
          [[0, 8], [1, 2], [1, 3], [1, 5], [1, 9], [2, 0], [2, 4], [2, 8], [3, 2], [3, 6], [4, 8], [5, 0], [5, 3], [5, 4], [5, 7]]]
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

import numpy as np
import random


def encryption(message):
    message_vector = [[' '] * 10 for i in range(6)]  # инициализируем матрицу (решетку)
    print(np.random.choice(alphabet, 1, True), 'пизда')
    k = 0
    for side in sides:  # заполняем решетку по координатам
        for i in range(len(side)):
            if k < len(message):
                message_vector[side[i][0]][side[i][1]] = message[k]
            else:
                message_vector[side[i][0]][side[i][1]] = str(np.random.choice(alphabet, 1, True))[2:-2]
            k = k + 1

    message_vector = np.array(message_vector)
    print(message_vector)

    message_encryption = array_in_str(message_vector)

    return message_encryption

def decryption(encrypted_message):
    message_vector = [[' '] * 10 for i in range(6)]
    messsage_decryption = ''
    k = 0

    for i in range(len(message_vector)):  # записываем сообщение в матрицу (решетку)
        for j in range(len(message_vector[i])):
            message_vector[i][j] = encrypted_message[k]
            k = k + 1

    for side in sides:  # выписываем расшифрованное сообщение по координатам
        for i in range(len(side)):
            messsage_decryption = messsage_decryption + message_vector[side[i][0]][side[i][1]]

    return messsage_decryption

def array_in_str(message_arr):  #  преобразовываем массив в строку, чтобы сообщение на выходе имело презентабельный вид
    message = ''
    for i in range(len(message_arr)):
        for j in range(len(message_arr[i])):
            message = message + message_arr[i][j]

    return message

message = input('Введите сообщение: ')

encrypted_message = encryption(message)
print('Зашифрованное сообщение: ', encrypted_message)

decrypted_message = decryption(encrypted_message)
print('Расшифрованное сообщение: ', decrypted_message)
