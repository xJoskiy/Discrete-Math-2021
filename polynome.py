import natural as nat
import rational as rat
import integer


def PolToStr(list_result, list_stepen):
    seq = ''
    for i in range(len(list_result)):
        if list_result[i][0] == [0]:
            list_result.pop(i)
            list_stepen.pop(i)
    for i in range(len(list_result)):
        for j in range(len(list_result[i])):
            for k in range(len(list_result[i][j])):
                if list_result[i][j][k] != '-':
                    list_result[i][j][k] = chr(list_result[i][j][k] + 48)
                seq = seq + list_result[i][j][k]
            if not j:
                seq = seq + '/'
        seq = seq + 'x'
    i = 0
    while i < len(seq):
        if i < len(seq) - 2:
            if seq[i] == '/' and seq[i + 1] == '1' and seq[i + 2] == 'x':
                seq = seq[:i] + seq[i + 2:]
        if i < len(seq) - 1:
            if seq[i] == 'x' and 47 < ord(seq[i + 1]) < 58:
                seq = seq[:i + 1] + '+' + seq[i + 1:]
        i += 1
    i = tmp = 0
    flag = -1
    while i < len(seq):
        if seq[i] == 'x':
            flag += 1
        if flag == tmp and seq[i] == 'x':
            string = ''
            for t in range(len((list_stepen[tmp]))):
                list_stepen[tmp][t] = chr(list_stepen[tmp][t] + 48)
                string = string + list_stepen[tmp][t]
            if string != '1' and string != '0':
                seq = seq[:i + 1] + '^' + string + seq[i + 1:]
            elif string == '0':
                seq = seq[:len(seq) - 1]
            tmp += 1
        i += 1
    i = 0
    while i < len(seq) - 1:
        if seq[i] == '1':
            if i == 0 and seq[i + 1] == 'x':
                seq = seq[i + 1:]
            elif seq[i + 1] == 'x' and (seq[i - 1] == '-' or seq[i - 1] == '+') and i < len(seq) - 2:
                seq = seq[:i] + seq[i + 1:]
        i += 1
    return seq

# Polynomials are represented by two lists: coefficients and powers
# Each coefficient is a rational number
# Each power is a natural number
# [ [ ['-', 1, 2], [4, 5] ], [ [1, 2], [1] ], [ ['-', 6], [1] ] ] : [ [1, 1], [4], [0] ]   -12/45x^12x^4-6


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
        power[i] = nat.ADD_NN_N(power[i], k)   # Степень каждого члена увеличиваем на k единиц
    return power


def MUL_PP_P(koefs_1, powers_1, koefs_2, powers_2):
    # Артамонов Артур, гр.0306
    # Умножение многочленов

    new_koefs = []
    new_powers = []

    for i in range(len(koefs_1)):
        for j in range(len(koefs_2)):
            k = rat.MUL_QQ_Q(koefs_1[i], koefs_2[j])            # Умножаем фонтанчиком
            n = nat.ADD_NN_N(powers_1[i], powers_2[j])          # коэффициенты и степени

            new_koefs.append(k)
            new_powers.append(n)

    super_new_powers = []
    super_new_koefs = []

    deleted = set()
    t = [[0], [1]]
    # Складываем одночлены с одинаковыми степенями
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
    # Сортировка пузырьком
    n = len(super_new_powers)
    for j in range(n - 1):
        for i in range(n - j - 1):
            a = int(''.join(map(str, super_new_powers[i])))
            b = int(''.join(map(str, super_new_powers[i + 1])))
            if a < b:
                super_new_powers[i], super_new_powers[i + 1] = super_new_powers[i + 1], super_new_powers[i]
                super_new_koefs[i], super_new_koefs[i + 1] = super_new_koefs[i + 1], super_new_koefs[i]

    return super_new_koefs, super_new_powers


def SUB_PP_P(list1, stepen1, list2, stepen2):
    # Вычитание многочленов
    # Семёнов Михаил
    for i in range(len(stepen2)):
        list2[i][0] = integer.MUL_ZM_Z(list2[i][0])     # Все коэффициенты домножаем на -1 и складываем
    return ADD_PP_P(list1, stepen1, list2, stepen2)


def DER_P_P(coefficient, power):
    # Производная многочлена
    # Аносов Павел
    for i in range(len(power)):
        coefficient[i] = rat.MUL_QQ_Q(coefficient[i], rat.TRANS_Z_Q(power[i]))  # Коэффициенты домножаем на степени
        power[i] = nat.SUB_NN_N(power[i], [1])                                  # Степени уменьшаем на единицу
    return coefficient, power


def DIV_PP_P(coefficient1, power1, coefficient2, power2):
    # Деление многочленов
    # Аносов Павел
    new_power = []
    new_coefficient = []
    try:
        while integer.SUB_ZZ_Z(power1[0], power2[0]) != ['-', 1] and power1:
            new_power.append(nat.SUB_NN_N(power1[0], power2[0]))
            new_coefficient.append(rat.DIV_QQ_Q(coefficient1[0], coefficient2[0]))
            coef, pow = MUL_PP_P(coefficient2, power2, [new_coefficient[-1]], [new_power[-1]])
            coefficient1, power1 = SUB_PP_P(coefficient1, power1, coef, pow)

            del coefficient1[0]
            del power1[0]
    except:
        pass
    return new_coefficient, new_power


def ADD_PP_P(koefs_1, powers_1, koefs_2, powers_2):

    new_koefs = []
    new_powers = []

    if len(powers_2) > len(powers_1):
        koefs_1, koefs_2 = koefs_2, koefs_1
        powers_1, powers_2 = powers_2, powers_1

    for i in range(len(powers_1)):
        x = powers_1[i]
        c = koefs_1[i]

        q = 0
        for j in range(len(powers_2)):
            if q != -1:
                q += 1
            if powers_2[j] == x:
                q = -1
                k = rat.ADD_QQ_Q(koefs_2[j], c)
                new_koefs.append(k)
                new_powers.append(powers_2[j])

        if q == len(powers_2):
            new_koefs.append(c)
            new_powers.append(x)

    for i in range(len(powers_2)):
        x = powers_2[i]
        c = koefs_2[i]

        q = 0
        for j in range(len(powers_1)):
            if q != -1:
                q += 1
            if powers_1[j] == x:
                q = -1

        if q == len(powers_1):
            new_koefs.append(c)
            new_powers.append(x)


    n = len(new_powers)
    for j in range(n - 1):
        for i in range(n - j - 1):
            a = int(''.join(map(str, new_powers[i])))
            b = int(''.join(map(str, new_powers[i + 1])))
            if a < b:
                new_powers[i], new_powers[i + 1] = new_powers[i + 1], new_powers[i]
                new_koefs[i], new_koefs[i + 1] = new_koefs[i + 1], new_koefs[i]

    return new_koefs, new_powers
