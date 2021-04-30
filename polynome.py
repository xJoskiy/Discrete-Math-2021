def MUL_Pxk_P(polynome1, polynome2):
    #Дашкин Дамир
    #Умножение многочлена на x^k
    res = ""
    str1 = Changing_str(polynome1)
    str2 = Changing_str(polynome2)
    k = 0
    i=0
    while i < len(polynome2):
        k += 1
        i += 2
    k -= 1
    res = str1[:] + k*" 00"
    return res
  

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

def LED_P_Q(list0):
# Пекло Елизавета
#Нахождение старшего коэффициента многочлена
    for (i != " ") in list0:
        list1 = list1 + i
    return list1

  
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

