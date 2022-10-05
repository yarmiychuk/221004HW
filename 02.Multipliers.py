# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

from random import randint

def getMultipliers(number):
    multipliers = []
    nextMult = 2
    while number > 1:
        nextMult = getNextMultiplier(number, nextMult)
        multipliers.append(nextMult)
        number /= nextMult
    return multipliers

def getNextMultiplier(number, nextOne):
    while (number % nextOne != 0):
        nextOne += 1
    return nextOne

number = randint(10, 999)
print(f'Список простых множителей для числа {number}:')
print(getMultipliers(number))
