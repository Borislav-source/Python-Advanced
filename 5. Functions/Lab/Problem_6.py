def permutation(word, index=0):
    if index == len(word):
        print(''.join(word))
        return

    for el in range(index, len(word)):
        word[el], word[index] = word[index], word[el]
        permutation(word, index+1)
        word[el], word[index] = word[index], word[el]
    return


data = list(input())
permutation(data)