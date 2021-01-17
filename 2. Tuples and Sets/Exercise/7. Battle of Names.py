import math
n = int(input())
even = set()
odd = set()
for line in range(1, n + 1):
    the_sum = 0
    name = input()
    for ch in name:
        the_sum += (ord(ch) / line)
    if math.floor(the_sum) % 2 == 0:
        even.add(math.floor(the_sum))
    else:
        odd.add(math.floor(the_sum))
if sum(even) == sum(odd):
    print(', '.join(set(map(str, odd.union(even)))))
elif sum(even) > sum(odd):
    print(', '.join(set(map(str, odd.symmetric_difference(even)))))
else:
    print(', '.join(set(map(str, odd.difference(even)))))
