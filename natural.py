# How numbers are represented:
# [1, 2, 3, 5]  1235
# [0] 0

def COM_NN_D(x, y):
    # Аносов Павел
    # Сравнение двух чисел
    if len(x) > len(y):  # Если первый список длиннее второго, то он число больше
        return 2
    elif len(x) < len(y):  # И наоборот
        return 1
    else:
        for i, k in zip(x, y):
            if i > k:  # Если цифра в большем разряде первого числа больше цифры во втором
                return 2  # То оно больше
            elif i < k:
                return 1
    return 0


def SUB_NN_N(list1, list2):
    # Вычитание из первого большего натурального числа второго меньшего или равного
    # Кривоконь Максим
    x = list1
    y = list2
    if COM_NN_D(x, y) == 0:  # Если числа равны, то из первого вычитаем второе
        if x[0] > y[0]:
            a1 = x
            a2 = y
        else:
            a1 = y
            a2 = x
    else:
        if COM_NN_D(x, y) == 2:  # Если первое больше второго, то из первого вычитаем второе
            while len(x) > len(y):
                y = [0] + y  # Добавляем нули до одинаковой длины
            a1 = x
            a2 = y
        else:  # Иначе из второго первое
            return [0]
    i1 = len(x) - 1  # Индекс последнего эл-та
    i2 = len(y) - 1  # Индекс последнего эл-та
    res = []  # Задаем список под новое число
    b = 0  # Занимаемый десяток
    while True:
        if i1 < 0 and i2 < 0:  # Если индекс меньше нуля, то завершаем цикл
            break
        q1 = int(a1[i1])  # Берем число, записанное в последнем эл-те
        q2 = int(a2[i2])  # Берем число, записанное в последнем эл-те
        q = q1 - b - q2  # Вычитаем последние эл-ты
        if q >= 0:  # Если результат больше нуля, то добавляем его в новый список на первое место и обнуляем b
            res.insert(0, q)
            b = 0
        else:  # Иначе прибавляем к числу десять и увеличиваем b
            q += 10
            b = 1
            res.insert(0, q)
        i1 -= 1  # Сдвигаемся на следующий эл-т
        i2 -= 1  # Сдвигаемся на следующий эл-т
    if all(x == res[0] == 0 for x in res):  # Если все элементы нули, то выводим один ноль
        res = [0]
    elif res[0] == 0:  # Если есть незначащие нули, то убираем их
        while res[0] == 0:
            res = res[1:]
    return res


def MUL_ND_N(list0, n):
    # Пекло Елизавета
    # Умножение натурального числа на цифру
    list2 = list0.copy()
    tmp1 = 0
    tmp2 = 0
    # Переворачиваем список для удобства
    list2.reverse()
    # Перебираем элементы списка
    for i in range(len(list2)):
        # Присваиваем текущему эл-ту [остаток от деления на 10 + целая часть от деления прошлого эл-та] и сохраняем
        # целую часть от деления текущего эл-та
        tmp1 = list2[i]
        list2[i] = list2[i] * n % 10 + tmp2
        # Если получили переполнение, отсекаем целую часть и переносим в следующий разряд
        if list2[i] > 9:
            tmp2 = tmp1 * n // 10
            tmp2 = tmp2 + list2[i]//10
            list2[i] = list2[i] % 10
        else:
            tmp2 = tmp1 * n // 10
    # Если при умножении последней цифры остается целая часть от деления, то добавляем эту целую часть в конец
    if tmp2 != 0:
        list2.append(tmp2)
    # Переворачиваем список
    list2.reverse()
    return list2


def SUB_NDN_N(nat1, nat2, number):
    # Семёнов Михаил
    # Вычитание из натурального числа другого натурального числа ,умноженного на цифру
    # Результат только для положительных значений
    nat0 = nat2
    nat2_mull_nd_n = MUL_ND_N(nat0, number)  # функция умножения второго числа на цифру
    if COM_NN_D(nat1, nat2_mull_nd_n) != 1:  # если первое число больше второго умноженного на цифру
        return SUB_NN_N(nat1, nat2_mull_nd_n)  # вычитаем из первого второе, умноженное на цифру


def DIV_NN_N(a, b):
    # Аносов Павел
    # Частное от деления большего натурального числа на меньшее или равное натуральное с остатком
    count = 0
    if not NZER_N_B(b):
        while True:
            if COM_NN_D(a, b) != 1:
                quot = DIV_NN_Dk(a, b.copy())
                sub = MUL_Nk_N(quot, b.copy())
                a = SUB_NN_N(a, sub)
                count += 10**quot
            else:
                break
    else:
        return ["Unable to calculate"]
    return list(map(int, str(count)))


