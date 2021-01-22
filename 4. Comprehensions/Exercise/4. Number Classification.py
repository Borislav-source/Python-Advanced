my_list = list(map(int, input().split(', ')))
positive = [str(number) for number in my_list if number >= 0]
negative = [str(number) for number in my_list if number < 0]
even = [str(number) for number in my_list if number % 2 == 0]
odd = [str(number) for number in my_list if not number % 2 == 0]

print(f'''Positive: {', '.join(positive)}
Negative: {', '.join(negative)}
Even: {', '.join(even)}
Odd: {', '.join(odd)}
''')
