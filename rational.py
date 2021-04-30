def INT_Q_B(Q):
    numerator = Q[0]
    denominator = Q[1]
    return not MOD_NN_N([numerator[1], numerator[2]], denominator)
# Гурьянов Савелий
# Функция возвращает отрицание результата остатка от деления числителя, преобразованного к натуральному числу,
# на натуральный знаменатель, если остаток равен нулю, то дробь преобразуется к натуральному числу, иначе не преобразуется и вернётся 0


def RED_Q_Q(Q):
    Q[0] = DIV_ZZ_Z(Q[0], [0] + GCF_NN_N(ABS_Z_N(Q[0]), Q[1]))
    Q[1] = DIV_ZZ_Z([0] + Q[1], [0] + GCF_NN_N(ABS_Z_N(Q[0]), Q[1]))[1:]
    return [Q[0], Q[1]]
# Гурьянов Савелий
# Числитель и знаменатель делятся на НОД знаменателя и числителя(числитель преобразуется к натуральному числу при помощи
# функции ABS_Z_N)

def ADD_QQ_Q(list1, list2):
# Пекло Елизавета
# Сложение дробей
    i=0
    while list1[i] != "/":
        i=i+1
    ch1 = list1[1:i]
    zn1 = list1[i+1:]
    i=0
    while list2[i] != "/":
        i=i+1
    ch2 = list2[1:i]
    zn2 = list2[i+1:]
# ptr1, ptr2 - хранят знаки чисел
    prt1 = list1[0]
    prt2 = list2[0]
# НОК и есть новый знаменатель дробей
    nok = LCM_NN_N(zn1, zn2)
# Находим множители при числителях дробей
    mn1 = DIV_ZZ_Z([0]+nok, [0]+zn1)
    mn2 = DIV_ZZ_Z([0]+nok, [0]+zn2)
# Находим сами числители, а затем и их сумму
    ch1_new = MUL_ZZ_Z([0]+ch1, mn1)
    ch2_new = MUL_ZZ_Z([0]+ch2, mn2)
    ch1_new[0] = ptr1
    ch2_new[0] = ptr2
    newCh = ADD_ZZ_Z(ch1, ch2)
# Возвращаем новые числитель и знаменатель
    return newCh + ['/'] + nok

def TRANS_Q_Z(list):
# Преобразование дробного в целое (если знаменатель равен 1)
    while(list[i]!='/'):
        i=i+1
    newList=list[:i]
    return newList

