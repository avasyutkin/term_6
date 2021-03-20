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
    R1 = list(map(int, key_bin[0:19]))  # (18, 17, 16, 13, 0), синхробит - 7
    R2 = list(map(int, key_bin[19:41]))   # (21, 20, 0), синхробит - 9
    R3 = list(map(int, key_bin[41:64]))  # (22, 21, 20, 7, 0), синхробит - 9

    encrypted_message_binary = []
    output_bits_array = ''

    for i in message_binary:
        output_bit = (R1[18] + R2[21] + R3[22]) % 2
        output_bits_array = output_bits_array + str(output_bit)
        encrypted_message_binary += str((output_bit + int(i)) % 2)
        F = R1[7] & R2[9] | R1[7] & R3[9] | R2[9] & R3[9]
        if R1[7] == F:
            for k in range(len(R1)):
                R1[len(R1) - k - 1] = R1[len(R1) - k - 2]
            R1[0] = (R1[13] + R1[16] + R1[17] + R1[18]) % 2
        if R2[9] == F:
            for k in range(len(R2)):
                R2[len(R2) - k - 1] = R2[len(R2) - k - 2]
            R2[0] = (R2[20] + R2[21]) % 2
        if R3[9] == F:
            for k in range(len(R3)):
                R3[len(R3) - k - 1] = R3[len(R3) - k - 2]
            R3[0] = (R3[7] + R3[20] + R3[21] + R3[22]) % 2

    print('Сгенерированная гамма: ', output_bits_array)

    return encrypted_message_binary

message = input("Введите сообщение: ")
key = input('Введите ключ (минимум 4 символа): ')

encrypted_message = gamma_generation(message_to_bin(message), key_generation(key))
print("Зашифрованное сообщение:", bin_array_to_str(encrypted_message))

decrypted_message = bin_to_message(bin_array_to_str(gamma_generation(encrypted_message, key_generation(key))))
print('Расшифрованное сообщение: ', decrypted_message)

