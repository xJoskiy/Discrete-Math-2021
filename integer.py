import natural as nat


def POZ_Z_D(mas):  # на вход функция получает целое число
    # Семёнов Михаил
    # Знак целого числа
    if mas[0] == '-':  # первый символ числа "-"
        return '-'
    elif nat.NZER_N_B(mas):
        return 0
    else:
        return '+'


def ABS_Z_N(x):
    # Семёнов Михаил
    # Модуль целого числа
    if POZ_Z_D(x) == '-':
        return x[1:]
    else:
        return x


def SUB_ZZ_Z(list1, list2):
    # Семёнов Михаил
    # Вычитание целых чисел
    if POZ_Z_D(list2) == '-':
        list2 = ABS_Z_N(list2)
    elif list2 != [0]:
        list2 = ['-'] + list2
    return ADD_ZZ_Z(list1, list2)
  

def ADD_ZZ_Z(list1, list2):
    # Дашкин Дамир
    # Сложение целых чисел
    if POZ_Z_D(list1) == '+' and POZ_Z_D(list2) == '+':
        return nat.ADD_NN_N(list1, list2)
    elif POZ_Z_D(list1) == '-' and POZ_Z_D(list2) == '-':
        return ['-'] + nat.ADD_NN_N(ABS_Z_N(list1), ABS_Z_N(list2))
    elif nat.COM_NN_D(ABS_Z_N(list1), ABS_Z_N(list2)) == 2:
        if POZ_Z_D(list1) == '-':
            return ['-'] + nat.SUB_NN_N(ABS_Z_N(list1), ABS_Z_N(list2))
        else:
            return nat.SUB_NN_N(ABS_Z_N(list1), ABS_Z_N(list2))
    elif nat.COM_NN_D(ABS_Z_N(list1), ABS_Z_N(list2)) == 1:
        if POZ_Z_D(list2) == '-':
            return ['-'] + nat.SUB_NN_N(ABS_Z_N(list2), ABS_Z_N(list1))
        else:
            return nat.SUB_NN_N(ABS_Z_N(list2), ABS_Z_N(list1))
    elif nat.COM_NN_D(ABS_Z_N(list1), ABS_Z_N(list2)) == 0:
        return [0]


def MOD_ZZ_Z(num1, num2):
    # Дашкин Дамир
    # Остаток от деления целых чисел
    q = DIV_ZZ_Z(num1, num2)  # Частное от деления
    k = MUL_ZZ_Z(q, num2)     # Произведения частного на число этого частного
    return SUB_ZZ_Z(num1, k)


def MUL_ZM_Z(x):
    # Умножение целого на (-1)
    # Кривоконь Максим
    if POZ_Z_D(x) == '-':  # Если число отрицательное
        x = ABS_Z_N(x)   # то знак меняется
    elif not nat.NZER_N_B(x):
        x = ['-'] + x  # Иначе число отрицательное
    return x


def MUL_ZZ_Z(list1, list2):
    # Умножение целых чисел
    # Кривоконь Максим
    if not nat.NZER_N_B(list1) and not nat.NZER_N_B(list2):
        if (POZ_Z_D(list1) == '+' and POZ_Z_D(list2) == '+') or (POZ_Z_D(list1) == '-' and POZ_Z_D(list2) == '-'):
            return nat.MUL_NN_N(ABS_Z_N(list1), ABS_Z_N(list2))
        else:
            return ['-'] + nat.MUL_NN_N(ABS_Z_N(list1), ABS_Z_N(list2))
    else:
        return [0]


def DIV_ZZ_Z(x, y):
    # Савелий Гурьянов
    # Частное от деления целого на целое
    if POZ_Z_D(x) == POZ_Z_D(y):
        return nat.DIV_NN_N(ABS_Z_N(x), ABS_Z_N(y))
    elif nat.NZER_N_B(x) or nat.NZER_N_B(x):
        return ["Unable to calculate"]
    else:
        return ['-'] + nat.DIV_NN_N(ABS_Z_N(x), ABS_Z_N(y))
