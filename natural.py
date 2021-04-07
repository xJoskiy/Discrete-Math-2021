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


def MUL_Nk_N(k, list0):
    # Пекло Елизавета
    #Умножение натурального целого на 10^k
    list1 = [0]*k
    list0.extend(list1)
    return list0


def LCM_NN_N(a,b):
    # Пекло Елизавета
    #Нахождения НОК двух натуральных
    # НОК = А*Б:НОД
    nod = GCF_NN_N(a,b)
    multp = MUL_NN_N(a,b)
    nok = DIV_NN_N(multp,nod)
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

