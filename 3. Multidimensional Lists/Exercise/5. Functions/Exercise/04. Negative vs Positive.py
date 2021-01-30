from functools import reduce


def negative_nums(nums):
    return list(filter(lambda x: x < 0, nums))


def positive_nums(nums):
    return list(filter(lambda x: x > 0, nums))


numbers = list(map(int, input().split()))
negative = sum(negative_nums(numbers))
positive = sum(positive_nums(numbers))
print(negative)
print(positive)

if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
