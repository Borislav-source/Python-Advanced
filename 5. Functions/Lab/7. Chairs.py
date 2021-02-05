def test(the_test=True):
    if not the_test:
        return input().split(', ')
    else:
        return ["Peter", "George", "Amy"]


def combinations(names, chairs, current=[]):
    if len(current) == chairs:
        print(', '.join(current))
        return
    for name in range(len(names)):
        current.append(names[name])
        combinations(names[name+1:], chairs, current)
        current.pop()


people = test(the_test=False)
number = int(input())
combinations(people, number)


