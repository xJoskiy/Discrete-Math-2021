import natural as nat

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


def LED_P_Q(listCff):
# Пекло Елизавета
#Нахождение старшего коэффициента многочлена
    return listCff[0]

def DEG_P_N(listSt):
# Пекло Елизавета
# Получение степени многочлена
    return listSt[0]

  


def ADD_PP_P(x, y):
    # Кривоконь Максим
    # Сложение многочленов
    res = ""  # Результат
    prdx = x.split(' ')
    prdy = y.split(' ')
    i = len(prdx)
    prdx.reverse() 
    prdy.reverse()
    if (len(prdx) < len(prdy)):  # Если кол-во коэффициентов в первой переменной меньше, чем во второй, то
        while (i != len(prdy)):  # записываем их нулями - "00"
            prdx.insert(0, str('00'))
            i = i + 1
    i = len(prdy)
    if (len(prdy) < len(prdx)):  # Если кол-во коэффициентов во второй переменной меньше, чем в первой, то
        while (i != len(prdx)):  # записываем их нулями - "00"
            prdy.insert(0, str('00'))
            i = i + 1
    prdx.reverse()
    prdy.reverse()
    i = 0
    print(prdx)
    print(prdy)
    while (i != len(prdx)):
        res = res + ADD_QQ_Q((prdx[i]+"/1"), (prdy[i]+"/1")) + " "  # Получаем итоговый результат сложения
        i = i + 1
    return res


def SUB_PP_P(list1,list2,stepen1,stepen2)
    for i in range(len(list2)):
        if list2[i][0][0] == '-':
            list2[i][0] = list2[i][0][1:]
        else:
            list2[i][0] = ['-'] + list2[i][0]
    return(ADD_PP_P(list1,list2,stepen1,stepen2))

def MUL_Pxk_P(polynome2,k):
    #Дашкин Дамир
    #Умножение многочлена на x^k
    for i in range(len(polynome2)):
        polynome2[i] = nat.ADD_NN_N(polynome2[i], k)
    return polynome2

