numbers = [1, 2, 3, 4]


def expressions(nums, current_sum=0, expression=''):
    if not nums:
        return [(expression, current_sum)]
    plus_result = expressions(nums[1:], current_sum+nums[0], f'{expression}+{nums[0]}')
    minus_result = expressions(nums[1:], current_sum-nums[0], f"{expression}-{nums[0]}")
    result = plus_result + minus_result
    return result


print(expressions(numbers))

