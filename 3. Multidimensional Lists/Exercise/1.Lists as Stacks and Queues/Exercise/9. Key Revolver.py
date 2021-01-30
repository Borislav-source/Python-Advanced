from collections import deque
bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_value = int(input())
unlocked = True
bullets_count = 0
while bullets and locks:
    current_bullet = bullets.pop()
    intelligence_value -= bullet_price
    bullets_count += 1
    if unlocked:
        lock = locks.popleft()
    if current_bullet <= lock:
        print('Bang!')
        unlocked = True
    else:
        print('Ping!')
        unlocked = False
    if bullets:
        if bullets_count == gun_barrel_size:
            print('Reloading!')
            bullets_count = 0
if not unlocked:
    locks.append(lock)
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")
