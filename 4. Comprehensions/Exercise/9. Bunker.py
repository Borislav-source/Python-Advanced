items_categories = input().split(', ')
relations = int(input())
my_dict = {}
the_sum_of_quantity = 0
the_sum_of_quality = 0
for _ in range(relations):
    data = input()
    category, item, rest = data.split(' - ')
    quantity, quality = rest.split(';')
    if category not in my_dict:
        my_dict[category] = []
    my_dict[category].append(item)
    the_sum_of_quantity += int(quantity.split(':')[1])
    the_sum_of_quality += float(quality.split(':')[1])


print(f'''Count of items: {the_sum_of_quantity}
Average quality: {the_sum_of_quality / len(my_dict):.2f}''')
[print(f'{cat} -> {", ".join(my_dict[cat])}') for cat in items_categories]
