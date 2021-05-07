

def prn_generator(parameters, len_message):
    parameters = list(parameters.split())
    if len(parameters) < 3:
        return 'Введите три параметра T, a и c.'

    T = int(parameters[2])
    a = int(parameters[0])
    c = int(parameters[1])

    T_array = []
    if c % 2 == 0:
        return 'Значение параметра с должно быть четным. Пожалуйста, введите новые параметры.'

    if a % 4 != 1:
        return 'Значение параметра а должно удовлетворять условию a mod 4 = 1. Пожалуйста, введите новые параметры.'

    for i in range(len_message):
        T_array.append(T)
        T = (a * T + c) % 1114

    return T_array


def encryption(message, parameters):
    gamma = prn_generator(parameters, len(message))
    if gamma == 'Значение параметра с должно быть четным. Пожалуйста, введите новые параметры.' or gamma == 'Значение параметра а должно удовлетворять условию a mod 4 = 1. Пожалуйста, введите новые параметры.':
        return gamma

    encrypted_message = []
    message = message_to_code(message)

    k = 0
    for i in message:
        encrypted_message.append(int(i) + gamma[k] % 1114)
        k += 1

    encrypted_message = code_to_message(encrypted_message)

    return encrypted_message


def decryption(encrypted_message, parameters):
    encrypted_message = message_to_code(encrypted_message)
    gamma = prn_generator(parameters, len(encrypted_message))
    decrypted_message = []

    k = 0
    for i in encrypted_message:
        decrypted_message.append(int(i) - gamma[k] % 1114)
        k += 1

    decrypted_message = code_to_message(decrypted_message)

    return decrypted_message


def message_to_code(message):
    message_arr = []
    for i in message:
        message_arr.append('0' * (4 - len(str(ord(i)))) + str(ord(i)))

    return message_arr


def code_to_message(bin_message):
    text = ''
    for i in bin_message:
        if i < 0:
            return 'Введенное сообщение не является шифртекстом.'
        text += chr(int(i))

    return text
