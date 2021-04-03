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

multiply_by_9 = [['00','09','12','1b','24','2d','36','3f','48','41','5a','53','6c','65','7e','77'],
                 ['90','99','82','8b','b4','bd','a6','af','d8','d1','ca','c3','fc','f5','ee','e7'],
                 ['3b','32','29','20','1f','16','0d','04','73','7a','61','68','57','5e','45','4c'],
                 ['ab','a2','b9','b0','8f','86','9d','94','e3','ea','f1','f8','c7','ce','d5','dc'],
                 ['76','7f','64','6d','52','5b','40','49','3e','37','2c','25','1a','13','08','01'],
                 ['e6','ef','f4','fd','c2','cb','d0','d9','ae','a7','bc','b5','8a','83','98','91'],
                 ['4d','44','5f','56','69','60','7b','72','05','0c','17','1e','21','28','33','3a'],
                 ['dd','d4','cf','c6','f9','f0','eb','e2','95','9c','87','8e','b1','b8','a3','aa'],
                 ['ec','e5','fe','f7','c8','c1','da','d3','a4','ad','b6','bf','80','89','92','9b'],
                 ['7c','75','6e','67','58','51','4a','43','34','3d','26','2f','10','19','02','0b'],
                 ['d7','de','c5','cc','f3','fa','e1','e8','9f','96','8d','84','bb','b2','a9','a0'],
                 ['47','4e','55','5c','63','6a','71','78','0f','06','1d','14','2b','22','39','30'],
                 ['9a','93','88','81','be','b7','ac','a5','d2','db','c0','c9','f6','ff','e4','ed'],
                 ['0a','03','18','11','2e','27','3c','35','42','4b','50','59','66','6f','74','7d'],
                 ['a1','a8','b3','ba','85','8c','97','9e','e9','e0','fb','f2','cd','c4','df','d6'],
                 ['31','38','23','2a','15','1c','07','0e','79','70','6b','62','5d','54','4f','46']]

multiply_by_11 = [['00','0b','16','1d','2c','27','3a','31','58','53','4e','45','74','7f','62','69'],
                  ['b0','bb','a6','ad','9c','97','8a','81','e8','e3','fe','f5','c4','cf','d2','d9'],
                  ['7b','70','6d','66','57','5c','41','4a','23','28','35','3e','0f','04','19','12'],
                  ['cb','c0','dd','d6','e7','ec','f1','fa','93','98','85','8e','bf','b4','a9','a2'],
                  ['f6','fd','e0','eb','da','d1','cc','c7','ae','a5','b8','b3','82','89','94','9f'],
                  ['46','4d','50','5b','6a','61','7c','77','1e','15','08','03','32','39','24','2f'],
                  ['8d','86','9b','90','a1','aa','b7','bc','d5','de','c3','c8','f9','f2','ef','e4'],
                  ['3d','36','2b','20','11','1a','07','0c','65','6e','73','78','49','42','5f','54'],
                  ['f7','fc','e1','ea','db','d0','cd','c6','af','a4','b9','b2','83','88','95','9e'],
                  ['47','4c','51','5a','6b','60','7d','76','1f','14','09','02','33','38','25','2e'],
                  ['8c','87','9a','91','a0','ab','b6','bd','d4','df','c2','c9','f8','f3','ee','e5'],
                  ['3c','37','2a','21','10','1b','06','0d','64','6f','72','79','48','43','5e','55'],
                  ['01','0a','17','1c','2d','26','3b','30','59','52','4f','44','75','7e','63','68'],
                  ['b1','ba','a7','ac','9d','96','8b','80','e9','e2','ff','f4','c5','ce','d3','d8'],
                  ['7a','71','6c','67','56','5d','40','4b','22','29','34','3f','0e','05','18','13'],
                  ['ca','c1','dc','d7','e6','ed','f0','fb','92','99','84','8f','be','b5','a8','a3']]

multiply_by_13 = [['00','0d','1a','17','34','39','2e','23','68','65','72','7f','5c','51','46','4b'],
                  ['d0','dd','ca','c7','e4','e9','fe','f3','b8','b5','a2','af','8c','81','96','9b'],
                  ['bb','b6','a1','ac','8f','82','95','98','d3','de','c9','c4','e7','ea','fd','f0'],
                  ['6b','66','71','7c','5f','52','45','48','03','0e','19','14','37','3a','2d','20'],
                  ['6d','60','77','7a','59','54','43','4e','05','08','1f','12','31','3c','2b','26'],
                  ['bd','b0','a7','aa','89','84','93','9e','d5','d8','cf','c2','e1','ec','fb','f6'],
                  ['d6','db','cc','c1','e2','ef','f8','f5','be','b3','a4','a9','8a','87','90','9d'],
                  ['06','0b','1c','11','32','3f','28','25','6e','63','74','79','5a','57','40','4d'],
                  ['da','d7','c0','cd','ee','e3','f4','f9','b2','bf','a8','a5','86','8b','9c','91'],
                  ['0a','07','10','1d','3e','33','24','29','62','6f','78','75','56','5b','4c','41'],
                  ['61','6c','7b','76','55','58','4f','42','09','04','13','1e','3d','30','27','2a'],
                  ['b1','bc','ab','a6','85','88','9f','92','d9','d4','c3','ce','ed','e0','f7','fa'],
                  ['b7','ba','ad','a0','83','8e','99','94','df','d2','c5','c8','eb','e6','f1','fc'],
                  ['67','6a','7d','70','53','5e','49','44','0f','02','15','18','3b','36','21','2c'],
                  ['0c','01','16','1b','38','35','22','2f','64','69','7e','73','50','5d','4a','47'],
                  ['dc','d1','c6','cb','e8','e5','f2','ff','b4','b9','ae','a3','80','8d','9a','97']]

