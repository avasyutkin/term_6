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
    K = str_to_hex(K)[:64]
    K = key_generation(K)
    a = message_completion(a)
    print(a)

    new_a = ''
    for i in range(len(a)):
        for j in range(len(a[i])):
            new_a += a[i][j]

    a = wrap(new_a, 8)
    for p in range(0, len(a), 2):
        for i in range(31):
            a_ = a[p+1]
            a[p+1] = hex(int(a[p], 16) ^ int(g(K[i], a[p+1]), 16))[2:]
            a[p] = a_
            #print(a)
    print(a)
    a_=''
    for i in range(0, len(a), 2):
        a_ += hex(int(a[i], 16) ^ int(g(K[31], a[i+1]),16))[2:] + a[i+1]

    print(len(a_))
    return a_
    #return hex(int(a[0], 16) ^ int(g(K[31], a[1]), 16))[2:] + a[1]


def decryption(a, K):
    K = str_to_hex(K)[:64]
    K = key_generation(K)
    print('Зашифрованное сообщение:', a, 'gfgd')
    new_a = ''
    for i in range(len(a)):
        for j in range(len(a[i])):
            new_a += a[i][j]

    a = wrap(new_a, 8)
    for p in range(0, len(a), 2):
        for i in range(31, 0, -1):
            print(a[p], a[p + 1])
            a_ = a[p+1]
            a[p+1] = hex(int(a[p], 16) ^ int(g(K[i], a[p+1]), 16))[2:]
            a[p] = a_
            print(a[p], a[p+1])
    a_ = ''
    for i in range(0, len(a), 2):
        a_+=hex(int(a[i], 16) ^ int(g(K[0], a[i+1]),16))[2:] + a[i+1]

    print(a)
    a_ = hex_to_str(a_)
    return a_


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


def str_to_hex(a):
    a_ = ''
    for i in a:
        a_ += '0' * (4 - len(hex(ord(i))[2:])) + hex(ord(i))[2:]

    return a_


def message_completion(a):
    a = str_to_hex(a)
    a = wrap(a, 32)

    if len(a[len(a)-1]) < 32:
        a[len(a)-1] += '1' + '0' * (31 - len(a[len(a)-1]))

    return a


def hex_to_str(a):
    a_=''
    a = a.rstrip('0')
    a = a[:len(a)-1]
    a = wrap(a,4)

    for i in range(len(a)):
        a_ += chr(int(a[i], 16))

    return a_


#K = 'ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'
#a = ['fedcba98', '76543210']

a = input('Введите сообщение: ')
K = input('Введите ключ (минимум 9 символов): ')
a = 'невсекотумасленицазптбудетивеликийпосттчк'
K = 'ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'

#a = wrap(a, 8)
enc = encryption(a, K)
print('Зашифрованное сообщение:', enc)
print(len(enc))
#enc = wrap(enc, 8)
dec = decryption(enc, K)
print('Расшифрованное сообщение:', dec)
