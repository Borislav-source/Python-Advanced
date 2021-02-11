def list_manipulator(numbers, command, location, *args):
    numbers_to_input = []
    for n in args:
        numbers_to_input.append(n)
    if command == 'add':
        return add(numbers, location, numbers_to_input)
    else:
        return remove(numbers, location, numbers_to_input)


def add(numbers, location, numbers_to_input):
    if location == 'beginning':
        numbers = numbers_to_input + numbers

    elif location == 'end':
        numbers += numbers_to_input
    return numbers


def remove(numbers, location, numbers_to_input):
    if location == 'beginning':
        if numbers_to_input:
            index = numbers_to_input[0]
            numbers = numbers[index:]
        else:
            numbers = numbers[1:]
    elif location == 'end':
        if numbers_to_input:
            num = numbers_to_input[0]
            for i in range(int(num)):
                numbers.pop()
        else:
            numbers.pop()
    return numbers


# list_manipulator([1, 2, 3], 'add', 'beginning', 20, 30)
# list_manipulator([1, 2, 3], 'add', 'beginning')

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
