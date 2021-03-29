import PySimpleGUI as sg


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
            window['out'].update(int(values['dig1']) + int(values['dig2']))
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
            window['out'].update(int(values['dig1']) - int(values['dig2']))
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
            window['out'].update(int(values['dig1']) * int(values['dig2']))
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
            window['out'].update(int(values['dig1']) / int(values['dig2']))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_nat_mod():
    layout = [
        [sg.Text('Enter two naturals')],
        [sg.Input(key='dig1')],
        [sg.Button('MOD', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('The remainder of the division of natural numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            pass
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
            pass
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
            pass
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
    if event == "Sub_Int":
        open_window_int_sub()
    if event == "Product_Int":
        open_window_int_prod()
    if event == "Quotient_Int":
        open_window_int_quot()
    if event == "Sum_Int":
        open_window_int_sum()


sg.theme('LightGray2')
menu = [['&Naturals', ['Sum_Nat', 'Sub_Nat', 'Product_Nat', 'Quotient_Nat', 'Mod_Nat', 'LCD_Nat', 'GCD_Nat']],
        ['&Integers', ['Module', 'Sum_Int', 'Sub_Int', 'Product_Int', 'Quotient_Int', 'Mod_Int', 'Exponentiation', 'Representation of a number in the form of a = p * q + r']],
        ['&Rationals', ['Сумма', 'Разность', 'Произведение', 'Частное', 'Сокращение дроби']],
        ['&Polynomials', ['Сумма', 'Разность', 'Произведение', 'Частное']],
        ['&Additional', ['Метод Ферма', 'Метод Эйлера', 'Примерные корни', 'Быстрое Возведение в степень', 'Преобразование дробь в непрерывную', 'Простые числа до N', 'Разложение числа на простые множители']]
        ]

layout = [
    [sg.Menu(menu)],
    [sg.Text('Something Will never Appear There Soon!')]
         ]


window = sg.Window('Коллоквиум ДМиТИ', layout, size=(510, 230), resizable=True)

while True:
    event, values = window.read()
    Operation_with_Naturals(event)
    Operation_with_Integers(event)
    if event == sg.WINDOW_CLOSED:
        break