def MUL_Nk_N(k, list0):
    # Пекло Елизавета
    # Умножение натурального целого на 10^k
    list1 = [0] * k
    list0.extend(list1)
    return list0


def MOD_NN_N(x, y):
    # Артамонов Артур, гр.0306
    # Остаток от деления большего натурального числа на меньшее или равное натуральное с
    # остатком(делитель отличен от нуля)
    ch = DIV_NN_N(x, y)  # Нахождение неполного частного
    return SUB_NN_N(x, MUL_NN_N(y, ch))  # Нахождение остатка


def LCM_NN_N(a, b):
    # Пекло Елизавета
    # Нахождения НОК двух натуральных
    # НОК = А*Б:НОД
    nod = GCF_NN_N(a, b)
    multp = MUL_NN_N(a, b)
    nok = DIV_NN_N(multp, nod)
    return nok


def DIV_NN_Dk(N1, N2):
    # Гурьянов Савелий
    # Целочисленное деление натуральных чисел осуществляется при помощи функции MUL_Nk_N
    # Переменная k, ответственная за целую часть от деления, изначально равная 0, инкрементируется,
    # пока N1 больше произведения k на N2
    if COM_NN_D(N1, N2) != 1:
        k = 1
        while COM_NN_D(N1, MUL_Nk_N(k, N2.copy())) == 2:
            k += 1
        return k - 1
    else:
        return DIV_NN_Dk(N2, N1)

    
def NZER_N_B(x):
    # Артамонов Артур, гр.0306
    # Проверка на 0. Если число = 0, то да, иначе нет
    if x[0] == 0:
        return True
    return False


def ADD_NN_N(mas1, mas2):
    # Семёнов Михаил
    # Сложение натуральных чисел
    plus1 = 0
    mas1 = mas1[::-1]
    mas2 = mas2[::-1]
    rez_com_nn_d = COM_NN_D(mas1, mas2)
    if rez_com_nn_d == 0 or rez_com_nn_d == 2:
        length = len(mas1)
        min_length = len(mas2)
        if rez_com_nn_d == 2:
            flag = 2
        else:
            flag = 0
    elif rez_com_nn_d == 1:
        length = len(mas2)
        min_length = len(mas1)
        flag = 1
    mas_rez = [0] * (length + 1)
    for j in range(min_length):
        mas_rez[j] = (int(mas1[j]) + int(mas2[j]) + plus1) % 10
        plus1 = (int(mas1[j]) + int(mas2[j]) + plus1) // 10
    if flag == 2:
        for i in range(length - min_length):
            mas_rez[j + i + 1] = (int(mas1[j + i + 1]) + plus1) % 10
            plus1 = (int(mas1[j + i + 1]) + plus1) // 10
    if flag == 1:
        for i in range(length - min_length):
            mas_rez[j + i + 1] = (int(mas2[j + i + 1]) + plus1) % 10
            plus1 = (int(mas2[j + i + 1]) + plus1) // 10
    if plus1 == 0:
        mas_rez = mas_rez[0:len(mas_rez) - 1]
    else:
        mas_rez[-1] = 1
    mas_rez = mas_rez[::-1]
    return mas_rez


def MUL_NN_N(nat1, nat2):
    # Аносов Павел
    # Умножение натуральных чисел
    nat2 = nat2[::-1]  # разворот списка
    sum = []
    if not NZER_N_B(nat1) and not NZER_N_B(nat2[::-1]):
        for i in range(len(nat2)):  # проход по цифрам второго числа
            if nat2[i] != 0:  # если не 0
                rez = MUL_ND_N(nat1, int(nat2[i]))  # умножаем число на цифру
                rez = rez + i * [0]  # прибавляем разряды
                if sum:  # если список не пустой
                    sum = ADD_NN_N(sum, rez)  # складываем два натуральных числа
                else:
                    sum = rez  # присваиваем списку значения списка rez
    else:
        sum = [0]
    return sum


def GCF_NN_N(list1, list2):
    # Дашкин Дамир
    # Нахождение НОД по алгоритму Евклида, используя остаток от деления одного числа на другое
    num1 = list1
    num2 = list2
    while not NZER_N_B(num1) and not NZER_N_B(num2):
        if COM_NN_D(num1, num2) == 2:
            num1 = MOD_NN_N(num1, num2)
        else:
            num2 = MOD_NN_N(num2, num1)
    if num1[0] == 0:
        k = num2
    else:
        k = num1
    return k

