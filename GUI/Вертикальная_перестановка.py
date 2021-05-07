import numpy as np

def vector_initialization(message, key):  # подготавливаем векторы для заполнения
    if int(len(message) % len(key)) > 0:
        message_vector = [[0] * len(key) for i in range(int(len(message) / len(key)) + 1)]  # если длина сообщения не кратна размеру ключа, создаем дополнительный вектор, пустые значения в котором заполним пробелами
    else:
        message_vector = [[0] * len(key) for i in range(int(len(message) / len(key)))]

    return message_vector

def message_to_vector_enc(message_vector, message, key):  # заполняем векторы буквами исходного сообщения
    k = 0

    for i in range(len(key)):
        for j in range(len(message_vector)):
            if k < len(message):
                message_vector[j][i] = message[k]
            else:
                message_vector[j][i] = ' '  # если в векторе осталось место, а буквы в сообщении закончились, заполняем пробелами
            k = k + 1
    message_vector = np.array(message_vector)
    return message_vector

def message_to_vector_dec(message_vector, message, key):  # заполняем векторы буквами зашифрованного сообщения
    k = 0
    for i in range(len(message_vector)):
        for j in range(len(key)):
            if k < len(message):
                message_vector[i][j] = message[k]
            else:
                message_vector[i][j] = ' '
            k = k + 1

    message_vector = np.array(message_vector)

    return message_vector

def encryption(message, key):
    k = 0
    message = np.array(message)

    for i in key:
        if i == '1':
            message[:, k] = list(reversed(message[:, k]))  # по умолчанию все столбцы направлены вниз, если в ключе встречается 1, столбец переворачивается
        k = k + 1

    message_encryption = array_in_str(message)

    return message_encryption

def decryption(encryption_message, key):
    k = 0

    message = np.array(encryption_message)
    message_decryption_str = ''
    message_decryption = []

    for i in key:
        if i == '1':
            message_decryption.append(list(reversed(message[:, k])))
        else:
            message_decryption.append(list(message[:, k]))
        k = k + 1

    for i in message_decryption:
        for j in i:
            message_decryption_str = message_decryption_str + j

    return message_decryption_str

def array_in_str(message_arr):  #  преобразовываем массив в строку, чтобы сообщение на выходе имело презентабельный вид
    message = ''
    for i in range(len(message_arr)):
        for j in range(len(message_arr[i])):
            message = message + message_arr[i][j]

    return message
