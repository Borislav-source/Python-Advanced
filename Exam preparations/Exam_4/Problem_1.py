from collections import deque
bombs_effects = list(map(int, input().split(', ')))
bombs_casing = list(map(int, input().split(', ')))
bombs_effects = deque(bombs_effects)
bombs_dict = {
    40: ['Datura Bombs', 0],
    60: ['Cherry Bombs', 0],
    120: ['Smoke Decoy Bombs', 0]
}
condition = False
while bombs_casing and bombs_effects:
    if bombs_effects:
        effect = bombs_effects.popleft()
    else:
        break
    if bombs_casing:
        casing = bombs_casing.pop()
    else:
        break
    bomb = effect + casing

    if bomb in bombs_dict:
        bombs_dict[bomb][1] += 1
    else:
        while bomb not in bombs_dict:
            casing -= 5
            bomb = casing + effect
            if bomb in bombs_dict:
                bombs_dict[bomb][1] += 1
    condition = []
    for k, v in bombs_dict.items():
        if v[1] >= 3:
            condition.append(True)
        else:
            condition.append(False)
    if condition and all(condition):
        print("Bene! You have successfully filled the bomb pouch!")
        break
if not all(condition):
    print("You don't have enough materials to fill the bomb pouch.")

if bombs_effects:
    print(f"Bomb Effects: {', '.join(list(map(str, bombs_effects)))}")
else:
    print(f"Bomb Effects: empty")
if bombs_casing:
    print(f"Bomb Casings: {', '.join(list(map(str, bombs_casing)))}")
else:
    print(f"Bomb Casings: empty")
for key, value in sorted(bombs_dict.items(), key=lambda x: x[1][0]):
    print(f"{value[0]}: {value[1]}")
