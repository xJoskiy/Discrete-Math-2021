

        else:
            s += str1[i]
    return s


def MUL_PQ_P(P, Q):
    for index in range(0, P[0]):
        P[1][index] = MUL_PQ_P(P[1][index], Q)
    return P
# Гурьянов Савелий
# Каждый коэффициент многочлена циклично умножается на переданное рациональное число



def GCF_PP_P(P1, P2):
    if DEG_P_N(P1) >= DEG_P_N(P2):
        while (DEG_P_N(P2) != 0):
            P1, P2 = P2, MOD_PP_P(P1, P2)
        return P1
    else:
        return GCF_PP_P(P2, P1)
# Гурьянов Савелий
# Реализуется алгоритм Евклида для многочленов: пока степень меньшего многочлена неотрицательна,
# в больший многочлен переписывается меньший, а в меньший - остаток от деления большего на меньший

def LED_P_Q(str):
# Пекло Елизавета
#Нахождение старшего коэффициента многочлена
    str0 = Changing_str(str)
    str1 = ''
    i = 0
    while str0[i] != ' ':
        str1 = str1 + str0[i]
        i += 1
    return str1

def DEG_P_N(str):
# Пекло Елизавета
# Получение степени многочлена
# Степень многочлена равна количеству пробелов в списке
    str0 = Changing_str(str)
    cnt = 0
    i = 0
    for i in range(len(str0)):
        if str0[i] == ' ':
            cnt = cnt + 1
    return cnt
