from textwrap import wrap

Sbox = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
        ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
        ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
        ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
        ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
        ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
        ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
        ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
        ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
        ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
        ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
        ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
        ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
        ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
        ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
        ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

InvSbox = [['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'],
           ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'],
           ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'],
           ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'],
           ['72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'],
           ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84'],
           ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'],
           ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'],
           ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'],
           ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'],
           ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'],
           ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'],
           ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f'],
           ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'],
           ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'],
           ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']]

Rcon = ['00000000', '01000000', '02000000', '04000000', '08000000', '10000000', '20000000', '40000000', '80000000', '1b000000', '36000000']

def RotWord(wi):
    wi = wi[2:] + wi[:2]

    return wi

def SubWord(wi):
    SubWord = ''

    for i in wi:
        SubWord += Sbox[int(i[0], 16)][int(i[1], 16)]

    return SubWord

def XOR_with_Rcon(wi, Rcon):
    wi_ = ''
    for i in range(len(wi)):
        wi_ += str(hex((int(wi[i], 16) ^ int(Rcon[i], 16)))[2:])

    return wi_

def SubBytes(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            input[i][j] = Sbox[int(input[i][j][0], 16)][int(input[i][j][1], 16)]

    return input

def round_key_generation(w):
    for count_w in range(len(w), len(w) + 4):
        w_ = ''
        w.append(w_)

        if count_w % 4 == 0:
            w_ = RotWord(w[count_w - 1])
            w_ = wrap(w_, 2)
            w_ = SubWord(w_)
            Rcon_ = Rcon[int(count_w/4)]
            w_ = XOR_with_Rcon(w_, Rcon_)

        if w_ == '':
            w_ = w[count_w - 1]

        for i in range(len(w[count_w-4])):
            w[count_w] += str(hex((int(w_[i], 16) ^ int(w[count_w - 4][i], 16)))[2:])

    return w

def ShiftRows(input):
    input_ = []
    for j in range(len(input)):
        input_.append([i[j] for i in input][j:] + [i[j] for i in input][:j])

    for j in range(len(input_)):
        input[j] = ([i[j] for i in input_])

    return input

def MixColumns(input):
    a = generation_array(1, 4)
    b = generation_array(1, 4)
    input_ = ''
    for i in input:
        r = i
        for c in range(4):
            a[c] = r[c]
            h = (int(r[c], 16) >> 7) & 1
            b[c] = int(r[c], 16) << 1
            b[c] ^= h * int('1B', 16)

        r[0] = '0' * (2 - len(hex((b[0] ^ int(a[3], 16) ^ int(a[2], 16) ^ b[1] ^ int(a[1], 16)) % 256)[2:])) + hex((b[0] ^ int(a[3], 16) ^ int(a[2], 16) ^ b[1] ^ int(a[1], 16)) % 256)[2:]
        r[1] = '0' * (2 - len(hex((b[1] ^ int(a[0], 16) ^ int(a[3], 16) ^ b[2] ^ int(a[2], 16)) % 256)[2:])) + hex((b[1] ^ int(a[0], 16) ^ int(a[3], 16) ^ b[2] ^ int(a[2], 16)) % 256)[2:]
        r[2] = '0' * (2 - len(hex((b[2] ^ int(a[1], 16) ^ int(a[0], 16) ^ b[3] ^ int(a[3], 16)) % 256)[2:])) + hex((b[2] ^ int(a[1], 16) ^ int(a[0], 16) ^ b[3] ^ int(a[3], 16)) % 256)[2:]
        r[3] = '0' * (2 - len(hex((b[3] ^ int(a[2], 16) ^ int(a[1], 16) ^ b[0] ^ int(a[0], 16)) % 256)[2:])) + hex((b[3] ^ int(a[2], 16) ^ int(a[1], 16) ^ b[0] ^ int(a[0], 16)) % 256)[2:]
        input_ += r[0] + r[1] + r[2] + r[3]

    input_ = wrap(input_, 8)

    return input_

def generation_array(size1, size2):
    array = [[0] * size1 for i in range(size2)]

    return array

input = '3243f6a8885a308d313198a2e0370734'
key = '2b7e151628aed2a6abf7158809cf4f3c'
input = [input[0:8], input[8:16], input[16:24], input[24:32]]
w = [key[0:8], key[8:16], key[16:24], key[24:32]]


input_ = generation_array(4, 4)

d = 0
y = 0
w_ = w
for o in range(11):
    if y > 0:
        input = SubBytes(input_)

        input = ShiftRows(input)

        w = round_key_generation(w)

        w_ = w[4 * (o):]

        if d < 9:
            input = MixColumns(input)
            d = d + 1
        else:
            input_ = input
            input = ''
            for i in range(len(input_)):
                for j in range(len(input_[i])):
                    input+=input_[i][j]
            input = wrap(input, 8)

    input_str = ''

    for i in range(len(input)):
        for j in range(len(input[i])):
            for k in input[i][j]:
                input_str += hex(int(input[i][j], 16) ^ int(w_[i][j], 16))[2:]

    input_str = wrap(input_str, 2)
    input_ = generation_array(4, 4)

    k = 0
    for i in range(len(input_)):
        for j in range(len(input_[i])):
            input_[i][j] = input_str[k]
            k += 1
    y = y + 1
    print(input_)
