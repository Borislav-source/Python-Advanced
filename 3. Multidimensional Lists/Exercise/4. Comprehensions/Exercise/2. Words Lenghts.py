def printing_result(word):
    return f'{word} -> {len(word)}'


result = [printing_result(w) for w in input().split(', ')]
print(', '.join(result))
