categories = {category: [] for category in input().split(', ')}
relations = int(input())
the_sum_of_quantity = 0
the_sum_of_quality = 0

for _ in range(relations):
    category, item, rest = input().split(' - ')
    quantity, quality = rest.split(';')
    categories[category].append(item)
    the_sum_of_quantity += int(quantity.split(':')[1])
    the_sum_of_quality += int(quality.split(':')[1])


print(f'''Count of items: {the_sum_of_quantity}
Average quality: {the_sum_of_quality / len(categories):.2f}''')
[print(f'{cat} -> {", ".join(item)}') for cat, item in categories.items()]
