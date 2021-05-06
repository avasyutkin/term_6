import sys
import numpy as np

alphabet = [' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def message_to_index(message):  # преобразовываем введенное сообщение (строку) в массив чисел, соответствующих порядковому номеру каждой буквы
    message_1 = []
    for i in message:
        message_1.append(alphabet.index(i))
    return message_1


def message_to_vector(message, key):  # разделяем массив с порядковыми номерами букв на массив с векторами (длинны, равной размеру ключа-матрицы)
    if int(len(message) % key[0]) > 0:
        message_vector = [[0] * key[0] for i in range(int(len(message) / key[0]) + 1)]  # если длина сообщения не кратна размеру ключа, создаем дополнительный вектор, пустые значения в котором заполним пробелами
    else:
        message_vector = [[0] * key[0] for i in range(int(len(message) / key[0]))]

    k = 0
    for i in range(len(message_vector)):
        for j in range(key[0]):
            if k < len(message):
                message_vector[i][j] = message[k]  # распределяем числа по векторам
            else:
                message_vector[i][j] = 0  # если в векторе осталось место, а числа закончились, заполняем нулями
            k = k + 1

    return message_vector


def key_generation(key):   # генерируем матрицу из ключа, который ввел пользователь
    key_matrix = [[0] * key[0] for i in range(key[0])]
    print(key)

    k = 1
    for i in range(key[0]):
        for j in range(key[0]):
            key_matrix[i][j] = key[k]
            k = k + 1

    key_matrix = np.array(key_matrix)

    if int(np.linalg.det(key_matrix)) == 0:  # если определитель матрицы равен нулю, завершаем работу программы
        print('Введенный ключ не подходит для шифрования, введите другой.')
        sys.exit(0)

    return key_matrix

def encryption(message, key):  # шифруем наше сообщение путем перемножения ключа на векторы с порядковыми номерами
    encrypted_message = list()
    print('Матрица-ключ:  \n', key)
    for i in message:
        for j in range(len(key)):
            encrypted_message.append(key.dot(i)[j])

    return encrypted_message

def decryption(encrypted_message, key):
    print('pizda', encrypted_message)
    decrypted_message = ''
    key_1 = [[0]*len(key) for i in range(len(key))]
    a = np.linalg.det(key)  # считаем определитель
    for i in range(len(key)):
        for j in range(len(key)):
            key_1[i][j] = ((-1)**(i+j))*minor_of_element(key, i, j)  # находим элементы для присоединенной матрицы

    key_1 = np.array(key_1).transpose()  # транспонируем присоединенную матрицу
    print('Транспонированная матрица: \n', key_1)
    for i in encrypted_message:
        for j in range(len(key)):
            decrypted_message = decrypted_message + alphabet[(int(int((key_1).dot(i)[j])/int(a)))]  # вычисляем обратную матрицу и ее на векторы зашифрованного сообщения

    return decrypted_message

def minor_of_element(A, i, j):  # всопомогательная функция для нахождения минора каждого элемента матрицы
    sub_A = np.delete(A, i, 0)
    sub_A = np.delete(sub_A, j, 1)
    M_ij = np.linalg.det(sub_A)

    return np.around(M_ij, decimals=3)

message = list(input('Введите сообщение: '))
key = list(map(int, input('Введите размерность ключа и элементы его элементы через пробел: ').split()))

encrypted_message = encryption(message_to_vector(message_to_index(message), key), key_generation(key))
print('Зашифрованное сообщение: ', encrypted_message)

decrypted_message = decryption(message_to_vector(encrypted_message, key), key_generation(key))
print('Расшифрованное сообщение: ', decrypted_message)