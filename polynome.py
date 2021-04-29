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
            for k in range len(mnog1):#проход по созданному списку 
                if mnog1[i] != ' ' and mnog1[i] != '/': #если значения списка цифры
                    mnog1[i] = int(mnog1[i]) # переводим символы в цифры
            i = i + 1 #увеличиваем счётчик
            count1 = i
        while(j != ' ' and j < len(stroka2)): #аналогичные действия для второго полинома
            j += 1
        if stroka2[j] == ' ':
            mnog2 = list(stroka2[count2:j])
            k=0
            for k in range len(mnog2):
                if mnog2[i] != ' ' and mnog2[i] != '/':
                    mnog2[i] = int(mnog2[i])
            j = j + 1
            count2 = j
        if (i != len(stroka1)) or (j != len(stroka2)) #если не дошли до конца 
            rez = rez + SUBB_QQ_Q(mnog1,mnog2) + [' '] #прибавляем к списку разность коэффицентов полиномов
        else :
            rez = rez + SUBB_QQ_Q(mnog1,mnog2) #тоже самое ,только без пробела после последнего элемента

    result="".join(map(str,rez)) #склеивеаем в строку
