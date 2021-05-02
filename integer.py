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


def ADD_ZZ_Z(list1, list2):
    # Семёнов Михаил
    # Вычитание целых чисел
    if POZ_Z_D(list1) == '+' and POZ_Z_D(list2) == '-':
        return ADD_NN_N(list1, ABS_Z_N(list2))
    elif POZ_Z_D(list1) == '-' and POZ_Z_D(list2) == '+':
        return ['-'] + ADD_NN_N(ABS_Z_N(list1), ABS_Z_N(list2))
    elif COM_NN_D(ABS_Z_N(list1), ABS_Z_N(list2)) == 2 :
        if list2 != [0]:
            return  SUB_NN_N(ABS_Z_N(list1), ABS_Z_N(list2))
        else :
            return list1
    elif POZ_Z_D(list1) == 0 :
        if POZ_Z_D(list2) == '-':
            return list2[1:]
        elif list2 == [0]:
            return list2
        else :
            return ['-'] + list2

    else:
        if POZ_Z_D(list1) == '+':
            return ['-'] + SUB_NN_N(ABS_Z_N(list2), ABS_Z_N(list1))
        else :
            return  SUB_NN_N(ABS_Z_N(list2), ABS_Z_N(list1))
  

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
