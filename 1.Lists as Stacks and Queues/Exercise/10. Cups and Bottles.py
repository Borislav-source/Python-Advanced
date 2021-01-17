from collections import deque
cups = deque(map(int, input().split()))
bottles_of_water = list(map(int, input().split()))
wasted_water = 0
filled = True
bottles_count = 0
while cups and bottles_of_water:
    if filled:
        current_cup = cups.popleft()
    bottle = bottles_of_water.pop()
    water = bottle - current_cup
    if water >= 0:
        wasted_water += bottle - current_cup
        filled = True
        continue
    filled = False
    current_cup -= bottle
if bottles_of_water:
    print(f"Bottles: {' '.join(list(map(str, bottles_of_water)))}")
else:
    print(f"Cups: {' '.join(list(map(str, cups)))}")


print(f"Wasted litters of water: {wasted_water}")
