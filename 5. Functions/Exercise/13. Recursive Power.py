def recursive_power(value, n, result=1):
    if n == 0:
        return result
    result *= value
    return recursive_power(value, n - 1, result)


print(recursive_power(2, 10))