def create_fibonacci(count):
    fib_list = [0, 1]
    for num in range(2, count):
        next_num = fib_list[-2] + fib_list[-1]
        fib_list.append(next_num)
    return ' '.join(map(str, fib_list))


def locate_num(num, sequence):
    sequence = sequence.split()
    try:
        return f"The number - {num} is at index {tuple(sequence).index(num)}"
    except ValueError:
        return f"The number {num} is not in the sequence"
