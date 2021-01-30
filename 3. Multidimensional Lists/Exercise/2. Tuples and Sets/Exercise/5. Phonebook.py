line = input()
phone_book = {}
while not line.isdigit():
    name, phone = line.split('-')
    phone_book[name] = phone
    line = input()

n = int(line)
for i in range(n):
    name = input()
    if name in phone_book:
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")
