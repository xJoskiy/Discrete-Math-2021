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

#Пекло Елизавета
#Умножение натурального целого на 10^k
#------------------------------------
def MUL_Nk_N(k, list0):
    list1 = [0]*k
    list0.extend(list1)
    return list0
#------------------------------------
