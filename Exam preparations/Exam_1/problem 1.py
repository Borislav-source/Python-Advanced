from collections import deque

males = list(filter(lambda x: x != 0, list(map(int, input().split()))))
females = deque(filter(lambda x: x != 0, list(map(int, input().split()))))

matches = 0

while males and females:
    male = males.pop()
    if male % 25 == 0:
        males.pop()
        male = males.pop()
    female = females.popleft()
    if female % 25 == 0:
        females.popleft()
        female = females.popleft()

    if male == female:
        matches += 1
        continue
    male -= 2
    males.append(male)

print(f'Matches: {matches}')
if not males:
    print(f'Males left: none')
else:
    print(f'Males left: {", ".join(reversed(list(map(str, males))))}')

if not females:
    print(f'Females left: none')
else:
    print(f'Females left: {", ".join(reversed(list(map(str, females))))}')
