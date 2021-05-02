import natural as nat


def POZ_Z_D(mas):  # на вход функция получает целое число
    # Семёнов Михаил
    # Знак целого числа
    if mas[0] == '-':  # первый символ числа "-"
        return mas[0]
    elif mas[0] == 0:  # число равно нулю
        return 0
    else:
        return ''


def ABS_Z_N(celoe):
    # Семёнов Михаил
    # Модуль целого числа
    if POZ_Z_D(celoe) == '-':
        return celoe[1:]
    else:
        return celoe


def SUB_ZZ_Z(celoe1, celoe2):  # на вход функция получает 2 целых числа
    # Семёнов Михаил
    # Вычитание целых чисел
    poz1 = POZ_Z_D(celoe1)  # выясняем знак числа 1
   
    poz2 = POZ_Z_D(celoe2)  # выясняем знак числа 2
    celoe1 = celoe1[1:]
    celoe2 = celoe2[1:]
    if poz1 != poz2:  # числа разных знаков
        if poz1 == 1 and poz2 == 2:  # число 1 отрицательное
            
            celoe1_nat = ABS_Z_N(celoe1)  # модуль числа 1
            
            sum_res = nat.ADD_NN_N(celoe1_nat, celoe2)  # складываем модули чисел
            
            result = [1] + sum_res  # результат
        elif poz1 == 2 and poz2 == 1:  # число 1 положительное
            
            celoe2_nat = ABS_Z_N(celoe2)  # модуль числа 1
            
            sum_res = nat.ADD_NN_N(celoe1, celoe2_nat)  # складываем модули чисел
            
            result = [0] + sum_res  # результат
        elif poz1 == 0:  # число 1 равно "0"
            if poz2 == 2:  # число 2 положительное
                result = [1] + celoe2  # результат
            if poz2 == 1:  # число 2 положительное
                result = '-' + celoe2  # результат
            else:
                if poz2 == 1: # число 2 отрицательное
                    
                    celoe2_nat = ABS_Z_N(celoe2)  # находим модуль 2 числа

                    result =[0] + celoe2  # результат
                else : 
                    celoe2_nat = [0]
                    result =[0] + celoe2_nat  # результат
        else: # число 2 равно "0"
            if poz1 == 1:  # число 1 отрицательное
                
                celoe1_nat = ABS_Z_N(celoe1)  # находим модуль числа 1
                
                result = [1] + celoe1_nat  # результат
            else:
                result = [0] + celoe1  # результат
    else :
        if poz1 == 2:  # число 1 положительное
            
            sravnenie = nat.COM_NN_D(celoe1, celoe2)  # выясняем какое число больше
            
            if sravnenie == 2 or sravnenie == 0:
                
                result = [0] + nat.SUB_NN_N(celoe1,celoe2) # результат
                
            else:
                result = [1] + nat.SUB_NN_N(celoe2, celoe1)  # результат
        elif poz1 == 1:
            
            celoe1_nat = ABS_Z_N(celoe1)  # модуль числа 1
            
            celoe2_nat = ABS_Z_N(celoe2)  # модуль числа 2
            
            sravnenie = nat.COM_NN_D(celoe1_nat,celoe2_nat)  # сравниваем модули чисел
            
            if sravnenie == 1 or sravnenie == 0:
                 result = [0] + nat.SUB_NN_N(celoe2_nat, celoe1_nat)  # результат
            else:
                result = [1] + nat.SUB_NN_N(celoe1_nat, celoe2_nat)  # результат
        else:
            result = [0] + celoe1  # результат
    return result
  

def ADD_ZZ_Z(list1, list2):
    # Дашкин Дамир
    # Сложение целых чисел
    if POZ_Z_D(list1) == '' and POZ_Z_D(list2) == '':
        return nat.ADD_NN_N(list1, list2)
    elif POZ_Z_D(list1) == '-' and POZ_Z_D(list2) == '-':
        return ['-'] + nat.ADD_NN_N(ABS_Z_N(list1), ABS_Z_N(list2))
    elif nat.COM_NN_D(ABS_Z_N(list1), ABS_Z_N(list2)) == 2:
        return [POZ_Z_D(list1)] + nat.SUB_NN_N(ABS_Z_N(list1), ABS_Z_N(list2))
    else:
        return [POZ_Z_D(list2)] + nat.SUB_NN_N(ABS_Z_N(list2), ABS_Z_N(list1))


def MOD_ZZ_Z(num1, num2):
    # Дашкин Дамир
    # Остаток от деления целых чисел
    q = DIV_ZZ_Z(num1, num2)
    k = MUL_ZZ_Z(q, num2)
    return SUB_ZZ_Z(num1, k)


def MUL_ZM_Z(x):
    # Умножение целого на (-1)
    # Кривоконь Максим
    if POZ_Z_D(x) == '-':  # Если число отрицательное
        x = ABS_Z_N(x)   # то знак меняется
    else:
        x[0] = '-'   # Иначе число отрицательное
    return x


def MUL_ZZ_Z(list1, list2):
    # Умножение целых чисел
    # Кривоконь Максим
    if POZ_Z_D(list1) and POZ_Z_D(list2):
        if (POZ_Z_D(list1) == '' and POZ_Z_D(list2) == '') or (POZ_Z_D(list1) == '-' and POZ_Z_D(list2) == '-'):
            return nat.MUL_NN_N(ABS_Z_N(list1), ABS_Z_N(list1))
        else:
            return ['-'] + nat.MUL_NN_N(ABS_Z_N(list1), ABS_Z_N(list1))
    else:
        return 0


def DIV_ZZ_Z(celoe1, celoe2):
    # Савелий Гурьянов
    # Частное от деления целого на целое
    znak1 = POZ_Z_D(celoe1)  # знак числа 1
    znak2 = POZ_Z_D(celoe2)  # знак числа 2
    if znak1 != 0:  # делимое не 0
        celoe1_nat = ABS_Z_N(celoe1)  # натуральное число
        celoe2_nat = ABS_Z_N(celoe2)  # натуральное число
        result = nat.DIV_NN_N(celoe1_nat, celoe2_nat)  # частное от деления натуральных
        if znak1 != znak2:  # если знаки чисел разные
            result = [1] + result
        elif znak1 == 2:  # делимое больше нуля
            result = [0] + result
        else:
            result = [1] + result
    else:
        result = celoe1
    return result
