n = int(input())
all_signs = []
current = ''
for _ in range(n):
    current += f' {input()}'
all_signs = current.split()
unique_signs = set(all_signs)

for sign in unique_signs:
    print(sign)
