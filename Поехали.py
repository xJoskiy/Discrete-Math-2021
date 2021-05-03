import PySimpleGUI as sg
import natural as nat
import integer
import rational as rat
import polynome as pol


def StrToRat(seq):
    seq = StrToList(seq)
    Rat = [seq[:seq.index('/')], seq[seq.index('/') + 1:]]
    return Rat


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
            window['out'].update(ListToStr(rat.ADD_QQ_Q(StrToRat(values['dig1']), StrToRat(values['dig2']))))
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
            window['out'].update(ListToStr(rat.SUB_QQ_Q(StrToRat(values['dig1']), StrToRat(values['dig2']))))
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
            window['out'].update(ListToStr(rat.MUL_QQ_Q(StrToRat(values['dig1']), StrToRat(values['dig2']))))
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
            window['out'].update(ListToStr(rat.DIV_QQ_Q(StrToRat(values['dig1']), StrToRat(values['dig2']))))
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
            window['out'].update(ListToStr(rat.RED_Q_Q(StrToRat(values['dig1']))))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_pol_sum():
    layout = [
        [sg.Text('Enter coefficients of two polynomials')],
        [sg.Input(key='dig1')],
        [sg.Button('+', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The sum of polynomials', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update()
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
            window['out'].update(int(values['dig1']) + int(values['dig2']))
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
            window['out'].update(int(values['dig1']) + int(values['dig2']))
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


menu = [['&Naturals', ['Sum_Nat', 'Sub_Nat', 'Product_Nat', 'Quotient_Nat', 'Mod_Nat', 'LCM_Nat', 'GCD_Nat']],
        ['&Integers', ['Module', 'Sum_Int', 'Sub_Int', 'Product_Int', 'Quotient_Int', 'Mod_Int']],
        ['&Rationals', ['Sum_Rat', 'Sub_Rat', 'Product_Rat', 'Quotient_Rat', 'Fraction reduction']],
        ['&Polynomials', ['Sum_Pol', 'Sub_Pol', 'Product_Pol', 'Quotient_Pol']]
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

