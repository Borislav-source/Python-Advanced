def even_odd(*args):
    command = args[-1]
    return list(filter(mapper[command], args[:-1]))


mapper = {
    'even': lambda x: x % 2 == 0,
    'odd': lambda x: x % 2 != 0
}

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
