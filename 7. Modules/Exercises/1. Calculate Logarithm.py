import math


def log_calculator(num, fund):
    if fund == 'natural':
        return math.log(num)
    else:
        return math.log(num, int(fund))


number = int(input())
data = input()
print(f'{log_calculator(number, data):.2f}')


