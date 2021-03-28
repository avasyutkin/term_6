from textwrap import wrap

π = [['c', '4', '6', '2', 'a', '5', 'b', '9', 'e', '8', 'd', '7', '0', '3', 'f', '1'],
     ['6', '8', '2', '3', '9', 'a', '5', 'c', '1', 'e', '4', '7', 'b', 'd', '0', 'f'],
     ['b', '3', '5', '8', '2', 'f', 'a', 'd', 'e', '1', '7', '4', 'c', '9', '6', '0'],
     ['c', '8', '2', '1', 'd', '4', 'f', '6', '7', '0', 'a', '5', '3', 'e', '9', 'b'],
     ['7', 'f', '5', 'a', '8', '1', '6', 'd', '0', '9', '3', 'e', 'b', '4', '2', 'c'],
     ['5', 'd', 'f', '6', '9', '2', 'c', 'a', 'b', '7', '8', '1', '4', '3', 'e', '0'],
     ['8', 'e', '2', '5', '6', '9', '1', 'c', 'f', '4', 'b', '0', 'd', 'a', '3', '7'],
     ['1', '7', 'e', 'd', '0', '5', '8', '3', '4', 'f', 'a', '6', '9', 'c', 'b', '2']]


def t(a):
    new_a = ''
    for i in range(len(a)):
        new_a += π[7 - i][int(a[i], 16)]

    return new_a

def g(k, a):
    new_a = '0' * (8 - len(hex((int(a, 16) + int(k, 16)) % 2 ** 32)[2:])) + hex((int(a, 16) + int(k, 16)) % 2 ** 32)[2:]
    new_a = t(new_a)
    new_a = '0' * (32 - len(bin(int(new_a, 16))[2:])) + bin(int(new_a, 16))[2:]
    new_a = hex(int(new_a[11:] + new_a[:11], 2))[2:]

    return new_a


def key_generation(K):
    K_ = generation_array(8,32)
    p = 0
    for i in range(len(K_)):
        K_[i] += K[p:p+8]
        p+=8
        if p == 64:
            p = 0

    K = K_[:24] + K_[24:][::-1]
    K = array_to_str8(K)

    return K


def encryption(a, K):
    K = key_generation(K)
    for i in range(31):
        a_ = a[1]
        a[1] = hex(int(a[0], 16) ^ int(g(K[i], a[1]), 16))[2:]
        a[0] = a_

    return hex(int(a[0], 16) ^ int(g(K[31], a[1]), 16))[2:] + a[1]


def decryption(a, K):
    K = key_generation(K)
    for i in range(31, 0, -1):
        a_ = a[1]
        a[1] = hex(int(a[0], 16) ^ int(g(K[i], a[1]), 16))[2:]
        a[0] = a_

    return hex(int(a[0], 16) ^ int(g(K[0], a[1]), 16))[2:] + a[1]


def generation_array(size1, size2):
    array = [[] * size1 for i in range(size2)]

    return array


def array_to_str8(input):
    input = array_to_str(input)
    input = wrap(input, 8)

    return input


def array_to_str(array):
    str = ''
    for i in range(len(array)):
        for j in range(len(array[i])):
            str += array[i][j]

    return str


K = 'ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'
a = ['fedcba98', '76543210']

encrypted_message = encryption(a, K)
print('Зашифрованное соообщение: ', encrypted_message)

a = wrap(encrypted_message, 8)
decrypted_message = decryption(a, K)
print('Расшифрованное сообщение: ', decrypted_message)




