def max(numbers):
    if len(numbers) == 1:
        return numbers[0]

    x = numbers[-1]
    y = max(numbers[:-1])

    if x > y:
        return x
    else:
        return y


print(max([1, 6, 3, 4, 5]))