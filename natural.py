def COM_NN_D(x, y):
    # Аносов Павел
    # Сравнение двух чисел
    if len(x) > len(y):
        return 2
    elif len(x) < len(y):
        return 1
    else:
        for i, k in zip(x, y):
            if i > k:
                return 2
            elif i < k:
                return 1
    return 0


def DIV_NN_N(x, y):
    # Аносов Павел
    # Частное от деления большего натурального числа на меньшее или равное натуральное с остатком (делитель отличен от нуля)
    count = 0
    while COM_NN_D(x, y):
        x = SUB_NN_N(x, y)
        count += 1
    return count


def MUL_Nk_N(k, list0):
    # Пекло Елизавета
    # Умножение натурального целого на 10^k
    list1 = [0] * k
    list0.extend(list1)
    return list0


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
    if COM_NN_D(N1, N2) == 2:
        k = 1
        while N1 > MUL_Nk_N(N2, k):
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


def MOD_NN_N(x, y):
    # Артамонов Артур, гр.0306
    # Остаток от деления большего натурального числа на меньшее или равное натуральное с остатком(делитель отличен от нуля)

    ch = DIV_NN_N(x, y)  # Нахождение неполного частного
    mod = SUB_NDN_N(x, ch, y)  # Нахождение остатка. Пример: 53 mod 3 = 2. Тогда ch = 53/3 = 17. mod = 53 - 17 * 3 = 2
    return mod


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
            mas_rez[j + i + 1] = (int(mas1[j + i + 1])+plus1) % 10
            plus1 = (int(mas1[j + i + 1])+plus1) // 10
    if flag == 1:
        for i in range(length - min_length):
            mas_rez[j+i+1] = (int(mas2[j + i + 1]) + plus1) % 10
            plus1 = (int(mas2[j+i+1]) + plus1) // 10
    if plus1 == 0:
        mas_rez = mas_rez[0:len(mas_rez) - 1]
    else:
        mas_rez[-1] = 1
    mas_rez = mas_rez[::-1]
    return "".join(map(str, mas_rez))


def GCF_NN_N(n1, list1, n2, list2):
    # Дашкин Дамир
    # Нахождение НОД по алгоритму Евклида, используя остаток от деления одного числа на другое
    str1 = "" 
    str2 = ""
    for i in range(len(list1)):
        str1 = str1 + str(list1[i])
    for j in range(len(list2)):
        str2 = str2 + str(list2[j])
    num1, num2 = int(str1), int(str2)
    while NZER_N_B(num1) == "Нет" and NZER_N_B(num2) == "Нет":
        if COM_NN_D(num1, num2) == 2:
            num2 = MOD_NN_N(num2, num1)
        else:
            num1 = MOD_NN_N(num1, num2)
    return num1 + num2
