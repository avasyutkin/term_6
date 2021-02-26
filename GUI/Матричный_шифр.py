import sys
import numpy as np

alphabet = [' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '.', ',', '-', '!', '?', ':', ';', '—', '(', ')']

def message_to_index(message):
    message_1 = []

    for i in message:
        message_1.append(alphabet.index(i))
    return message_1

def message_to_vector(message, key):
    if int(len(message) % int(key[0])) > 0:
        message_vector = [[0] * int(key[0]) for i in range(int(len(message) / int(key[0])) + 1)]
    else:
        message_vector = [[0] * int(key[0]) for i in range(int(len(message) / int(key[0])))]

    k = 0
    for i in range(len(message_vector)):
        for j in range(int(key[0])):
            if k < len(message):
                message_vector[i][j] = message[k]
            else:
                message_vector[i][j] = 0
            k = k + 1

    return message_vector


def key_generation(key):
    key_matrix = [[0] * int(key[0]) for i in range(int(key[0]))]

    k = 1
    for i in range(int(key[0])):
        for j in range(int(key[0])):
            key_matrix[i][j] = key[k]
            k = k + 1
    key_matrix = np.array(key_matrix)

    return key_matrix

def matrix_check(matrix):

    if int(np.linalg.det(matrix)) == 0:
        matrix = 'Введенный ключ не подходит для шифрования, введите другой.'

    return matrix

def encryption(message, key):
    encrypted_message = list()
    for i in message:
        for j in range(len(key)):
            encrypted_message.append(key.dot(i)[j])
    encrypted_message = str(encrypted_message)[1: -1]
    return encrypted_message

def decryption(encrypted_message, key):
    decrypted_message = ''

    for i in range(len(encrypted_message)):
        for j in range(len(encrypted_message[i])):
            encrypted_message[i][j] = int(encrypted_message[i][j])

    key_1 = [[0]*len(key) for i in range(len(key))]
    a = np.linalg.det(key)
    for i in range(len(key)):
        for j in range(len(key)):
            key_1[i][j] = ((-1)**(i+j))*minor_of_element(key, i, j)

    key_1 = np.array(key_1).transpose()

    for i in encrypted_message:
        for j in range(len(key)):
            decrypted_message = decrypted_message + alphabet[(int(int((key_1).dot(i)[j])/int(a)))]

    return decrypted_message

def minor_of_element(A, i, j):
    sub_A = np.delete(A, i, 0)
    sub_A = np.delete(sub_A, j, 1)
    M_ij = np.linalg.det(sub_A)

    return np.around(M_ij, decimals=3)

def key_to_array(key):
    key = list(map(int, key.split()))

    return key

def str_to_list(str):
    str = str.split(', ')

    return str

