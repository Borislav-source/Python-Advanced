import sys
n = int(input())
stack = []
maxx = 0
minn = sys.maxsize
for i in range(n):
    data = input().split()
    command = data[0]
    if command == '1':
        number = data[1]
        stack.append(number)
        number = int(number)
        if number < minn:
            minn = number
    elif command == '2':
        if stack:
            old_num = int(stack.pop())
    elif command == '3':
        for k in stack:
            if int(k) > maxx:
                maxx = int(k)
        print(maxx)
    elif command == '4':
        print(minn)
print(', '.join(stack[::-1]))
