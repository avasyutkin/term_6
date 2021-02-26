from textwrap import wrap

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'э', 'ю', 'я']

def encryption(message, encrypted_message, key):
    key = key_generation(key)
    message = list(message)
    message_str = ''
    i = -1
    for symbol in message:
        if symbol == message[i]:
            message_str = message_str + 'ф' + symbol
        else:
            message_str = message_str + symbol
        i = i + 1
    print(len(message_str))
    if len(message_str) % 2 != 0:
        message_str = message_str + 'ф'

    print(message_str)

    message = wrap(message_str, 2)
    print(key)
    message_str = ''
    for symbol in message:
        for sym in symbol:
            for i in range(len(key)):
                for j in range(len(key[i])):
                    if sym == key[i][j]:
                        message_str = message_str + str(i)+str(j)

    message = wrap(message_str, 4)
    message_str = ''
    print(message)
    for i in message:
        i = wrap(i, 1)
        if i[0] == i[2]:
            if i[1] == '5':
                i[1] = (int(i[1]) + 1) % len(key) - 1
                i[3] = int(i[3]) + 1
            if i[3] == '5':
                i[3] = (int(i[3]) + 1) % len(key) - 1
                i[1] = int(i[1]) + 1
            else:
                i[1] = (int(i[1]) + 1) % len(key)
                i[3] = (int(i[3]) + 1) % len(key)
        elif i[1] == i[3]:
            if i[0] == '4':
                i[0] = (int(i[0]) + 1) % len(key) - 1
                i[2] = int(i[2]) + 1
            if i[2] == '4':
                i[2] = (int(i[2]) + 1) % len(key) - 1
                i[0] = int(i[0]) + 1
            else:
                i[0] = (int(i[0]) + 1) % len(key)
                i[2] = (int(i[2]) + 1) % len(key)
        else:
            m = i[3]
            i[3] = i[1]
            i[1] = m
        message_str = message_str + str(i[0]) + str(i[1]) + str(i[2]) + str(i[3])
    print(len(message_str), message_str)
    message = wrap(message_str, 2)
    print(len(message), message)
    count= 0
    for i in message:
        #print(message.index(i))
        for o in range(len(key)+1):
            for j in range(len(key)+1):
                if i == str(o)+str(j):
                    count = count + 1
                    #print(count, message[message.index(i)], str(o)+str(j))
                    encrypted_message = encrypted_message + key[o][j]
    print(encrypted_message, 'письк')

    return encrypted_message

def decryption(encrypted_message, decrypted_message, key):
    key = key_generation(key)
    message = wrap(encrypted_message, 2)
    print(message)
    message_str = ''
    for symbol in message:
        for sym in symbol:
            for i in range(len(key)):
                for j in range(len(key[i])):
                    if sym == key[i][j]:
                        message_str = message_str + str(i) + str(j)
    print(message_str)

    message = wrap(message_str, 4)
    message_str = ''
    print(message)
    for i in message:
        i = wrap(i, 1)
        if i[0] == i[2]:
            if i[1] == '0':
                i[1] = (int(i[1]) - 1) % len(key) + 1
                i[3] = int(i[3]) - 1
            if i[3] == '0':
                i[3] = (int(i[3]) - 1) % len(key) + 1
                i[1] = int(i[1]) - 1
            else:
                i[1] = (int(i[1]) - 1) % len(key)
                i[3] = (int(i[3]) - 1) % len(key)
        elif i[1] == i[3]:
            if i[0] == '0':
                i[0] = (int(i[0]) - 1) % len(key) + 1
                i[2] = int(i[2]) - 1
            if i[2] == '0':
                i[2] = (int(i[2]) - 1) % len(key) + 1
                i[0] = int(i[0]) - 1
            else:
                i[0] = (int(i[0]) - 1) % len(key)
                i[2] = (int(i[2]) - 1) % len(key)
        else:
            m = i[3]
            i[3] = i[1]
            i[1] = m
        message_str = message_str + str(i[0]) + str(i[1]) + str(i[2]) + str(i[3])
    print(message)
    message = wrap(message_str, 2)
    print(message)

    for i in message:
        for o in range(len(key)+1):
            for j in range(len(key)+1):
                if i == str(o)+str(j):
                    decrypted_message = decrypted_message + key[o][j]

    message = list(decrypted_message)
    message_str = ''
    i = -1
    for symbol in message:
        if (symbol == 'ф') and (message[i] == message[i+2]):
            print(message[i], symbol)
        else:
            message_str = message_str + symbol
        if i == len(message)-3:
            continue
        else:
            i = i + 1



    print(message_str)



    return decrypted_message

def key_generation(key):
    key_set = set()
    key = [x for x in list(key) + alphabet if not (x in key_set or key_set.add(x))]
    key_matrix = [[0]*6 for i in range(5)]
    k = 0
    for i in range(5):
        for j in range(6):
            key_matrix[i][j] = key[k]
            k = k + 1
    return key_matrix


message = 'рневсекотумасленицазптбудетивеликиипосттчк'
key = 'сова'
encrypted_message = ''
encrypted_message = encryption(message, encrypted_message, key)

print(encrypted_message)

decrypted_message = ''
decrypted_message = decryption(encrypted_message, decrypted_message, key)

print(decrypted_message)