multiply_by_14 = [['00','0e','1c','12','38','36','24','2a','70','7e','6c','62','48','46','54','5a'],
                  ['e0','ee','fc','f2','d8','d6','c4','ca','90','9e','8c','82','a8','a6','b4','ba'],
                  ['db','d5','c7','c9','e3','ed','ff','f1','ab','a5','b7','b9','93','9d','8f','81'],
                  ['3b','35','27','29','03','0d','1f','11','4b','45','57','59','73','7d','6f','61'],
                  ['ad','a3','b1','bf','95','9b','89','87','dd','d3','c1','cf','e5','eb','f9','f7'],
                  ['4d','43','51','5f','75','7b','69','67','3d','33','21','2f','05','0b','19','17'],
                  ['76','78','6a','64','4e','40','52','5c','06','08','1a','14','3e','30','22','2c'],
                  ['96','98','8a','84','ae','a0','b2','bc','e6','e8','fa','f4','de','d0','c2','cc'],
                  ['41','4f','5d','53','79','77','65','6b','31','3f','2d','23','09','07','15','1b'],
                  ['a1','af','bd','b3','99','97','85','8b','d1','df','cd','c3','e9','e7','f5','fb'],
                  ['9a','94','86','88','a2','ac','be','b0','ea','e4','f6','f8','d2','dc','ce','c0'],
                  ['7a','74','66','68','42','4c','5e','50','0a','04','16','18','32','3c','2e','20'],
                  ['ec','e2','f0','fe','d4','da','c8','c6','9c','92','80','8e','a4','aa','b8','b6'],
                  ['0c','02','10','1e','34','3a','28','26','7c','72','60','6e','44','4a','58','56'],
                  ['37','39','2b','25','0f','01','13','1d','47','49','5b','55','7f','71','63','6d'],
                  ['d7','d9','cb','c5','ef','e1','f3','fd','a7','a9','bb','b5','9f','91','83','8d']]


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


def SubBytes(input, bool):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if bool == True:
                input[i][j] = Sbox[int(input[i][j][0], 16)][int(input[i][j][1], 16)]
            else:
                input[i][j] = InvSbox[int(input[i][j][0], 16)][int(input[i][j][1], 16)]

    return input


def round_key_generation(w):
    for count_w in range(len(w), len(w) + 4):
        w_ = ''
        w.append(w_)

        if count_w % 4 == 0:
            w_ = RotWord(w[count_w - 1])
            w_ = wrap(w_, 2)
            w_ = SubWord(w_)
            Rcon_ = Rcon[int(count_w / 4)]
            w_ = XOR_with_Rcon(w_, Rcon_)

        if w_ == '':
            w_ = w[count_w - 1]

        for i in range(len(w[count_w - 4])):
            w[count_w] += str(hex((int(w_[i], 16) ^ int(w[count_w - 4][i], 16)))[2:])

    return w


def ShiftRows(input):
    input_ = []
    for j in range(len(input)):
        input_.append([i[j] for i in input][j:] + [i[j] for i in input][:j])

    for j in range(len(input_)):
        input[j] = ([i[j] for i in input_])

    return input


def InvShiftRows(input):
    input_ = []

    for j in range(len(input)):
        input_.append([i[j] for i in input][len(input) - j:] + [i[j] for i in input][:len(input) - j])

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


