from textwrap import wrap

def key_generation(key):
    key_bin = ''
    for i in key:
        key_bin += '0' * (16 - len(bin(ord(i))[2:])) + bin(ord(i))[2:]

    return key_bin

def message_to_bin(message):
    message_arr = []
    for i in message:
        message_arr.append('0' * (16 - len(bin(ord(i))[2:])) + bin(ord(i))[2:])

    message_binary = ''.join(message_arr)

    return message_binary

def bin_array_to_str(bin_message):
    message = ''
    for i in bin_message:
        message += i

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

    encrypted_message_binary = []
    output_bits_array = ''

    for i in message_binary:
        R1_F = R1[12] & R1[14] | R1[12] & R1[15] | R1[14] & R1[15]
        R2_F = R2[9] & R2[13] | R2[9] & R2[16] | R2[13] & R2[16]
        R3_F = R3[13] & R3[16] | R3[13] & R3[18] | R3[16] & R3[18]

        output_bit = (R1[18] + R2[21] + R3[22] + R1_F + R2_F + R3_F) % 2
        output_bits_array = output_bits_array + str(output_bit)
        encrypted_message_binary += str((output_bit + int(i)) % 2)
        F = R4[3] & R4[7] | R4[3] & R4[10] | R4[7] & R4[10]
        if R4[10] == F:
            for k in range(len(R1)):
                R1[len(R1) - k - 1] = R1[len(R1) - k - 2]
            R1[0] = (R1[13] + R1[16] + R1[17] + R1[18]) % 2
        if R4[3] == F:
            for k in range(len(R2)):
                R2[len(R2) - k - 1] = R2[len(R2) - k - 2]
            R2[0] = (R2[20] + R2[21]) % 2
        if R4[7] == F:
            for k in range(len(R3)):
                R3[len(R3) - k - 1] = R3[len(R3) - k - 2]
            R3[0] = (R3[7] + R3[20] + R3[21] + R3[22]) % 2
        for k in range(len(R4)):
            R4[len(R4) - k - 1] = R4[len(R4) - k - 2]
        R4[0] = (R4[11] + R4[16]) % 2

    print('Сгенерированная гамма: ', output_bits_array)

    return encrypted_message_binary

message = input("Введите сообщение: ")
key = input('Введите ключ (минимум 5 символов): ')

encrypted_message = gamma_generation(message_to_bin(message), key_generation(key))
print("Зашифрованное сообщение:", bin_array_to_str(encrypted_message))

decrypted_message = bin_to_message(bin_array_to_str(gamma_generation(encrypted_message, key_generation(key))))
print('Расшифрованное сообщение: ', decrypted_message)

