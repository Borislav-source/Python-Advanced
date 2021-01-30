def condition(word):
    if len(word) % 2 == 0:
        return word


def printing(my_list):
    for el in my_list:
        print(el)


result = [w for w in input().split() if condition(w)]
printing(result)
