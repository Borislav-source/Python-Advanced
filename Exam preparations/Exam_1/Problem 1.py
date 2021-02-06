from collections import deque
males = list(map(int, input().split()))
females = list(map(int, input().split()))

for m in range(len(list(map(str, males)))):
    if int(males[m]) <= 0:
        males[m] = None
    elif int(males[m]) % 25 == 0:
        males[m] = None
        if not m == 0:
            males[m-1] = None
males = [i for i in males if i is not None]

for f in range(len(list(map(str, females)))):
    if int(females[f]) <= 0:
        females[f] = None
    elif int(females[f]) % 25 == 0:
        females[f] = None
        if not f + 1 == len(females):
            females[f+1] = 0
females = [i for i in females if i is not None]
females = deque(females)

matches = 0

while len(males) > 0 and 0 < len(females):

    woman = females.popleft()

    man = males.pop()
    if man % 25 == 0:
        while man % 25 == 0:
            if males:
                males.pop()
                if males:
                    man = males.pop()
                else:
                    man = None
                    break
            else:
                man = None
                break
    if man == None:
        break
    if woman == man:
        matches += 1
    else:
        man -= 2
        if man > 0:
            males.append(man)

print(f'Matches: {matches}')
if males:
    print(f'Males left: {", ".join(list(map(str, reversed(males))))}')
else:
    print('Males left: none')
if females:
    print(f'Females left: {", ".join(list(map(str, females)))}')
else:
    print('Females left: none')
