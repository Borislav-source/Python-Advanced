from collections import deque

males_seq = list(map(int, input().split()))
females_seq = deque(map(int, input().split()))

males_seq = list(filter(lambda x: x != 0, males_seq))
females_seq = deque(filter(lambda x: x != 0, females_seq))


female = None
male = None
matches = 0

while females_seq:

    if female is None:
        if females_seq:
            female = females_seq.popleft()
        else:
            break
    if female % 25 == 0:
        females_seq.popleft()
        female = None
        continue
    if male is None:
        if males_seq:
            male = males_seq.pop()
        else:
            females_seq.insert(0, female)
            break
    if male % 25 == 0:
        males_seq.pop()
        male = None
        continue

    if not female == male:
        male -= 2
        if male > 0:
            males_seq.append(male)
    else:
        matches += 1
    male = None
    female = None



result = f'Matches: {matches}\n'

result += f'Males left: {", ".join(list(map(str, (reversed(males_seq)))))}\n' if males_seq else 'Males left: none\n'
result += f'Females left: {", ".join(list(map(str, (females_seq))))}' if females_seq else 'Females left: none'

print(result)