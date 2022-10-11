# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

from random import randint as r

degree = \
        ['\u2070', '\u00B9', '\u00B2', '\u00B3', '\u2074',
        '\u2075', '\u2076', '\u2077', '\u2078', '\u2079']
path = ['file1.txt', 'file2.txt']
pathResult = 'result.txt'

def createExpression(k):
    expression = ''
    for i in range(k, -1, -1):
        expression += getSegment(i, r(-100, 100), expression == '')
    return expression + '= 0'

def getSegment(i, num, isStart):
    segment = ''
    if num != 0:
        strNum = str(num)
        if not isStart:
            if num > 0:
                strNum = '+ ' + strNum
            else:
                strNum = strNum.replace('-', '- ')
        segment += strNum
        if i > 0:
            segment += "x"
        if i > 1:
            segment += degree[i]
        segment += ' '
    return segment

def listToDict(list):
    dict = {}
    for item in list:
        index = 0
        number = 0
        if len(item) > 2 and item[len(item) - 1] in degree:
            index = degree.index(item[len(item) - 1])
            number = int(item[:len(item) - 2])
        elif len(item) > 1 and item[len(item) - 1] == 'x':
            index = 1
            number = int(item[:len(item) - 1])
        else:
            number = int(item)
        dict[index] = number
    return dict

# Create
k = r(5, 9)
exp = [createExpression(k), createExpression(k)]
print(f'Сгенерированные выражения:\n{exp[0]}\n{exp[1]}')

# Write
for i in range(2):
    with open(path[i], 'w') as f:
        f.write(exp[i])
print(f'Успешно записаны в файлы {path[0]} и {path[1]}')

# Read
rExp = []
for i in range(2):
    with open(path[i]) as f:
        rExp.append(f.read())

# Convert
dict = []
for i in range(2):
    rExp[i] = rExp[i].replace(' = 0', '').replace('- ', '-').replace('+ ', '')
    dict.append(listToDict(rExp[i].split(' ')))

# Create result
expression = ''
for i in range(k, -1, -1):
    if dict[0].get(i) != None and dict[1].get(i) != None:
        number = dict[0].get(i) + dict[1].get(i)
    elif dict[0].get(i) == None:
        number = dict[1].get(i)
    else:
        number = dict[0].get(i)
    expression += getSegment(i, number, expression == '')
expression += '= 0' 

# Write result
print(f'Сумма многочленов:\n{expression}')
with open(pathResult, 'w') as f:
    f.write(expression)
print(f'Записана в файл {pathResult}')
