from collections import deque
food_quantity = int(input())
my_list = list(input().split())
my_copy = map(int, my_list)
top = max(my_copy)
sequence = deque(my_list)
condition = False

for ordr in range(len(sequence)):
    order = int(sequence.popleft())
    if food_quantity - order >= 0:
        food_quantity -= order
    else:
        condition = True
        break
print(top)
if condition:
    if len(sequence) >= 1:
        print(f"Orders left: {str(order)}, {', '.join(sequence)}")
    else:
        print(f"Orders left: {str(order)}")
else:
    print('Orders complete')