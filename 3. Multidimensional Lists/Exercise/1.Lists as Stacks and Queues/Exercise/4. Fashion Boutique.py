from collections import deque
clothes = list(map(int, input().split()))
capacity = int(input())
current_amount = 0
next_cloth = 0
count = 0
while clothes:
    next_cloth = clothes.pop()
    if capacity >= current_amount + next_cloth:
        current_amount += next_cloth
        # capacity -= current_amount
    else:
        count += 1
        current_amount = next_cloth
print(count + 1)

