from natural import *

def POZ_Z_D(mas): # на вход функция получает целое число
    # Семёнов Михаил
    # Знак целого числа
    if mas[0] == '-': # первый символ числа "-"
        res = 1
    elif mas[0] == '0': # число равно нулю
        res=0
    else: # число положительное
        res = 2
    return res


def SUB_ZZ_Z(celoe1, celoe2): # на вход функция получает 2 целых числа
    # Семёнов Михаил
    # Вычитание целых чисел
    poz1 = POZ_Z_D(celoe1) # выясняем знак числа 1
   
    poz2 = POZ_Z_D(celoe2) # выясняем знак числа 2
    
    if poz1 != poz2 : # числа разных знаков
        if poz1 == 2 and poz2 == 1: # число 1 отрицательное
            
            celoe1_nat = ABS_Z_N(celoe1) # модуль числа 1
            
            sum_res = ADD_NN_N(celoe1_nat,celoe2) # складываем модули чисел
            
            result = '-' + sum_res # результат
        elif poz1 == 1 and poz2 == 2: # число 1 положительное
            
            celoe2_nat = ABS_Z_N(celoe2) # модуль числа 1
            
            sum_res = ADD_NN_N(celoe1,celoe2_nat) # складываем модули чисел
            
            result = sum_res # результат
        elif poz1 == 0: # число 1 равно "0"
            if poz2 == 1 # число 2 положительное
                result = '-' + celoe2 # результат
            else:
                if poz2 == 2: # число 2 отрицательное
                    
                    celoe2_nat = ABS_Z_N(celoe2) # находим модуль 2 числа
                    
                else : celoe_nat = '0'
                result = celoe2 # результат
        else: # число 2 равно "0"
            if poz1 == 2: # число 1 отрицательное
                
                celoe1_nat = ABS_Z_N(celoe1) # находим модуль числа 1
                
                result = '-' + celoe_nat # результат
            else:
                result = celoe # результат
    else :
        if poz1 == 1: # число 1 положительное
            
            sravnenie = COM_NN_D(celoe1,celoe2) # выясняем какое число больше
            
            if sravnenie ==  2 or sravnenie == 0:
                
                result = SUB_NN_N(celoe1,celoe2) # результат
                
            else:
                result = '-' + SUB_NN_N(celoe2,celoe1) # результат
        elif poz1 == 2:
            
            celoe1_nat = ABS_Z_N(celoe1) # модуль числа 1
            
            celoe2_nat = ABS_Z_N(celoe2) # модуль числа 2
            
            sravnenie = COM_NN_D(celoe1_nat,celoe2_nat) # сравниваем модули чисел
            
            if sravnenie ==  1 or sravnenie == 0:
                 result = SUB_NN_N(celoe2_nat,celoe1_nat) # результат
            else:
                result = '-' + SUB_NN_N(celoe1_nat,celoe2_nat) # результат
        else:
            result = '0' # результат
    return result
  

def ADD_ZZ_Z(b1, n1, list1, b2, n2, list2):
    #Дашкин Дамир
    #Сложение целых чисел
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
    if POZ_Z_D(num1) == 2 and POZ_Z_D(num2) == 2:
        res = ADD_NN_N(num1, num2)
    if POZ_Z_D(num1) == 1 and POZ_Z_D(num2) == 1:
        mod1 = ABS_Z_N(num1)
        mod2 = ABS_Z_N(num2)
        res = ADD_NN_N(mod1, mod2)
        res = MUL_ZM_Z(res)
    else:
        mod1 = ABS_Z_N(num1)
        mod2 = ABS_Z_N(num2)
        if COM_NN_D(mod1, mod2) == 2:
            if POZ_Z_D(num1) == 1:
                res = SUB_NN_N(mod1, mod2)
                res = MUL_ZM_Z(res)
            else:
                res = SUB_NN_N(mod1, mod2)
        if COM_NN_D(mod1, mod2) == 1:
            if POZ_Z_D(num2) == 1:
                res = SUB_NN_N(mod2, mod1)
                res = MUL_ZM_Z(res)
            else:
                res = SUB_NN_N(mod2, mod1)
        else:
            res = 0
    return res


def MOD_ZZ_Z(b1, n1, list1, b2, n2, list2):
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
    q = DIV_ZZ_Z(num1, num2)
    k = MUL_ZZ_Z(q, num2)
    res = SUB_ZZ_Z(num1, k)
    return res
