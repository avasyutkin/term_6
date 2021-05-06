import numpy as np
import math
import random

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '.', ',', '-', '!', '?', ':', ';', '—', ' ', '(', ')']

def key_generation(len_message):  # генерация решетки
    key_size = int(math.sqrt(len_message)) + int((4 - int(math.sqrt(len_message)) % 4))  # исходя из длины текста вычитываем размер матрицы, в которой будет шифроваться
    message_vector = [[[' ' for i in range(int(key_size/2))] for j in range(int(key_size/2))] for k in range(4)]  # инициализируем матрицу

    k = 1
    for i in range(len(message_vector[0])):  # заполняем четыре части матрицы одинаковыми числами
        for j in range(len(message_vector[0][i])):
            message_vector[0][i][j] = k
            message_vector[1][i][j] = k
            message_vector[2][i][j] = k
            message_vector[3][i][j] = k
            k += 1

    message_vector = np.array(message_vector)
    message_vector[1] = np.rot90(np.rot90(np.rot90(message_vector[0])))  # крутим каждую из частей таким образом, чтобы единицы были в углах
    message_vector[2] = np.rot90(np.rot90(message_vector[1]))
    message_vector[3] = np.rot90(message_vector[2])

    matrix = []
    for i in range(len(message_vector)):  # соединяем четыре матрицы в одну
        for j in range(len(message_vector[0])):
            if i < len(message_vector)-1:
                if i % 2 == 0:
                    matrix.append(message_vector[i][j])
                    matrix.append(message_vector[i+1][j])

    matrix = np.array(matrix)
    matrix = matrix.reshape(key_size, key_size)

    nonrepeating_array = []
    key = []
    while len(nonrepeating_array) != message_vector[3][0][0]:  # генерируем координаты для ключа
        x = np.random.randint(0, len(matrix))
        y = np.random.randint(0, len(matrix))
        if matrix[x, y] in nonrepeating_array:
            continue
        else:
            key.append([x,y])
            nonrepeating_array.append(matrix[x, y])

    return matrix, key

def encryption(message):
    key = key_generation(len(message))  # получаем координаты
    message_vector = [[' '] * len(key[0]) for i in range(len(key[0]))]  # инициализируем матрицу (решетку)
    message_vector = np.array(message_vector)

    k = 0
    for i in range(4):  # заполняем решетку по координатам
        for j in range(len(key[1])):
            if k < len(message):
                message_vector[key[1][j][0]][key[1][j][1]] = message[k]
            else:
                message_vector[key[1][j][0]][key[1][j][1]] = str(np.random.choice(alphabet, 1, True))[2:-2]
            k = k + 1

        message_vector = np.rot90(message_vector)  # переворачиваем матрицу

    key_str = ''

    for i in key[1]:  # преобразовываем координаты в строку для вывода
        for j in i:
            key_str = key_str + str(j) + ' '

    message_encryption = array_in_str(message_vector)

    return message_encryption, key_str

def decryption(encrypted_message, key):
    key_ = list(key.split())
    for i in key_:
        if not i.isnumeric():
            return 'Введите последовательность чисел через пробел'

    key = key.split(' ')
    key_array = [[' '] * 2 for i in range(int((len(key)-1)/2))]

    k = 0
    for i in range(len(key_array)):  # преобразовываем строку с ключом в массив с координатами
        for j in range(len(key_array[i])):
            key_array[i][j] = key[k]
            k += 1

    message_vector = [[' '] * int(math.sqrt(len(encrypted_message))) for i in range(int(math.sqrt(len(encrypted_message))))]
    message_vector = np.array(message_vector)
    messsage_decryption = ''

    k = 0
    for i in range(len(message_vector)):  # записываем сообщение в матрицу (решетку)
        for j in range(len(message_vector[i])):
            message_vector[i][j] = encrypted_message[k]
            k = k + 1

    for k in range(4):  # выписываем расшифрованное сообщение по координатам
        for i in range(len(key_array)):
            messsage_decryption = messsage_decryption + message_vector[int(key_array[i][0])][int(key_array[i][1])]
        message_vector = np.rot90(message_vector)  # переворачиваем решетку

    return messsage_decryption


def array_in_str(message_arr):  # преобразовываем массив в строку, чтобы сообщение на выходе имело презентабельный вид
    message = ''
    for i in range(len(message_arr)):
        for j in range(len(message_arr[i])):
            message = message + message_arr[i][j]

    return message


