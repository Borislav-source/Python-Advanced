from fibonacci_sequence import *
data = input()

while not data == 'Stop':
    data = data.split()
    num = int(data.pop())
    command = data[0]
    if command == 'Create':
        sequence = create_fibonacci(num)
        print(sequence)
    else:
        print(locate_num(str(num), sequence))
    data = input()
    