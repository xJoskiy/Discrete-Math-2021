import natural as nat
import integer as integer


def INT_Q_B(Q):
    if nat.MOD_NN_N(integer.ABS_Z_N(Q[0]), Q[1]) == [0]:
        return True
    else:
        return False
    # Гурьянов Савелий Функция возвращает отрицание результата остатка от деления числителя, преобразованного к
    # натуральному числу, на натуральный знаменатель, если остаток равен нулю, то дробь преобразуется к натуральному
    # числу, иначе не преобразуется и вернётся 0


def RED_Q_Q(Q):
    #Гурьянов Савелий
    #Сокращение дроби
    result = [[0],[0]]
    nod = nat.GCF_NN_N(ABS_Z_N(Q[0]),ABS_Z_N(Q[1]))#нод числителя и знаменателя
    result[0] = integer.DIV_ZZ_Z(Q[0],nod)#делим числитель на нод
    result[1] = integer.DIV_ZZ_Z(Q[1],nod)#делим знаменатель на нод
    return result


def ADD_QQ_Q(list1, list2):
    # Пекло Елизавета
    # Сложение дробей
    i = 0
    while list1[i] != "/":
        i = i + 1
    ch1 = list1[1:i]
    zn1 = list1[i + 1:]
    i = 0
    while list2[i] != "/":
        i = i + 1
    ch2 = list2[1:i]
    zn2 = list2[i + 1:]
    # ptr1, ptr2 - хранят знаки чисел
    prt1 = list1[0]
    prt2 = list2[0]
    # НОК и есть новый знаменатель дробей
    nok = nat.LCM_NN_N(zn1, zn2)
    # Находим множители при числителях дробей
    mn1 = integer.DIV_ZZ_Z([0] + nok, [0] + zn1)
    mn2 = integer.DIV_ZZ_Z([0] + nok, [0] + zn2)
    # Находим сами числители, а затем и их сумму
    ch1_new = integer.MUL_ZZ_Z([0] + ch1, mn1)
    ch2_new = integer.MUL_ZZ_Z([0] + ch2, mn2)
    ch1_new[0] = prt1
    ch2_new[0] = prt2
    newCh = integer.ADD_ZZ_Z(ch1, ch2)
    # Возвращаем новые числитель и знаменатель
    return newCh + ['/'] + nok


def TRANS_Q_Z(list):
    # Преобразование дробного в целое (если знаменатель равен 1)
    i = 0
    while list[i] != '/':
        i = i + 1
    newList = list[:i]
    return newList


def DIV_QQ_Q(rational1, rational2):
    # Деление дробей
    # Кривоконь Максим
    result = [[0], [0]]
    result[0] = MUL_ZZ_Z(rational1[0], rational2[1])  # умножение числителя на знаменатель
    result[1] = MUL_ZZ_Z(rational1[1], rational2[0])  # умножение знаменателя на числитель
    res = RED_Q_Q(result)  # сокращение дроби
    return res

def MUL_QQ_Q(rational1, rational2):  # на вход функция получает 2 рациональных числа
    # Семёнов Михаил
    # Умножение дробей
    result = [[0], [0]] # результат умножения
    result[0] = MUL_ZZ_Z(rational1[0],rational2[0]) # умножение числителей
    result[1] = MUL_ZZ_Z(rational1[1],rational2[1]) # умножение знаменателей
    rez = RED_Q_Q(result) # сокращение дроби

def TRANS_Z_Q(x):
    # Артамонов Артур, гр.0306
    # Преобразование целого в дробное
    x.append('/')
    x.append(1)
    return x


def TRANS_Q_Z(x):
    # Артамонов Артур, гр.0306
    # Преобразование дробного в целое, если знам. = 1
    if x[-1] == 1:
        if x[-2] == '/':
            x = x[:-2]
    return x


def SUB_QQ_Q(list1, list2):
    # Дашкин Дамир
    # Вычитание дробей
    k1 = list1[0]
    k2 = list2[0]
    znam = nat.LCM_NN_N(k1, k2)
    add1 = nat.DIV_NN_N(znam, k1)
    add2 = nat.DIV_NN_N(znam, k2)
    chisl1 = integer.MUL_ZZ_Z(add1, list1[1])
    chisl2 = integer.MUL_ZZ_Z(add2, list2[1])
    result = integer.SUB_ZZ_Z(chisl1, chisl2)
    res = [0]*2
    res[0] = result
    res[1] = znam
    return res


def INT_Q_B(A):
    # Аносов Павел
    # Проверка на целое
    i = 0
    x = []
    while A[i] != '/':
        x.append(A[i])
    y = A[i + 1:]
    if nat.MOD_NN_N(x, y) == 0:
        return "Да"
    else:
        return "Нет"






