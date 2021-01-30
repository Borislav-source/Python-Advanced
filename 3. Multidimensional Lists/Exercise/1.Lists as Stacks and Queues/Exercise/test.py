# from collections import deque
# sentance = [1, 2, 3]
# a = deque(sentance)
# left = a.popleft()
# right = a.pop()
a = 1, 5, 8, 5, 6, 7
b = list(map(str, a))
print(*b)
print(type(a[0]))
print(type(b[0]))
