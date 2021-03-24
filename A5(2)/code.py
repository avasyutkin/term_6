from textwrap import wrap
import sys

def key_generation(key):
    key_bin = ''
    for i in key:
        key_bin += '0' * (16 - len(bin(ord(i))[2:])) + bin(ord(i))[2:]

    return key_bin

def message_to_bin(message):
    message_arr = []
    for i in message:
        message_arr.append('0' * (16 - len(bin(ord(i))[2:])) + bin(ord(i))[2:])
    #print(message_arr)
    message_binary = ''.join(message_arr)

    return message_binary

def bin_array_to_str(bin_message):
    message = ''
    for i in bin_message:
        message += i

    return message

def bin_to_hex(message):
    message = wrap(message, 4)
    message_hex = ''

    for i in message:
        message_hex += hex(int(i, 2))[2:]

    return message_hex

def hex_to_bin(message_hex):
    message = ''
    for i in message_hex:
        message += '0' * (4 - len(bin(int(i, 16))[2:])) + bin(int(i, 16))[2:]

    return message

def bin_to_message(bin_message):
    message = ''
    bin_message = wrap(bin_message, 16)
    for i in bin_message:
        message += chr(int(i, 2))

    return message

def gamma_generation(message_binary, key_bin):
    R1 = list(map(int, key_bin[0:19]))  # (18, 17, 16, 13, 0), мажоритарная функция - 12, 14, 15
    R2 = list(map(int, key_bin[19:41]))  # (21, 20, 0), мажоритарная функция - 9, 13, 16
    R3 = list(map(int, key_bin[41:64]))  # (22, 21, 20, 7, 0), мажоритарная функция - 13, 16, 18
    R4 = list(map(int, key_bin[64:81]))  # (16, 11, 0), синхробиты - 3, 7, 10
    #print('R', R1, R2, R3, R4)

    encrypted_message_binary = []
    output_bits_array = ''

    for i in message_binary:
        R1_F = R1[12] & R1[14] | R1[12] & R1[15] | R1[14] & R1[15]
        R2_F = R2[9] & R2[13] | R2[9] & R2[16] | R2[13] & R2[16]
        R3_F = R3[13] & R3[16] | R3[13] & R3[18] | R3[16] & R3[18]

        output_bit = (R1[18] + R2[21] + R3[22] + R1_F + R2_F + R3_F) % 2
        #print('outputbit', output_bit, 'R1_F', R1_F, 'R2_F', R2_F, 'R3_F', R3_F, 'R1[18]', R1[18], 'R2[21]', R2[21], 'R3[22]', R3[22])

        output_bits_array = output_bits_array + str(output_bit)
        encrypted_message_binary += str((output_bit + int(i)) % 2)
        #print('enc bit', (output_bit + int(i)) % 2)
        F = R4[3] & R4[7] | R4[3] & R4[10] | R4[7] & R4[10]
        #print('F',F, R4[3], R4[7], R4[10])
        if R4[10] == F:
            for k in range(len(R1)):
                R1[len(R1) - k - 1] = R1[len(R1) - k - 2]
            R1[0] = (R1[13] + R1[16] + R1[17] + R1[18]) % 2
            #print(R1, R1[13], R1[16] , R1[17] , R1[18])
        if R4[3] == F:
            for k in range(len(R2)):
                R2[len(R2) - k - 1] = R2[len(R2) - k - 2]
            R2[0] = (R2[20] + R2[21]) % 2
            #print(R2, R2[20] , R2[21])
        if R4[7] == F:
            for k in range(len(R3)):
                R3[len(R3) - k - 1] = R3[len(R3) - k - 2]
            R3[0] = (R3[7] + R3[20] + R3[21] + R3[22]) % 2
            #print(R3, R3[7] , R3[20] , R3[21] , R3[22])
        for k in range(len(R4)):
            R4[len(R4) - k - 1] = R4[len(R4) - k - 2]
        R4[0] = (R4[11] + R4[16]) % 2
        #print(R4,R4[11] ,R4[16] )

    print('Сгенерированная гамма: ', bin_to_hex(output_bits_array))

    return encrypted_message_binary

message = input("Введите сообщение: ")
key = input('Введите ключ (минимум 6 символов): ')
if len(key) < 6:
    print('Длина ключа не соответствует требованиям криптосистемы. Пожалуйста, введите новый ключ.')
    sys.exit(0)

encrypted_message = bin_to_hex(bin_array_to_str(gamma_generation(message_to_bin(message), key_generation(key))))
print("Зашифрованное сообщение:", encrypted_message)

decrypted_message = bin_to_message(bin_array_to_str(gamma_generation(hex_to_bin(encrypted_message), key_generation(key))))
print('Расшифрованное сообщение: ', decrypted_message)

