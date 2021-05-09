import natural as nat
import rational as rat
import integer


def MUL_PQ_P(coefficient, Q):
    # Гурьянов Савелий
    # Каждый коэффициент многочлена циклично умножается на переданное рациональное число
    for index in range(len(coefficient)):
        coefficient[index] = rat.MUL_QQ_Q(coefficient[index], Q)
    return coefficient


def GCF_PP_P(P1, P2):
    # Гурьянов Савелий
    # Реализуется алгоритм Евклида для многочленов: пока степень меньшего многочлена неотрицательна,
    # в больший многочлен переписывается меньший, а в меньший - остаток от деления большего на меньший
    if DEG_P_N(P1) >= DEG_P_N(P2):
        while DEG_P_N(P2) != 0:
            P1, P2 = P2, MOD_PP_P(P1, P2)
        return P1
    else:
        return GCF_PP_P(P2, P1)


def NMR_P_P(P):
    # Гурьянов Савелий
    # Многочлен делится на НОД многочлена и производной
    P = DIV_PP_P(P, GCF_PP_P(P, DER_P_P(P)))
    return P


def LED_P_Q(coefficient):
    # Пекло Елизавета
    # Нахождение старшего коэффициента многочлена
    return coefficient[0]


def DEG_P_N(power):
    # Пекло Елизавета
    # Получение степени многочлена
    return power[0]


def MUL_Pxk_P(power, k):
    # Дашкин Дамир
    # Умножение многочлена на x^k
    for i in range(len(power)):
        power[i] = nat.ADD_NN_N(power[i], k)
    return power


def MUL_PP_P(koefs_1, powers_1, koefs_2, powers_2):
    # Артамонов Артур, гр.0306
    # Умножение многочленов

    new_koefs = []
    new_powers = []

    for i in range(len(koefs_1)):
        for j in range(len(koefs_2)):
            k = rat.MUL_QQ_Q(koefs_1[i], koefs_2[j])

            n = nat.ADD_NN_N(powers_1[i], powers_2[j])

            new_koefs.append(k)
            new_powers.append(n)

    super_new_powers = []
    super_new_koefs = []

    deleted = set()
    t = [[0], [1]]
    for i in range(len(new_powers)):
        x = new_powers[i]
        if new_powers.count(x) > 1:
            q = i
            for j in range(q + 1, len(new_powers)):
                if new_powers[j] == x:
                    k = rat.ADD_QQ_Q(new_koefs[q], new_koefs[j])
                    t = rat.ADD_QQ_Q(t, k)

            if new_powers[i][0] not in deleted:
                super_new_koefs.append(t)
                super_new_powers.append(new_powers[i])
                deleted.add(new_powers[i][0])

        else:
            super_new_koefs.append(new_koefs[i])
            super_new_powers.append(new_powers[i])

    n = len(super_new_powers)
    for j in range(n - 1):
        for i in range(n - j - 1):
            if super_new_powers[i][0] < super_new_powers[i + 1][0]:
                super_new_powers[i], super_new_powers[i + 1] = super_new_powers[i + 1], super_new_powers[i]
                super_new_koefs[i], super_new_koefs[i + 1] = super_new_koefs[i + 1], super_new_koefs[i]

    return super_new_koefs, super_new_powers


def SUB_PP_P(list1, stepen1, list2, stepen2):
    for i in range(stepen1):
        list1[i][0] = integer.MUL_ZM_Z(list1[i][0])
    return ADD_PP_P(list1, stepen1, list2, stepen2)


def DER_P_P(coefficient, power):
    # Производная многочлена
    # Аносов Павел
    for i in range(len(power)):
        coefficient[i] = rat.MUL_QQ_Q(coefficient[i], rat.TRANS_Z_Q(power[i]))
        power[i] = nat.SUB_NN_N(power[i], [1])
    return coefficient, power


def DIV_PP_P(coefficient1, power1, coefficient2, power2):
    new_power = []
    new_coefficient = []
    while nat.DIV_NN_N(power1, power2) >= 0:
        new_power.append(nat.DIV_NN_N(power1, power2))
        new_coefficient.append(rat.DIV_QQ_Q(coefficient1, coefficient2))
        coefficient1, power1 = SUB_PP_P(coefficient1, power1, new_power, new_coefficient)
    return new_coefficient, new_power

# [1, 2, 3, 5]  1235
# ['-', 1, 2, 4]  -124
# [['-', 2, 3], [6, 4]]
# [[['-', 1, 2], [4, 5]], [1, 2], [1]]] [[2], [0]]

