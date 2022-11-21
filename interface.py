from separation import parse, calculate
from output import view_result as view
from logger import log

def button_click():
    flag = input('Введите 0, чтобы продолжить, или любой другой символ, чтобы прервать работу программы... ')
    while flag == '0':
        separate_expression = parse()
        result = calculate(separate_expression)
        log(separate_expression, result)
        view(result)
        flag = input('Введите 0, чтобы продолжить, или любой другой символ, чтобы прервать работу программы... ')
    print('Программа завершена.')