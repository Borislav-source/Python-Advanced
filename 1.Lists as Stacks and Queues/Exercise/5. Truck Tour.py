from collections import deque
pumps = int(input())
stack = []
for _ in range(pumps):
    liters, kilometers = map(int, input().split())
    result = liters - kilometers
    stack.append(result)
my_copy = deque(stack)
while True:
    condition = False
    current_liters = 0
    for i in range(len(my_copy)):
        current_liters += my_copy[i]
        if current_liters >= 0:
            continue
        else:
            condition = True
            break
    if condition:
        a = my_copy.popleft()
        my_copy.append(a)
    else:
        index = my_copy.popleft()
        break

for k in range(len(stack)):
    if stack[k] == index:
        print(k)
        break
