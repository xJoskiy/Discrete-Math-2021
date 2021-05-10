import PySimpleGUI as sg
import natural as nat
import integer
import rational as rat
import polynome as pol


def PolToStr(list_result, list_stepen):
    seq = ''
    for i in range(len(list_result)):
        if list_result[i][0] == [0]:
            list_result.pop(i)
            list_stepen.pop(i)
    for i in range(len(list_result)):
        for j in range(len(list_result[i])):
            for k in range(len(list_result[i][j])):
                if list_result[i][j][k] != '-':
                    list_result[i][j][k] = chr(list_result[i][j][k] + 48)
                seq = seq + list_result[i][j][k]
            if not j:
                seq = seq + '/'
        seq = seq + 'x'
    i = 0
    while i < len(seq):
        if i < len(seq) - 2:
            if seq[i] == '/' and seq[i + 1] == '1' and seq[i + 2] == 'x':
                seq = seq[:i] + seq[i + 2:]
        if i < len(seq) - 1:
            if seq[i] == 'x' and 47 < ord(seq[i + 1]) < 58:
                seq = seq[:i + 1] + '+' + seq[i + 1:]
        i += 1
    i = tmp = 0
    flag = -1
    while i < len(seq):
        if seq[i] == 'x':
            flag += 1
        if flag == tmp and seq[i] == 'x':
            string = ''
            for t in range(len((list_stepen[tmp]))):
                list_stepen[tmp][t] = chr(list_stepen[tmp][t] + 48)
                string = string + list_stepen[tmp][t]
            if string != '1' and string != '0':
                seq = seq[:i + 1] + '^' + string + seq[i + 1:]
            elif string == '0':
                seq = seq[:len(seq) - 1]
            tmp += 1
        i += 1
    i = 0
    while i < len(seq) - 1:
        if seq[i] == '1':
            if i == 0 and seq[i + 1] == 'x':
                seq = seq[i + 1:]
            elif seq[i + 1] == 'x' and (seq[i - 1] == '-' or seq[i - 1] == '+') and i < len(seq) - 2:
                seq = seq[:i] + seq[i + 1:]
        i += 1
    return seq


def StrToPol(seq):
    i = tmp = 0
    while i < len(seq):
        if seq[i] == 'x':
            if i == len(seq) - 1:
                seq = seq + '^1'
            elif seq[i + 1] == '+' or seq[i + 1] == '-':
                seq = seq[:i + 1] + '^1' + seq[i + 1:]
            if i == 0:
                seq = '1' + seq
            elif seq[i - 1] == '+' or seq[i - 1] == '-':
                seq = seq[:i] + '1' + seq[i:]
        if 47 < ord(seq[len(seq) - 1]) < 58:
            t = len(seq) - 1
            while seq[t] != '^' and seq[t] != '-' and seq[t] != '+' and t != 0 and tmp == 0:
                t -= 1
            if seq[t] == '-' or seq[t] == '+' or t == 0:
                seq = seq + 'x^0'
                tmp = 1
        i += 1
    mas = list(seq)
    coefficient = []
    power = []
    for i in range(len(mas)):
        if mas[i] != '-' and mas[i] != '+' and mas[i] != '^' and mas[i] != 'x' and mas[i] != '/':
            mas[i] = ord(mas[i]) - 48
    i = t = p = k = flag = 0
    while i < len(mas):
        if mas[i] == '-':
            p = 1
        if mas[i] == '/':
            flag = 1
            k = i
        if mas[i] == 'x':
            j = t
            if flag == 0:
                if p == 1 and j != 0:
                    j = t - 1
                    p = 0
                coefficient.append([mas[j:i], [1]])
            else:
                if p == 1 and not j:
                    j = t - 1
                    p = 0
                coefficient.append([mas[j:k], mas[k + 1:i]])
                flag = 0
        if mas[i] == '^':
            t = i
            while (mas[t] != '-' and mas[t] != '+') and t != len(mas) - 1:
                t += 1
            if t != len(mas) - 1:
                power.append(mas[i + 1:t])
            else:
                power.append(mas[i + 1:])
            t = t + 1
            i = t - 2
        i += 1
    return coefficient, power


def StrToRat(seq):
    seq = StrToList(seq)
    Rat = [seq[:seq.index('/')], seq[seq.index('/') + 1:]]
    return Rat


def RatToStr(x):
    try:
        return ListToStr(x[0]) + '/' + ListToStr(x[1])
    except:
        return ListToStr(x)


def StrToList(seq):
    res = []
    for i in seq:
        if i.isdigit():
            res.append(int(i))
        else:
            res.append(i)
    return res


def ListToStr(seq):
    return ''.join(map(str, seq))


