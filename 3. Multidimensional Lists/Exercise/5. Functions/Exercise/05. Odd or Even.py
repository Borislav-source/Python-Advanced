def odd_vs_even(operator, nums):
    return list(filter(mapper[operator], nums))


mapper = {
    'Even': lambda x: x % 2 == 0,
    'Odd': lambda x: x % 2 != 0
}
command = input()
numbers = list(map(int, input().split()))
print(sum(odd_vs_even(command, numbers)) * len(numbers))
