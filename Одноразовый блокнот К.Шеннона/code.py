import sys
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def prn_generator(T0, a, c, len_message):
    T = int(T0)
    a = int(a)
    c = int(c)

    T_array = []
    if c % 2 == 0 or a % 4 != 1:
        print('Введенные вами параметры не смогут обеспечить должную криптостойкость, пожалуйста, введите новые параметры.')
        sys.exit(0)

    for i in range(len_message):
        T_array.append(T)
        T = (a * T + c) % 33
    print('Сгенерированная гамма: ', T_array)
    return T_array

def encryption(message, gamma):
    encrypted_message = ''
    k = 0
    for i in message:
        encrypted_message += alphabet[((alphabet.index(i) + gamma[k]) % 33)]
        k += 1

    return encrypted_message

def decryption(encrypted_message, gamma):
    decrypted_mesage = ''
    k = 0
    for i in encrypted_message:
        decrypted_mesage += alphabet[((alphabet.index(i) - gamma[k]) % 33)]
        k += 1

    return decrypted_mesage

message = input('Введите сообщение: ')
parameters = input('Введите Т0, a, c через пробел: ').split()

encrypted_message = encryption(message, prn_generator(parameters[0], parameters[1], parameters[2], len(message)))
print('Зашифрованное сообщение: ', encrypted_message)

decrypted_message = decryption(encrypted_message, prn_generator(parameters[0], parameters[1], parameters[2], len(message)))
print('Расшифрованное сообщение: ', decrypted_message)