def open_window_nat_sum():
    layout = [
        [sg.Text('Enter two naturals')],
        [sg.Input(key='dig1')],
        [sg.Button('+', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The sum of natural numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(ListToStr(nat.ADD_NN_N(StrToList(values['dig1']), StrToList(values['dig2']))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_nat_sub():
    layout = [
        [sg.Text('Enter two naturals')],
        [sg.Input(key='dig1')],
        [sg.Button('-', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The subtraction of natural numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(ListToStr(nat.SUB_NN_N(StrToList(values['dig1']), StrToList(values['dig2']))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_nat_prod():
    layout = [
        [sg.Text('Enter two naturals')],
        [sg.Input(key='dig1')],
        [sg.Button('*', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The product of natural numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(ListToStr(nat.MUL_NN_N(StrToList(values['dig1']), StrToList(values['dig2']))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_nat_quot():
    layout = [
        [sg.Text('Enter two naturals')],
        [sg.Input(key='dig1')],
        [sg.Button('/', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The quotient of natural numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(ListToStr(nat.DIV_NN_N(StrToList(values['dig1']), StrToList(values['dig2']))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_nat_mod():
    layout = [
        [sg.Text('Enter two naturals')],
        [sg.Input(key='dig1')],
        [sg.Button('Mod', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The remainder of the division of natural numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(ListToStr(nat.MOD_NN_N(StrToList(values['dig1']), StrToList(values['dig2']))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_nat_gcd():
    layout = [
        [sg.Text('Enter two naturals')],
        [sg.Input(key='dig1')],
        [sg.Button('GCD', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('Greatest Common Denominator of natural numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(ListToStr(nat.GCF_NN_N(StrToList(values['dig1']), StrToList(values['dig2']))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_nat_lcm():
    layout = [
        [sg.Text('Enter two naturals')],
        [sg.Input(key='dig1')],
        [sg.Button('LCM', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('Least Common Multiple of natural numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(ListToStr(nat.LCM_NN_N(StrToList(values['dig1']), StrToList(values['dig2']))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_int_module():
    layout = [
        [sg.Text('Enter integer number')],
        [sg.Input(key='dig1')],
        [sg.Button('Module', key='start')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The module of integer number', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(ListToStr(integer.ABS_Z_N((StrToList(values['dig1'])))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_int_sum():
    layout = [
        [sg.Text('Enter two integers')],
        [sg.Input(key='dig1')],
        [sg.Button('+', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The sum of integer numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(ListToStr(integer.ADD_ZZ_Z(StrToList(values['dig1']), StrToList(values['dig2']))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_int_sub():
    layout = [
        [sg.Text('Enter two integers')],
        [sg.Input(key='dig1')],
        [sg.Button('-', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The subtraction of integer numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(ListToStr(integer.SUB_ZZ_Z(StrToList(values['dig1']), StrToList(values['dig2']))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_int_prod():
    layout = [
        [sg.Text('Enter two integers')],
        [sg.Input(key='dig1')],
        [sg.Button('*', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The product of integer numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(ListToStr(integer.MUL_ZZ_Z(StrToList(values['dig1']), StrToList(values['dig2']))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_int_mod():
    layout = [
        [sg.Text('Enter two integers')],
        [sg.Input(key='dig1')],
        [sg.Button('mod', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The mod of integer numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(ListToStr(integer.MOD_ZZ_Z(StrToList(values['dig1']), StrToList(values['dig2']))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_int_quot():
    layout = [
        [sg.Text('Enter two integers')],
        [sg.Input(key='dig1')],
        [sg.Button('/', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The quotient of integer numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(ListToStr(integer.DIV_ZZ_Z(StrToList(values['dig1']), StrToList(values['dig2']))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_rat_sum():
    layout = [
        [sg.Text('Enter two rationals')],
        [sg.Input(key='dig1')],
        [sg.Button('+', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The sum of rational numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(RatToStr(rat.TRANS_Q_Z(rat.ADD_QQ_Q(StrToRat(values['dig1']), StrToRat(values['dig2'])))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_rat_sub():
    layout = [
        [sg.Text('Enter two rationals')],
        [sg.Input(key='dig1')],
        [sg.Button('-', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The subtraction of rational numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(RatToStr(rat.TRANS_Q_Z(rat.SUB_QQ_Q(StrToRat(values['dig1']), StrToRat(values['dig2'])))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_rat_prod():
    layout = [
        [sg.Text('Enter two rationals')],
        [sg.Input(key='dig1')],
        [sg.Button('*', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The product of rational numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(RatToStr(rat.TRANS_Q_Z(rat.MUL_QQ_Q(StrToRat(values['dig1']), StrToRat(values['dig2'])))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_rat_quot():
    layout = [
        [sg.Text('Enter two rationals')],
        [sg.Input(key='dig1')],
        [sg.Button('/', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The quotient of rational numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(RatToStr(rat.TRANS_Q_Z(rat.DIV_QQ_Q(StrToRat(values['dig1']), StrToRat(values['dig2'])))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_rat_red():
    layout = [
        [sg.Text('Enter two rationals')],
        [sg.Input(key='dig1')],
        [sg.Button('', key='start')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The fraction reduction of rational numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(RatToStr(rat.TRANS_Q_Z(rat.RED_Q_Q(StrToRat(values['dig1'])))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_pol_sum():
    layout = [
        [sg.Text('Enter the polynomial')],
        [sg.Input(key='dig1')],
        [sg.Button('+', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The sum of polynomials', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            k1, p1 = StrToPol(values['dig1'])
            k2, p2 = StrToPol(values['dig2'])
            coefficient, power = pol.ADD_PP_P(k1, p1, k2, p2)
            window['out'].update(PolToStr(coefficient, power))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_pol_sub():
    layout = [
        [sg.Text('Enter coefficients of two polynomials')],
        [sg.Input(key='dig1')],
        [sg.Button('-', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The subtraction of polynomials', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(int(values['dig1']) + int(values['dig2']))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_pol_prod():
    layout = [
        [sg.Text('Enter coefficients of two polynomials')],
        [sg.Input(key='dig1')],
        [sg.Button('*', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The production of polynomials', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            k1, p1 = StrToPol(values['dig1'])
            k2, p2 = StrToPol(values['dig2'])
            coefficient, power = pol.MUL_PP_P(k1, p1, k2, p2)
            window['out'].update(PolToStr(coefficient, power))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_pol_quot():
    layout = [
        [sg.Text('Enter coefficients of two polynomials')],
        [sg.Input(key='dig1')],
        [sg.Button('/', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The quotient of polynomials', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            k1, p1 = StrToPol(values['dig1'])
            k2, p2 = StrToPol(values['dig2'])
            coefficient, power = pol.D(k1, p1, k2, p2)
            window['out'].update(PolToStr(coefficient, power))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_pol_derivative():
    layout = [
        [sg.Text('Enter coefficients of two polynomials')],
        [sg.Input(key='dig1')],
        [sg.Button('Differentiate', key='start')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('Derivative of polynomial', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            k1, p1 = StrToPol(values['dig1'])
            coefficient, power = pol.DER_P_P(k1, p1)
            window['out'].update(PolToStr(coefficient, power))
        if event == sg.WINDOW_CLOSED:
            break


def Operation_with_Naturals(event):
    if event == "Sum_Nat":
        open_window_nat_sum()
    if event == "Sub_Nat":
        open_window_nat_sub()
    if event == "Product_Nat":
        open_window_nat_prod()
    if event == "Quotient_Nat":
        open_window_nat_quot()
    if event == "Mod_Nat":
        open_window_nat_mod()
    if event == "LCM_Nat":
        open_window_nat_lcm()
    if event == "GCD_Nat":
        open_window_nat_gcd()


def Operation_with_Integers(event):
    if event == "Module":
        open_window_int_module()
    if event == "Sum_Int":
        open_window_int_sum()
    if event == "Mod_Int":
        open_window_int_mod()
    if event == "Sub_Int":
        open_window_int_sub()
    if event == "Product_Int":
        open_window_int_prod()
    if event == "Quotient_Int":
        open_window_int_quot()


def Operation_with_Rationals(event):
    if event == "Sum_Rat":
        open_window_rat_sum()
    if event == "Sub_Rat":
        open_window_rat_sub()
    if event == "Product_Rat":
        open_window_rat_prod()
    if event == "Quotient_Rat":
        open_window_rat_quot()
    if event == "Fraction reduction":
        open_window_rat_red()


def Operation_with_Polynomials(event):
    if event == "Sum_Pol":
        open_window_pol_sum()
    if event == "Sub_Pol":
        open_window_pol_sub()
    if event == "Product_Pol":
        open_window_pol_prod()
    if event == "Quotient_Pol":
        open_window_pol_quot()
    if event == "Derivative":
        open_window_pol_derivative()


menu = [['&Naturals', ['Sum_Nat', 'Sub_Nat', 'Product_Nat', 'Quotient_Nat', 'Mod_Nat', 'LCM_Nat', 'GCD_Nat']],
        ['&Integers', ['Module', 'Sum_Int', 'Sub_Int', 'Product_Int', 'Quotient_Int', 'Mod_Int']],
        ['&Rationals', ['Sum_Rat', 'Sub_Rat', 'Product_Rat', 'Quotient_Rat', 'Fraction reduction']],
        ['&Polynomials', ['Sum_Pol', 'Sub_Pol', 'Product_Pol', 'Quotient_Pol', 'Derivative']]
        ]
sg.theme('LightGray2')

layout = [
    [sg.Menu(menu)],
    [sg.Text('Something Will never Appear There Soon!')]
         ]


window = sg.Window('Коллоквиум ДМиТИ', layout, size=(510, 230), resizable=True)

while True:
    event, values = window.read()
    Operation_with_Naturals(event)
    Operation_with_Integers(event)
    Operation_with_Rationals(event)
    Operation_with_Polynomials(event)
    if event == sg.WINDOW_CLOSED:
        break

