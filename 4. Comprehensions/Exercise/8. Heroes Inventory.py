def printing_result(person):
    the_sum = [money for key, money in my_dict[person].items()]
    print(f'{person} -> Items: {len(my_dict[person])}, Cost: {sum(the_sum)}')


names = input().split(', ')
my_dict = {}
data = input()

while not data == 'End':
    name, item, cost = data.split('-')
    if name in names:
        if name not in my_dict:
            my_dict[name] = {}
        if item not in my_dict[name]:
            my_dict[name][item] = int(cost)
    data = input()

result = [printing_result(name) for name in names]


