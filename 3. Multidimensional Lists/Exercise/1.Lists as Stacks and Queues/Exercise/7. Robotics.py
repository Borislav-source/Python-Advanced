from datetime import datetime, timedelta
from collections import deque
import timeit
robs = input().split(';')
robots = {}
queue = deque()
for r in range(len(robs)):
    robot, time = robs[r].split('-')
    robots[robot] = int(time)
    queue.append(robot)
occupied = {}
time = datetime.strptime(input(), '%H:%M:%S')
product = input()
shop = deque()
while not product == 'End':
    shop.append(product)
    product = input()
while len(shop) > 0:
    product = shop.popleft()
    condition = True
    for q in queue:
        time = time + timedelta(seconds=1)
        if q in occupied:
            if not time == occupied[q]:
                continue
            del occupied[q]
        available = time + timedelta(seconds=robots[q])
        occupied[q] = available
        print(f'{q} - {product} [{time.strftime("%H:%M:%S")}]')
        current_robot = queue.popleft()
        queue.append(current_robot)
        condition = False
        break
    if condition:
        shop.append(product)
