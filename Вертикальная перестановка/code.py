import numpy as np

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

"""
def vector_initialization(message, key):  # подготавливаем векторы для заполнения
    print(message, 'message')
    if int(len(message) % len(key)) > 0:
        message_vector = [[0] * len(key) for i in range(int(len(message) / len(key)) + 1)]  # если длина сообщения не кратна размеру ключа, создаем дополнительный вектор, пустые значения в котором заполним пробелами
    else:
        message_vector = [[0] * len(key) for i in range(int(len(message) / len(key)))]

    return message_vector

def message_to_vector_dec(message_vector, message):  # заполняем векторы буквами исходного сообщения
    k = 0
    print(message_vector, 'мусещк')
    for i in range(len(message_vector)):
        for j in range(len(key)):
            if k < len(message):
                message_vector[j][i] = message[k]
            else:
                message_vector[j][i] = ' '  # если в векторе осталось место, а буквы в сообщении закончились, заполняем пробелами
            k = k + 1
    message_vector = np.array(message_vector)
    print(message_vector, 'messagevector')
    return message_vector

def message_to_vector_enc(message_vector, message):  # заполняем векторы буквами зашифрованного сообщения
    k = 0
    for i in range(len(key)):
        for j in range(len(message_vector)):
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
"""

def vector_initialization(message, key):  # подготавливаем векторы для заполнения
    if int(len(message) % len(key)) > 0:
        message_vector = [[0] * len(key) for i in range(int(len(message) / len(key)) + 1)]  # если длина сообщения не кратна размеру ключа, создаем дополнительный вектор, пустые значения в котором заполним пробелами
    else:
        message_vector = [[0] * len(key) for i in range(int(len(message) / len(key)))]

    return message_vector


def message_to_vector_enc(message_vector, message, key):  # заполняем векторы буквами исходного сообщения
    k = 0
    for i in range(len(message_vector)):
        for j in range(len(key)):
            if k < len(message):
                message_vector[i][j] = message[k]
            else:
                message_vector[i][j] = str(np.random.choice(alphabet, 1, True))[2:-2]  # если сообщение закончилось, заполняем рандомными буквами
            k = k + 1

    message_vector = np.array(message_vector)

    return message_vector


def message_to_vector_dec(message_vector, message, key):  # заполняем векторы буквами зашифрованного сообщения
    k = 0
    for i in range(len(key)):
        for j in range(len(message_vector)):
            if k < len(message):
                message_vector[j][i] = message[k]
            k = k + 1

    message_vector = np.array(message_vector)

    return message_vector

def encryption(message, key):
    key = permutation_indices(key)[0]
    print(message)
    message = message[:, key]  # осуществляем перестановку (шифрование) столбцов согласно порядку, который вернулся из функции permutation_indices
    print(message)
    message_str = ''
    for i in range(len(message[0])):
        for j in range(len(message)):
            message_str += message[j][i]  # записываем зашифрованное сообщение в строку, считывая по столбцам

    return message_str

def decryption(message, key):
    key = permutation_indices(key)[1]  # осуществляем перестановку (расшифрование) столбцов согласно порядку, который вернулся из функции permutation_indices
    message = message[:, key]
    message_str = ''
    for i in range(len(message)):
        for j in range(len(message[i])):
            message_str += message[i][j]  # записываем расшифрованное сообщение в строку

    return message_str

def permutation_indices(key):
    key_in_alphabet = []
    for i in key:
        key_in_alphabet.append(alphabet.index(i))  # индексы букв слова в alphabet

    key_in_alphabet_sort = sorted(key_in_alphabet)
    index_dec = []
    for i in key_in_alphabet:
            index_dec.append(key_in_alphabet_sort.index(i))  # индексы расставлены по возрастанию букв в порядке, согласно порядку букв в слове (а-0, б-1, в-2) (расшифрование)
    k = 1

    while [i for i in range(len(index_dec)) if not i == index_dec.index(index_dec[i])]:
        for j in [i for i in range(len(index_dec)) if not i == index_dec.index(index_dec[i])]:
            index_dec[j] = index_dec[j] + 1
            k += 1

    index_sort = []
    for i in index_dec:
        index_sort.append(index_dec.index(i))  # 1 2 3 4 5 ...

    index_enc = [0] * len(index_dec)  # индексы, задающие порядок столбцов при шифровании
    k = 0
    for i in index_dec:
        index_enc[i] = k
        k += 1

    return index_enc, index_dec

message = list(input('Введите сообщение: '))
key = input('Введите ключ: ')

encrypted_message = encryption(message_to_vector_enc(vector_initialization(message, key), message, key), key)
print('Зашифрованное сообщение: ', encrypted_message)

decrypted_message = decryption(message_to_vector_dec(vector_initialization(encrypted_message, key), encrypted_message, key), key)
print('Расшифрованное сообщение: ', decrypted_message)
