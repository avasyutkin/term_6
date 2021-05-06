import random


def public_key(n, a, k):

    return a ** k % n


def key_exchange(n_a_ka):
    n_a_ka = n_a_ka.split()

    if len(n_a_ka) < 3:
        return 'Введите три параметра n, a и секретный ключ.'

    if not n_a_ka[0].isnumeric():
        return 'Значение параметра n должно быть целым числом.'
    if not n_a_ka[1].isnumeric():
        return 'Значение параметра a должно быть целым числом.'
    if not n_a_ka[2].isnumeric():
        return 'Значение секретного ключа должно быть целым числом.'

    n = int(n_a_ka[0])
    a = int(n_a_ka[1])
    ka = int(n_a_ka[2])

    if a >= n:
        return 'Значение параметра a должно быть меньше n.'
    if ka >= n:
        return 'Значение секретного ключа должно быть меньше n.'

    if public_key(n, a, ka) == ka:
        return 'Открытый ключ равен секретному. Введите новый секретный ключ.'

    ya = public_key(n, a, ka)
    kb = random.randint(2, n - 1)
    yb = public_key(n, a, kb)

    if yb ** ka % n == ya ** kb % n:
        return 'Общий секретный ключ: ' + str(yb ** ka % n) + '\nОткрытый ключ собеседника: ' + str(yb)
    else:
        return 'Что-то пошло не так: ' + str(yb ** ka % n) + ' ' + str(ya ** kb % n) + '\nОткрытый ключ собеседника: ' + str(yb)
