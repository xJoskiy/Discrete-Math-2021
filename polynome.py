import natural as nat
import rational as rat

def mastostr( list_result, list_stepen ):
    str = ''
    for i in range (len( list_result)):
        if  list_result[i][0] == [0] :
            list_result.pop(i)
            list_stepen.pop(i)
    for i in range(len(list_result)):
        for j in range(len(list_result[i])):
            for k in range(len(list_result[i][j])):
                if list_result[i][j][k] != '-':
                    list_result[i][j][k] = chr(list_result[i][j][k] + 48)
                str = str + list_result[i][j][k]
            if j == 0:
                str = str + '/'
        str = str + 'x'
    i = 0
    while ( i < len(str) ):
        if i < len(str)-2:
            if str[i] == '/' and str[i+1] == '1' and str[i+2] == 'x':
                str = str[:i] + str[i+2:]
        if i < len(str)-1:
            if str[i] == 'x' and ord(str[i+1]) > 47 and ord(str[i+1]) < 58:
                str = str[:i+1] + '+' + str[i+1:]
        i += 1
    i = 0
    tmp = 0
    flag = -1
    j = 0
    while ( i < len(str) ):
        if str[i] == 'x' :
            flag += 1
        if flag == tmp and str[i] == 'x':
            stroka = ''
            for t in range(len((list_stepen[tmp]))):
                list_stepen[tmp][t] = chr(list_stepen[tmp][t]+48)
                stroka = stroka + list_stepen[tmp][t]
            if stroka != '1' and stroka != '0':
                str = str[:i + 1] + '^' + stroka + str[i+1:]
            elif stroka == '0':
                str = str[:len(str)-1]
            tmp += 1
        i += 1
    i = 0
    while ( i < len(str) - 1 ):
        if str[i] == '1':
            if i == 0 and str[i+1] == 'x':
                str = str[i+1:]
            elif str[i+1] == 'x' and (str[i-1] == '-' or str[i-1] == '+') and i < len(str) - 2:
                str = str[:i] + str[i+1:]
        i += 1
    return str

list_result = [[[1],[1]],[[0],[1]]]
list_stepen = [[5],[2]]
str = mastostr(list_result,list_stepen)
print(str)

def MUL_PQ_P(P, Q):
    # Гурьянов Савелий
    # Каждый коэффициент многочлена циклично умножается на переданное рациональное число
    for index in range(len(P[0])):
        P[0][index] = rat.MUL_QQ_Q(P[0][index], Q)
    return P


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

def LED_P_Q(listCff):
    # Пекло Елизавета
    # Нахождение старшего коэффициента многочлена
    return listCff[0]


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
    for i in range(len(list2)):
        if list2[i][0][0] == '-':
            list2[i][0] = list2[i][0][1:]
        else:
            list2[i][0] = ['-'] + list2[i][0]
    return ADD_PP_P(list1, stepen1, list2, stepen2)


