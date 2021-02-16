def expressions(sequence, current_sum=0, expression=''):
    if not sequence:
        return [(expression, current_sum)]

    plus_result = expressions(sequence[1:], current_sum+sequence[0], f"{expression}+{sequence[0]}")
    minus_result = expressions(sequence[1:], current_sum-sequence[0], f"{expression}-{sequence[0]}")
    result = plus_result + minus_result
    return result


[print(f'{exp[0]}={exp[1]}') for exp in expressions(list(map(int, input().split(', '))))]