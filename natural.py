def COM_NN_D(x, y):
    if len(x) > len(y):
        return 1
    elif len(x) < len(y):
        return -1
    else:
        for i, k in zip(x, y):
            if i > k:
                return 1
            elif i < k:
                return -1
    return 0
    
def DIV_NN_Dk(N1, N2):
    if COM_NN_D(N1, N2) == 2:
        k = 1
        while N1 > MUL_Nk_N(N2, k):
            k += 1
        return k - 1
    else:
        return DIV_NN_Dk(N2, N1)


def DIV_NN_Dk(N1, N2):
    if COM_NN_D(N1, N2) == 2:
        k = 1
        while N1 > MUL_Nk_N(N2, k):
            k += 1
        return k - 1
    else:
        return DIV_NN_Dk(N2, N1)
# Гурьянов Савелий
# Целочисленное деление натуральных чисел осуществляется при помощи функции MUL_Nk_N
# Переменная k, ответственная за целую часть от деления, изначально равная 0, инкрементируется,
# пока N1 больше произведения k на N2


