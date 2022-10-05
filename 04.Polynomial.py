# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# k - максимальная степень многочлена, следующая степень на 1 меньше и так до ноля.
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

from random import randint

path = 'polynomial.txt'

def getExpression(k):
    expression = ''
    degree = \
        ['\u2070', '\u00B9', '\u00B2', '\u00B3', '\u2074',
        '\u2075', '\u2076', '\u2077', '\u2078', '\u2079']
    for i in range(k, -1, -1):
        nextInt = randint(0, 100)
        if nextInt > 0:
            if i < k:
                expression += getSymbol()
            expression += str(nextInt)
            if i > 0:
                expression += "x"
            if i > 1:
                expression += degree[i]
            expression += ' '                
    expression += '= 0'
    return expression

def getSymbol():
    if randint(0, 1) == 0:
        return '- '
    return '+ '

k = randint(2, 9)
print(f'Заданная степень: {k}')
expression = getExpression(k)
print(f'Выражение {expression}')
with open(path, 'w') as f:
    f.write(expression)
print(f'Успешно записано в файл {path}')