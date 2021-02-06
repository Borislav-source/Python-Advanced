# def test(a, b, column):
#     result = a + b
#     column.append(result)
#     return a, b
#
#
# a = 1
# b = 2
# column = []
# test(a, b, column)
# print(column)

com = 'up'
s_row = 1
mapper = {
        'up': -1,
        'down': +1
    }
if com == 'up':
    choice = s_row + mapper[com]
print(choice)