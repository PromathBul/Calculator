from input import get_expression

def parse ():
    expression = get_expression()
    result = []
    number = ''
    # expression = expression.split()
    for symbol in expression:
        if symbol.isdigit():
            number += symbol
        else:
            result.append(float(number))
            number = ''
            result.append(symbol)
    else:
        if number:
            result.append(float(number))
    return result

def calculate(lst):
    result = 0.0
    while '/' in lst:
        index = lst.index('/')
        result = lst[index - 1] / lst[index + 1]
        lst = lst[:index -1] + [result] + lst[index + 2:]
    while '*' in lst:
        index = lst.index('*')
        result = lst[index - 1] * lst[index + 1]
        lst = lst[:index -1] + [result] + lst[index + 2:]
    while '+' in lst:
        index = lst.index('+')
        result = lst[index - 1] + lst[index + 1]
        lst = lst[:index -1] + [result] + lst[index + 2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index - 1] - lst[index + 1]
        lst = lst[:index -1] + [result] + lst[index + 2:]
    return result