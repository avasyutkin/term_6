from textwrap import wrap
from pyfinite import ffield
import sys

π = [252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233, 119, 240, 219, 147, 46,
     153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142,
     79, 5, 132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44, 81, 234, 200, 72, 171,
     242, 42, 104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156, 183, 93, 135, 21,
     161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177, 50, 117, 25, 61, 255, 53, 138, 126,
     109, 84, 198, 128, 195, 189, 13, 87, 223, 245, 36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3,
     224, 15, 236, 222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0, 98, 68, 26,
     184, 56, 130, 100, 159, 38, 65, 173, 69, 70, 146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 7, 88,
     179, 64, 134, 172, 29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83,
     170, 144, 202, 216, 133, 97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166,
     116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182]

inv_π = ['a5', '2d', '32', '8f', '0e', '30', '38', 'c0', '54', 'e6', '9e', '39', '55', '7e', '52', '91',
     '64', '03', '57', '5a', '1c', '60', '07', '18', '21', '72', 'a8', 'd1', '29', 'c6', 'a4', '3f',
     'e0', '27', '8d', '0c', '82', 'ea', 'ae', 'b4', '9a', '63', '49', 'e5', '42', 'e4', '15', 'b7',
     'c8', '06', '70', '9d', '41', '75', '19', 'c9', 'aa', 'fc', '4d', 'bf', '2a', '73', '84', 'd5',
     'c3', 'af', '2b', '86', 'a7', 'b1', 'b2', '5b', '46', 'd3', '9f', 'fd', 'd4', '0f', '9c', '2f',
     '9b', '43', 'ef', 'd9', '79', 'b6', '53', '7f', 'c1', 'f0', '23', 'e7', '25', '5e', 'b5', '1e',
     'a2', 'df', 'a6', 'fe', 'ac', '22', 'f9', 'e2', '4a', 'bc', '35', 'ca', 'ee', '78', '05', '6b',
     '51', 'e1', '59', 'a3', 'f2', '71', '56', '11', '6a', '89', '94', '65', '8c', 'bb', '77', '3c',
     '7b', '28', 'ab', 'd2', '31', 'de', 'c4', '5f', 'cc', 'cf', '76', '2c', 'b8', 'd8', '2e', '36',
     'db', '69', 'b3', '14', '95', 'be', '62', 'a1', '3b', '16', '66', 'e9', '5c', '6c', '6d', 'ad',
     '37', '61', '4b', 'b9', 'e3', 'ba', 'f1', 'a0', '85', '83', 'da', '47', 'c5', 'b0', '33', 'fa',
     '96', '6f', '6e', 'c2', 'f6', '50', 'ff', '5d', 'a9', '8e', '17', '1b', '97', '7d', 'ec', '58',
     'f7', '1f', 'fb', '7c', '09', '0d', '7a', '67', '45', '87', 'dc', 'e8', '4f', '1d', '4e', '04',
     'eb', 'f8', 'f3', '3e', '3d', 'bd', '8a', '88', 'dd', 'cd', '0b', '13', '98', '02', '93', '80',
     '90', 'd0', '24', '34', 'cb', 'ed', 'f4', 'ce', '99', '10', '44', '40', '92', '3a', '01', '26',
     '12', '1a', '48', '68', 'f5', '81', '8b', 'c7', 'd6', '20', '0a', '08', '00', '4c', 'd7', '74']

L_vector = [148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1]


def S(a):
    a = wrap(a, 2)
    new_a = ''

    for i in range(len(a)):
        new_a += '0' * (2 - len(hex(π[int(a[i], 16)])[2:])) + hex(π[int(a[i], 16)])[2:]

    return new_a


def inv_S(a):
    a = wrap(a, 2)
    new_a = ''

    for i in range(len(a)):
        new_a += '0' * (2 - len(inv_π[int(a[i],16)])) + inv_π[int(a[i],16)]

    return new_a


def R(a, F):
    new_a = 0
    for i in range(len(a) - 1, -1, -1):
        new_a ^= (F.Multiply(int(a[i], 16), L_vector[i]))

    for k in range(len(a)):
        a[len(a) - k - 1] = a[len(a) - k - 2]
    a[0] = '0' * (2 - len(hex(new_a)[2:])) + hex(new_a)[2:]

    return a


def inv_R(a, F):
    new_a = 0
    a_ = a[1:] + a[:14]

    for i in range(len(a) - 1, -1, -1):
        new_a ^= (F.Multiply(int(a_[i], 16), L_vector[i]))

    a.pop(0)
    a.append('0' * (2 - len(hex(new_a)[2:])) + hex(new_a)[2:])

    return a


def L(a):
    F = ffield.FField(8, gen=0x1c3)
    a = wrap(a, 2)

    for j in range(len(a)):
        R(a, F)

    a = array_to_str(a)

    return a


def inv_L(a):
    F = ffield.FField(8, gen=0x1c3)
    a = wrap(a, 2)

    for j in range(len(a)):
        inv_R(a, F)

    a = array_to_str(a)

    return a


def X(k, a):
    return '0' * (32 - len(hex(int(a, 16) ^ int(k, 16))[2:])) + hex(int(a, 16) ^ int(k, 16))[2:]


def F(K):
    K = wrap(K, 32)
    o = 1
    for i in range(2, 10, 2):
        K.append('')
        K.append('')
        K[i], K[i+1] = K[i-2], K[i-1]
        for j in range(1, 9):
            K_ = K[i]

            C = '0' * (32 - len(hex(o)[2:])) + hex(o)[2:]

            K[i] = L(S(X(K[i], L(C))))
            K[i] = X(K[i], K[i+1])
            K[i+1] = K_
            o += 1

    return K

def encryption(a, K):
    K = str_to_hex(K)[:128]
    K = F(K)
    a = message_completion(a)
    a_ = ''
    for p in range(len(a)):
        for i in range(len(K)-1):
            a[p] = L(S(X(K[i], a[p])))
        a[p] = X(K[9], a[p])
        a_ += a[p]

    return a_

def decryption(a, K):
    K = str_to_hex(K)[:128]
    K = F(K)
    a = wrap(a, 32)
    a_=''

    for p in range(len(a)):
        for i in range(len(K)-1, 0, -1):
            a[p] = inv_S(inv_L(X(K[i], a[p])))

        a[p] = X(K[0], a[p])
        a_ += a[p]
    a_ = hex_to_str(a_)
    return a_

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
    a = wrap(a, 4)
    for i in range(len(a)):
        if chr(int(a[i], 16)) != 'က':
            a_ += chr(int(a[i], 16))

    return a_


message = input('Введите сообщение: ')

key = input('Введите ключ (минимум 8 символов): ')
if len(key) < 8:
    print('Введите новый ключ.')
    sys.exit(0)
#message = 'невсекотумасленицазптбудетивеликийпосттчк'
#key = 'совасовасова'

enc = encryption(message, key)
print('Зашифрованное сообщение:', enc)

dec = decryption(enc, key)
print('Расшифрованное сообщение:', dec)


