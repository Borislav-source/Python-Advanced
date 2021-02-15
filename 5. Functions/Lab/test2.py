def permutation(word, current_index=0):
    if current_index == len(word):
        print(word)
        return

    for el in range(current_index, len(word)):
        word[el], word[current_index] = word[current_index], word[el]
        permutation(word, current_index+1)
        word[el], word[current_index] = word[current_index], word[el]


my_word = ['a', 'b', 'c', 'd']
permutation(my_word)
