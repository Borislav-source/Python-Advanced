st = input()
s = []
for i in st:
    s.append(i)
result = ''
while s:
    result += s.pop()
print(result)