import numpy as np

def vector_initialization(message, key):  # подготавливаем векторы для заполнения
    if int(len(message) % len(key)) > 0:
        message_vector = [[0] * len(key) for i in range(int(len(message) / len(key)) + 1)]  # если длина сообщения не кратна размеру ключа, создаем дополнительный вектор, пустые значения в котором заполним пробелами
    else:
        message_vector = [[0] * len(key) for i in range(int(len(message) / len(key)))]

    return message_vector

def message_to_vector(message_vector):  # заполняем векторы буквами исходного сообщения
    k = 0
    for i in range(len(key)):
        for j in range(len(message_vector)):
            if k < len(message):
                message_vector[j][i] = message[k]
            else:
                message_vector[j][i] = ' '  # если в векторе осталось место, а буквы в сообщении закончились, заполняем пробелами
            k = k + 1
    message_vector = np.array(message_vector)

    print(message_vector)

    return message_vector

def encryption(message, key):
    k = 0
    message = np.array(message)

    for i in key:
        if i == '1':
            message[:, k] = list(reversed(message[:, k]))  # по умолчанию все столбцы направлены вниз, если в ключе встречается 1, столбец переворачивается
        k = k + 1
    print(message)
    message_encryption = array_in_str(message)

    return message_encryption

def decryption(message, key):
    k = 0

    message = np.array(message)
    message_encryption = []

    for i in key:
        message_encryption = message_encryption + (list(message[:, k]))
        k = k + 1

    message_decryption = array_in_str(message_encryption)

    return message_decryption

def array_in_str(message_arr):  #  преобразовываем массив в строку, чтобы сообщение на выходе имело презентабельный вид
    message = ''
    for i in range(len(message_arr)):
        for j in range(len(message_arr[i])):
            message = message + message_arr[i][j]

    return message


message = list(input('Введите сообщение: '))
key = input('Введите ключ (0 - направление вниз, 1 - вверх): ')

encrypted_message = encryption(message_to_vector(vector_initialization(message, key)), key)
print('Зашифрованное сообщение: ', encrypted_message)

decrypted_message = decryption(message_to_vector(vector_initialization(encrypted_message, key)), key)
print('Расшифрованное сообщение: ', decrypted_message)
