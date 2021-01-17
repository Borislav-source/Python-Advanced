text = tuple(input())
counted = []
for ch in sorted(text):
    if not ch in counted:
        print(f'{ch}: {text.count(ch)} time/s')
        counted.append(ch)