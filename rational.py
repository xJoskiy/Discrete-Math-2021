import natural as nat
import integer as integer

def strtomas(str):
    i = 0
    tmp = 0

    while(i < len(str)):
        if str[i] == 'x':
            if i == len(str)-1:
                str = str + '^1'
            elif str[i+1] == '+' or str[i+1] == '-':
                str = str[:i+1] + '^1'+str[i+1:]
            if i == 0:
                str = '1' + str
            elif str[i-1] == '+' or str[i-1] == '-':
                str = str[:i] + '1' + str[i:]
        if ord(str[len(str)-1]) > 47 and ord(str[len(str)-1]) < 58:
            t = len(str)-1
            while(str[t] != '^' and str[t] != '-' and str[t] != '+' and t != 0 and tmp == 0):
                t -= 1
            if str[t] == '-' or str[t] == '+' or t == 0:
                str = str+'x^0'
                tmp = 1
        i += 1
    mas = list(str)
    print(mas)
    mas_result = []
    mas_stepen = []
    for i in range(len(mas)):
        if mas[i] != '-' and mas[i] != '+' and mas[i] != '^' and mas[i] != 'x' and mas[i] != '/':
            mas[i] = ord(mas[i])-48
    i = 0
    t = 0
    p = 0
    k = 0
    j = 0
    flag = 0
    while(i<len(mas)):
        if mas[i] == '-':
           p = 1
        if mas[i] == '/':
            flag = 1
            k = i
        if mas[i] == 'x':
            j = t
            if flag == 0:
                if p == 1 and j != 0:
                    j = t - 1
                    p = 0
                mas_result.append([mas[j:i], [1]])
            else:
                if p == 1 and j != 0:
                    j = t - 1
                    p = 0
                mas_result.append([mas[j:k], mas[k+1:i]])
                flag = 0
            j = i+1
        if mas[i] == '^':
            t = i
            while((mas[t] != '-' and mas[t] != '+') and t != len(mas)-1):
                t += 1
            if t != len(mas)-1:
                mas_stepen.append(mas[i+1:t])
            else:
                mas_stepen.append(mas[i+1:])
            t = t+1
            i = t - 2
        i += 1
    return mas_result, mas_stepen
str = input()
a, b = strtomas(str)
print(a)
print(b)

def INT_Q_B(Q):
    return not nat.NZER_N_B(nat.MOD_NN_N(integer.ABS_Z_N(Q[0]), Q[1]))
    # Гурьянов Савелий
    # Проверка на целое


def RED_Q_Q(Q):
    # Гурьянов Савелий
    # Сокращение дроби
    if integer.POZ_Z_D(Q[0]):
        nod = nat.GCF_NN_N(integer.ABS_Z_N(Q[0]), integer.ABS_Z_N(Q[1]))
        Q[0] = integer.DIV_ZZ_Z(Q[0], nod)
        Q[1] = integer.DIV_ZZ_Z(Q[1], nod)
        return TRANS_Q_Z(Q)
    else:
        return [0]


def ADD_QQ_Q(list1, list2):
    # Пекло Елизавета
    # Сложение дробей
    mul = nat.LCM_NN_N(list1[1], list2[1])          # НОД знаменателей
    mul1 = nat.DIV_NN_N(mul, list1[1])              # Сопряженное к первому знаменателю
    mul2 = nat.DIV_NN_N(mul, list2[1])              # Сопряженное ко второму знаменателю
    firstNum = integer.MUL_ZZ_Z(list1[0], mul1)     # Первое слагаемое нового числителя
    secNum = integer.MUL_ZZ_Z(list2[0], mul2)       # Второе
    numerator = integer.ADD_ZZ_Z(firstNum, secNum)  # Числитель, как сумма этих слагаемых
    denominator = mul                               # НОД знаменателей - новый знаменатель

    return RED_Q_Q([numerator, denominator])        # Сокращаем полученную дробь


def DIV_QQ_Q(rational1, rational2):
    # Деление дробей
    # Кривоконь Максим
    result = [[0], [0]]
    result[0] = integer.MUL_ZZ_Z(rational1[0], rational2[1])  # умножение числителя на знаменатель
    result[1] = integer.MUL_ZZ_Z(rational1[1], rational2[0])  # умножение знаменателя на числитель
    if integer.POZ_Z_D(result[0]) == '-' and integer.POZ_Z_D(result[1]) == '-':
        result[0] = integer.MUL_ZM_Z(result[0])
        result[1] = integer.MUL_ZM_Z(result[1])
    elif integer.POZ_Z_D(result[1]) == '-':
        result[1] = integer.ABS_Z_N(result[1])
        result[0] = integer.MUL_ZM_Z(result[0])

    return RED_Q_Q(result)  # сокращение дроби


def MUL_QQ_Q(rational1, rational2):  # на вход функция получает 2 рациональных числа
    # Семёнов Михаил
    # Умножение дробей
    result = [[0], [0]]  # результат умножения
    result[0] = integer.MUL_ZZ_Z(rational1[0], rational2[0])  # умножение числителей
    result[1] = integer.MUL_ZZ_Z(rational1[1], rational2[1])  # умножение знаменателей
    return RED_Q_Q(result)  # сокращение дроби


def TRANS_Q_Z(x):
    # Артамонов Артур, гр.0306
    # Преобразование дробного в целое, если знам. = 1
    if x[1][-1] == 1 and len(x[1]) == 1:
        return x[0]
    else:
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
    if nat.MOD_NN_N(integer.ABS_Z_N(A[0]), A[1]) == [0]:
        return True
    else:
        return False






