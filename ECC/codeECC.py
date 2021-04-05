import math
from textwrap import wrap
import sys
from sympy.ntheory import totient

def euler_function(a):
    p = 0

    for i in range(a):
        if math.gcd(a, i) == 1:
            print('a')
            p += 1

    return p


def doubling_P(P, a, p):
    λ = ['', '']
    λ[0] = (3 * P[0] ** 2 + a) % p
    print('111')
    λ[1] = 2 * P[1] % p
    print('112')
    if not (λ[0]/λ[1]).is_integer():
        print('pi1')
        λ[0] = λ[0] % p
        print(λ[1], (p - 2))
        λ[1] = (λ[1] ** (p - 2)) % p
        print('pi3')
        λ = int(λ[0] * λ[1] % p)
        print('113')
    else:
        λ = int(λ[0]/λ[1])

    x = (λ ** 2 - 2 * P[0]) % p
    y = (λ * (P[0] - x) - P[1]) % p

    return x, y


def addition_P(P1, P2, p):
    λ = ['', '']
    λ[0] = (P2[1] - P1[1]) % p
    λ[1] = (P2[0] - P1[0]) % p

    if not (λ[0]/λ[1]).is_integer():
        λ[0] = λ[0] % p
        print('pi')
        λ[1] = (λ[1] ** (p - 2)) % p
        print('pi2')
        λ = int(λ[0] * λ[1] % p)
        print('pi3')
    else:
        print('pi4')
        λ = int(λ[0]/λ[1])

    x = (λ ** 2 - P1[0] - P2[0]) % p
    y = (λ * (P1[0] - x) - P1[1]) % p

    return x, y


def key_gen(P, k, a, p):
    k = bin(k)[3:]
    P_ = P
    print('11')
    for i in k:
        P_ = doubling_P(P_, a, p)
        print('12')
        if i == '1':
            P_ = addition_P(P, P_, p)

    return P_


def encryption(message, P_x, P_y, k, Cb):
    P = [P_x, P_y]
    print('1')
    public_key = key_gen(P, Cb, a, p)
    print('2')
    private_key = key_gen(P, k, a, p)
    print('3')
    P = key_gen(public_key, k, a, p)
    print('4')
    new_message = ''

    new_message += str(int(message) * P[0] % p)

    return private_key, new_message


def decryption(message, Cb):
    P = key_gen(message[0], Cb, a, p)

    new_message = ''
    new_message += str(int(message[1]) * (P[0] ** (p - 2)) % p)

    return new_message


def message_to_pos_unicode(message):
    new_message = []

    for i in message:
        new_message.append(('0' * (4 - len(str(ord(i)))) + str(ord(i))))

    return new_message


def pos_unicode_to_message(message):
    new_message = ''
    for i in message:
        new_message += chr(i)

    return new_message

print(euler_function(57896044618658097711785492504343953926634992332820282019728792003956564821041))
a = 7
b = 43308876546767276905765904595650931995942111794451039583252968842033849580414
p = 57896044618658097711785492504343953926634992332820282019728792003956564821041

message = input('Введите сообщение: ')
key = list(map(int, input('Введите через пробел следующиме параметры: точку P, k, Cb: ').split()))

enc = encryption(message, key[0], key[1], key[2], key[3])
print('Закрытый ключ и зашифрованное сообщение:', enc)

dec = decryption(enc, key[3])
print('Расшифрованное сообщение:', dec)