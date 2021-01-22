Countries = input().split(', ')
Cities = input().split(', ')
result = {Countries[x]: Cities[x] for x in range(len(Countries))}
for key, item in result.items():
    print(f'{key} -> {item}')
