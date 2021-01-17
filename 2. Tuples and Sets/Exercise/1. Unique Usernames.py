n = int(input())
line = []
for _ in range(n):
    line.append(input())

unique = set(line)
for user in unique:
    print(user)