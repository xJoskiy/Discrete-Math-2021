from natural import POZ_Z_D, ABS_Z_N, COM_NN_D, ADD_NN_N, SUB_NN_N, MUL_ZM_Z
def ADD_ZZ_Z(b1,n1,list1,b2,n2,list2):
    #Дашкин Дамир
    #Сложение целых чисел
    str1 = ""
    str2 = ""
    for i in range(len(list1)):
        str1 = str1 + str(list1[i])
    for j in range(len(list2)):
        str2 = str2 + str(list2[j])
    if b1==1:
        str1= "-" + str1
    num1=int(str1)
    if b2==1:
        str2="-" + str2
    num2=int(str2)
    if POZ_Z_D(num1)==2 and POZ_Z_D(num2)==2:
        res=ADD_NN_N(num1,num2)
    if POZ_Z_D(num1)==1 and POZ_Z_D(num2)==1:
        mod1=ABS_Z_N(num1)
        mod2=ABS_Z_N(num2)
        res=ADD_NN_N(mod1,mod2)
        res=MUL_ZM_Z(res)
    else:
        mod1=ABS_Z_N(num1)
        mod2=ABS_Z_N(num2)
        if COM_NN_D(mod1,mod2)==2:
            if POZ_Z_D(num1)==1:
                res=SUB_NN_N(mod1,mod2)
                res=MUL_ZM_Z(res)
            else:
                res=SUB_NN_N(mod1,mod2)
        if COM_NN_D(mod1,mod2)==1:
            if POZ_Z_D(num2) == 1:
                res = SUB_NN_N(mod2, mod1)
                res = MUL_ZM_Z(res)
            else:
                res = SUB_NN_N(mod2, mod1)
        else:
            res=0
    return res
def MOD_ZZ_Z(b1,n1,list1,b2,n2,list2):
    #Дашкин Дамир
    #Остаток от деления целых чисел
    str1 = ""
    str2 = ""
    for i in range(len(list1)):
        str1 = str1 + str(list1[i])
    for j in range(len(list2)):
        str2 = str2 + str(list2[j])
    if b1 == 1:
        str1 = "-" + str1
    num1 = int(str1)
    if b2 == 1:
        str2 = "-" + str2
    num2 = int(str2)
    q=DIV_ZZ_Z(num1,num2)
    k=MUL_ZZ_Z(q,num2)
    res=SUB_ZZ_Z(num1,k)
    return res