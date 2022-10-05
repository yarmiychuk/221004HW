# Задайте последовательность цифр.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Решать через множества и еще каким-нибудь способом кроме множества
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

from random import randint

def createSubsequence():
    result = ''
    for i in range(10):
        result += str(randint(0, 9))
    return result

def getNonRecurring(line):
    list = []
    for item in line:
        if line.count(item) == 1:
            list.append(int(item))
    return list

subsequence = createSubsequence()
print(f'Неповторяющиеся элементы в последовательности цифр {subsequence}: {getNonRecurring(subsequence)}')