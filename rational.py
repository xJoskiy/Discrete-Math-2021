import natural as nat
import integer as integer


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






