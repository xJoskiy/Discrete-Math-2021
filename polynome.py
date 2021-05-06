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


def LED_P_Q(str):
    # Пекло Елизавета
    # Нахождение старшего коэффициента многочлена
    list1 = ''
    i = 0
    while list0[i] != ' ':
        list1 = list1 + list0[i]
        i += 1
    return list1

def DEG_P_N(list):
# Пекло Елизавета
# Получение степени многочлена
# Степень многочлена равна количеству пробелов в списке
    cnt = 0
    for x in list:
        if x == ' ':
            cnt = cnt + 1
    return cnt


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

  
def SUB_PP_P(stroka1,stroka2):
    #Семёнов Михаил
    #Вычитание многочленов
    i = 0
    rez = [] #создаём пустой список
    while (i != len(stroka1) and j != len(stroka2)):#условие прохода по двум многочленам
        while(i != ' ' and i < len(stroka1)):#пока не встретили пробел или не закончилась строка
            i += 1 #увеличиваем счётчик
        if stroka1[i]==' ': #если дошли до пробела
            mnog1 = list(stroka1[count1:i]) #создаём список ,состоящий из цифр числа коэффицента полинома
            k = 0
            for k in range(len(mnog1)):  #проход по созданному списку
                if mnog1[i] != ' ' and mnog1[i] != '/': #если значения списка цифры
                    mnog1[i] = int(mnog1[i]) # переводим символы в цифры
            i = i + 1 #увеличиваем счётчик
            count1 = i
        while(j != ' ' and j < len(stroka2)): #аналогичные действия для второго полинома
            j += 1
        if stroka2[j] == ' ':
            mnog2 = list(stroka2[count2:j])
            k=0
            for k in range(len(mnog2)):
                if mnog2[i] != ' ' and mnog2[i] != '/':
                    mnog2[i] = int(mnog2[i])
            j = j + 1
            count2 = j
        if (i != len(stroka1)) or (j != len(stroka2)): #если не дошли до конца
            rez = rez + SUBB_QQ_Q(mnog1,mnog2) + [' '] #прибавляем к списку разность коэффицентов полиномов
        else :
            rez = rez + SUBB_QQ_Q(mnog1,mnog2) #тоже самое ,только без пробела после последнего элемента

    result="".join(map(str,rez)) #склеивеаем в строку

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

def MUL_Pxk_P(polynome2,k):
    #Дашкин Дамир
    #Умножение многочлена на x^k
    for i in range(len(polynome2)):
        polynome2[i] = nat.ADD_NN_N(polynome2[i], k)
    return polynome2

