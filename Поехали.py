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
        [sg.Button('Mod', key='start')],
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
            window['out'].update()
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
            window['out'].update(int(values['dig1']) + int(values['dig2']))
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
            window['out'].update(int(values['dig1']) - int(values['dig2']))
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
            window['out'].update(int(values['dig1']) * int(values['dig2']))
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
    window = sg.Window('The quotient of natural numbers', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(int(values['dig1']) / int(values['dig2']))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_int_exp():
    layout = [
        [sg.Text('Enter number and power')],
        [sg.Input(key='dig1')],
        [sg.Button('Do it', key='start')],
        [sg.Input(key='dig2')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('Exponentiation of a number', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(int(values['dig1']) / int(values['dig2']))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_int_shortForm():
    layout = [
        [sg.Text('Enter number')],
        [sg.Input(key='dig1')],
        [sg.Button('^', key='start')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('Short form of a number', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(int(values['dig1']))
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
            window['out'].update(int(values['dig1']) + int(values['dig2']))
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


def open_window_add_fermat():
    layout = [
        [sg.Text('Enter number')],
        [sg.Input(key='dig1')],
        [sg.Button('Do it', key='start')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('Fermat`s method', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(int(values['dig1']))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_add_euler():
    layout = [
        [sg.Text('Enter number')],
        [sg.Input(key='dig1')],
        [sg.Button('Do it', key='start')],
        [sg.Text(size=(400, 10), key='out')]
    ]
    window = sg.Window('Euler`s method', layout, size=(460, 260), resizable=True)
    while True:
        event, values = window.read()
        if event == "start":
            window['out'].update(int(values['dig1']))
        if event == sg.WINDOW_CLOSED:
            break


def open_window_add_apprRoots():
    pass


def open_window_add_quickExp():
    pass


def open_window_add_contFract():
    pass


def open_window_add_primeNums():
    pass


def open_window_add_primeFactors():
    pass


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
    if event == "Exponentiation":
        open_window_int_exp()
    if event == "Representation of a number in the form of a = p * q + r":
        open_window_int_shortForm()


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


def Operation_with_Additional(event):
    if event == "Fermat`s method":
        open_window_add_fermat()
    if event == "Euler`s method":
        open_window_add_euler()
    if event == "Approximate roots":
        open_window_add_apprRoots()
    if event == "Quick exponentiation":
        open_window_add_quickExp()
    if event == "Convert a fraction to a continuous one":
        open_window_add_contFract()
    if event == "Prime numbers up to the N":
        open_window_add_primeNums()
    if event == "Decomposition of a number into prime factors":
        open_window_add_primeFactors()


menu = [['&Naturals', ['Sum_Nat', 'Sub_Nat', 'Product_Nat', 'Quotient_Nat', 'Mod_Nat', 'LCD_Nat', 'GCD_Nat']],
        ['&Integers', ['Module', 'Sum_Int', 'Sub_Int', 'Product_Int', 'Quotient_Int', 'Mod_Int', 'Exponentiation', 'Representation of a number in the form of a = p * q + r']],
        ['&Rationals', ['Sum_Rat', 'Sub_Rat', 'Product_Rat', 'Quotient_Rat', 'Fraction reduction']],
        ['&Polynomials', ['Sum_Pol', 'Sub_Pol', 'Product_Pol', 'Quotient_Pol']],
        ['&Additional', ['Fermat`s method', 'Euler`s method', 'Approximate roots', 'Quick exponentiation', 'Convert a fraction to a continuous one', 'Prime numbers up to the N', 'Decomposition of a number into prime factors']]
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
    Operation_with_Additional(event)
    if event == sg.WINDOW_CLOSED:
        break
