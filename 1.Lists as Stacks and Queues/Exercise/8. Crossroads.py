from collections import deque
green_light_duration = int(input())
free_window_duration = int(input())
data = input()
queue_of_cars = deque()
count = 0
crash = False

while not data == 'END':
    full_time = green_light_duration + free_window_duration
    if not data == 'green':
        car = data
        queue_of_cars.append(car)
    else:
        while queue_of_cars:
            c = queue_of_cars.popleft()
            count += 1
            full_time -= len(c)
            if full_time > free_window_duration:
                continue
            elif full_time < 0:
                print(f"""A crash happened!
{c} was hit at {c[full_time]}.""")
                crash = True
                break
            break
    if crash:
        break
    data = input()

if not crash:
    print(f"""Everyone is safe.
    {count} total cars passed the crossroads.""")