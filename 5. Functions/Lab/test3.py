def combinations(my_list, pair=[]):
    if not my_list:
        return
    pair.clear()
    pair.append(my_list[0])
    for indx in range(1, len(my_list)):
        pair.append(my_list[indx])
        print(pair)
        pair.pop()
    combinations(my_list[1:])

#
#
#
# combinations(['Peter', 'George', 'Amy'])


# def combinations(my_list, current_index=0, pair=[]):
#     if current_index == 2:
#         print(pair)
#         return
#
#     for name in range(len(my_list)):
#         pair.append(my_list[name])
#         combinations(my_list[name+1:], current_index+1)
#         pair.pop()



combinations(['Peter', 'George', 'Amy', 'Gabi'])

# def permutations(word, current_index=0):
#     if current_index == len(word)-1:
#         print(word)
#         return
#
#     for el in range(current_index, len(word)):
#         word[el], word[current_index] = word[current_index], word[el]
#         permutations(word, current_index+1)
#         word[el], word[current_index] = word[current_index], word[el]
#
#
#
#
# word = ['a', 'b', 'c']
# permutations(word)