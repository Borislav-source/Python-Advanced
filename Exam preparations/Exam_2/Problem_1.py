from collections import deque
jobs = list(map(int, input().split(', ')))
index = int(input())
jobs = deque(jobs)
cycles = 0
my_job = jobs[index]

while my_job in jobs:
    minimal = jobs[0]
    for n in jobs:
        if n < minimal:
            minimal = n

    for i in range(jobs.count(minimal)):
        cycles += minimal
        jobs.remove(minimal)

print(cycles)
