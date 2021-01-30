sequence = input()
stack = []
condition = True
mirrors = {'{': '}', '[': ']', '(': ')'}

for i in sequence:
    if i in '{[(':
        stack.append(i)
    else:
        if len(stack) == 0:
            condition = False
            break
        current = stack.pop()
        if not i == mirrors[current]:
            condition = False
            break
if condition:
    print('YES')
else:
    print('NO')