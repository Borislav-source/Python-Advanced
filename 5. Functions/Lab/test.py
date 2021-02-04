def permute(word, current_index=0):
    if current_index == len(word):
        print(''.join(word))
        return
    for i in range(current_index, len(word)):
        word[i], word[current_index] = word[current_index], word[i]
        permute(word, current_index+1)
        word[i], word[current_index] = word[current_index], word[i]


word_list = list(input())
permute(word_list)