def InvMixColumns(input):
    input_ = ''
    r = generation_array(4, 4)

    for i in range(len(input)):
        r[i][0] = '0' * (2 - len(hex(int(multiply_by_14[int(input[i][0][0], 16)][int(input[i][0][1], 16)], 16) ^ int(multiply_by_11[int(input[i][1][0], 16)][int(input[i][1][1], 16)], 16) ^ int(multiply_by_13[int(input[i][2][0], 16)][int(input[i][2][1], 16)], 16) ^ int(multiply_by_9[int(input[i][3][0], 16)][int(input[i][3][1], 16)], 16))[2:])) + hex(int(multiply_by_14[int(input[i][0][0], 16)][int(input[i][0][1], 16)], 16) ^ int(multiply_by_11[int(input[i][1][0], 16)][int(input[i][1][1], 16)], 16) ^ int(multiply_by_13[int(input[i][2][0], 16)][int(input[i][2][1], 16)], 16) ^ int(multiply_by_9[int(input[i][3][0], 16)][int(input[i][3][1], 16)], 16))[2:]
        r[i][1] = '0' * (2 - len(hex(int(multiply_by_9[int(input[i][0][0], 16)][int(input[i][0][1], 16)], 16) ^ int(multiply_by_14[int(input[i][1][0], 16)][int(input[i][1][1], 16)], 16) ^ int(multiply_by_11[int(input[i][2][0], 16)][int(input[i][2][1], 16)], 16) ^ int(multiply_by_13[int(input[i][3][0], 16)][int(input[i][3][1], 16)], 16))[2:])) + hex(int(multiply_by_9[int(input[i][0][0], 16)][int(input[i][0][1], 16)], 16) ^ int(multiply_by_14[int(input[i][1][0], 16)][int(input[i][1][1], 16)], 16) ^ int(multiply_by_11[int(input[i][2][0], 16)][int(input[i][2][1], 16)], 16) ^ int(multiply_by_13[int(input[i][3][0], 16)][int(input[i][3][1], 16)], 16))[2:]
        r[i][2] = '0' * (2 - len(hex(int(multiply_by_13[int(input[i][0][0], 16)][int(input[i][0][1], 16)], 16) ^ int(multiply_by_9[int(input[i][1][0], 16)][int(input[i][1][1], 16)] , 16)^ int(multiply_by_14[int(input[i][2][0], 16)][int(input[i][2][1], 16)], 16) ^ int(multiply_by_11[int(input[i][3][0], 16)][int(input[i][3][1], 16)], 16))[2:])) + hex(int(multiply_by_13[int(input[i][0][0], 16)][int(input[i][0][1], 16)], 16) ^ int(multiply_by_9[int(input[i][1][0], 16)][int(input[i][1][1], 16)] , 16)^ int(multiply_by_14[int(input[i][2][0], 16)][int(input[i][2][1], 16)], 16) ^ int(multiply_by_11[int(input[i][3][0], 16)][int(input[i][3][1], 16)], 16))[2:]
        r[i][3] = '0' * (2 - len(hex(int(multiply_by_11[int(input[i][0][0], 16)][int(input[i][0][1], 16)], 16) ^ int(multiply_by_13[int(input[i][1][0], 16)][int(input[i][1][1], 16)], 16) ^ int(multiply_by_9[int(input[i][2][0], 16)][int(input[i][2][1], 16)] , 16)^ int(multiply_by_14[int(input[i][3][0], 16)][int(input[i][3][1], 16)], 16))[2:])) + hex(int(multiply_by_11[int(input[i][0][0], 16)][int(input[i][0][1], 16)], 16) ^ int(multiply_by_13[int(input[i][1][0], 16)][int(input[i][1][1], 16)], 16) ^ int(multiply_by_9[int(input[i][2][0], 16)][int(input[i][2][1], 16)] , 16)^ int(multiply_by_14[int(input[i][3][0], 16)][int(input[i][3][1], 16)], 16))[2:]

        input_ += r[i][0] + r[i][1] + r[i][2] + r[i][3]

    input_ = str_to_array(input_)


    return input_

def generation_array(size1, size2):
    array = [[0] * size1 for i in range(size2)]

    return array


def AddRoundKey(input, w):
    input_str = ''

    for i in range(len(input)):
        for j in range(len(input[i])):
            for k in input[i][j]:
                input_str += hex(int(input[i][j], 16) ^ int(w[i][j], 16))[2:]

    input = str_to_array(input_str)

    return input


def str_to_array(input):
    input_ = generation_array(4, 4)
    input = wrap(input, 2)

    for i in range(len(input_)):
        for j in range(len(input_[i])):
            input_[i][j] = input[i * 4 + j]

    return input_


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


def encryption(input, key):
    input = wrap(input, 8)
    w = wrap(key, 8)
    input_ = generation_array(4, 4)
    j = 0
    w_ = w

    for i in range(11):
        if i > 0:
            input = SubBytes(input_, True)
            input = ShiftRows(input)
            w = round_key_generation(w)
            w_ = w[4 * i:]

            if j < 9:
                input = MixColumns(input)
                j += 1
            else:
                input = array_to_str8(input)

        input_ = AddRoundKey(input, w_)
        print(input_)
    input_ = array_to_str(input_)

    return input_


def decryption(input, key):
    input = wrap(input, 8)
    w = wrap(key, 8)

    for i in range(10):  # генерация всего ключа
        w = round_key_generation(w)

    for i in range(11):

        input = AddRoundKey(input, w[44 - 4 * (i + 1):44 - 4 * i])
        if i < 10:
            if i > 0:
                input = InvMixColumns(input)

            input = InvShiftRows(input)
            input = SubBytes(input, False)
            input = array_to_str(input)
            input = wrap(input, 8)

    input = array_to_str(input)
    return input

input = '3243f6a8885a308d313198a2e0370734'
key = '2b7e151628aed2a6abf7158809cf4f3c'

encrypted_message = encryption(input, key)
print('Зашифрованное сообщение:', encrypted_message)

decrypted_message = decryption(encrypted_message, key)
print('Расшифрованное сообщение:', decrypted_message)
