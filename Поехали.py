import PySimpleGUI as sg
import natural as nat
import integer
import rational as rat
import polynome as pol


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
            res = ''.join(map(str, nat.ADD_NN_N(list(map(int, values['dig1'])), list(map(int, values['dig2'])))))
            window['out'].update(res)
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
            res = ''.join(map(str, nat.SUB_NN_N(list(map(int, values['dig1'])), list(map(int, values['dig2'])))))
            window['out'].update(res)
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
            res = ''.join(map(str, nat.MUL_NN_N(list(map(int, values['dig1'])), list(map(int, values['dig2'])))))
            window['out'].update(res)
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
            window['out'].update(nat.DIV_NN_N(list(map(int, values['dig1'])), list(map(int, values['dig2']))))
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
            window['out'].update(nat.MOD_NN_N(list(map(int, values['dig1'])), list(map(int, values['dig2']))))
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
    window = sg.Window('Greatest Common Divisor of natural numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(nat.GCF_NN_N(list(map(int, values['dig1'])), list(map(int, values['dig2']))))
        if event == sg.WINDOW_CLOSED:
            break

def open_window_nat_lcd():
    layout = [
        [sg.Text('Enter two naturals')],
        [sg.Input(key='dig1')],
        [sg.Button('LCD', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('Least Common Divisor of natural numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(nat.LCM_NN_N(list(map(int, values['dig1'])), list(map(int, values['dig2']))))
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
        x = []
        if values['dig1'][0] == '-':
            x = [1] + list(map(int, values['dig1'][1:]))
        else:
            x = [0] + list(map(int, values['dig1']))
        res = integer.ABS_Z_N(x)
        if res[0] == 2:
            rex = ['-'] + res[1:]
        else:
            res = res[1:]
        res = ''.join(map(str, res))

        if event == "start":
            window['out'].update(res)
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
        x = []
        y = []
        if values['dig1'][0] == '-':
            x = [1] + list(map(int, values['dig1'][1:]))
        else:
            x = [0] + list(map(int, values['dig1']))
        if values['dig2'][0] == '-':
            y = [1] + list(map(int, values['dig2'][1:]))
        else:
            y = [0] + list(map(int, values['dig2']))
        if event == "start":
            window['out'].update(integer.ADD_ZZ_Z(x, y))
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
        x = []
        y = []
        if values['dig1'][0] == '-':
            x = [1] + list(map(int, values['dig1'][1:]))
        else:
            x = [0] + list(map(int, values['dig1']))
        if values['dig2'][0] == '-':
            y = [1] + list(map(int, values['dig2'][1:]))
        else:
            y = [0] + list(map(int, values['dig2']))
        if event == "start":
            window['out'].update(integer.SUB_ZZ_Z(x, y))
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
        x = []
        y = []
        if values['dig1'][0] == '-':
            x = [1] + list(map(int, values['dig1'][1:]))
        else:
            x = [0] + list(map(int, values['dig1']))
        if values['dig2'][0] == '-':
            y = [1] + list(map(int, values['dig2'][1:]))
        else:
            y = [0] + list(map(int, values['dig2']))
        if event == "start":
            window['out'].update(x, y)
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
        x = []
        y = []
        if values['dig1'][0] == '-':
            x = [1] + list(map(int, values['dig1'][1:]))
        else:
            x = [0] + list(map(int, values['dig1']))
        if values['dig2'][0] == '-':
            y = [1] + list(map(int, values['dig2'][1:]))
        else:
            y = [0] + list(map(int, values['dig2']))
        if event == "start":
            window['out'].update(integer.MOD_ZZ_Z(x, y))
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
        x = []
        y = []
        if values['dig1'][0] == '-':
            x = [1] + list(map(int, values['dig1'][1:]))
        else:
            x = [0] + list(map(int, values['dig1']))
        if values['dig2'][0] == '-':
            y = [1] + list(map(int, values['dig2'][1:]))
        else:
            y = [0] + list(map(int, values['dig2']))
        if event == "start":
            window['out'].update(integer.DIV_ZZ_Z(x, y))
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
        x = []
        y = []
        i = 0
        while values['dig1'] != "\\":
            x.append(values['dig1'][i])
            i = 0
        y.append(list(map(int, values['dig1'][i + 1:])))
        if event == "start":
            window['out'].update()
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
            window['out'].update(int(values['dig1']) + int(values['dig2']))
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
            window['out'].update(int(values['dig1']) + int(values['dig2']))
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
            window['out'].update(int(values['dig1']) + int(values['dig2']))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_rat_red():
    layout = [
        [sg.Text('Enter two rationals')],
        [sg.Input(key='dig1')],
        [sg.Button('', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The fraction reduction of rational numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(int(values['dig1']) + int(values['dig2']))
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
            window['out'].update(int(values['dig1']) + int(values['dig2']))
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
    if event == "LCD_Nat":
        open_window_nat_lcd()
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


menu = [['&Naturals', ['Sum_Nat', 'Sub_Nat', 'Product_Nat', 'Quotient_Nat', 'Mod_Nat', 'LCD_Nat', 'GCD_Nat']],
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

