import os

directory = r'input the directory path'
files = {}
for file_name in os.listdir(directory):
    tail = os.path.splitext(file_name.lower())
    if '' not in tail:
        if tail[1] not in files:
            files[tail[1]] = []
        files[tail[1]].append(file_name)

for key, value in sorted(files.items(), key=lambda x: (x[0], x[1])):
    try:
        file = open('report.txt', 'a')
        file.write(f'{key}\n')
        for el in value:
            file.write(f"---{el}\n")
        file.close()
    except FileNotFoundError:
        with open('report.txt', 'w') as file:
            file.write(key)
            for el in value:
                file.write(f"---{el}")
