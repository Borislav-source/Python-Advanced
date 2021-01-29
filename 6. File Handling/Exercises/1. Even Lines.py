file = open('text.txt', 'r')
for line in file:
    line = line.split()
    for el in range(len(line)):
        for ch in range(len(line[el])):
            if line[el][ch] in ['-', ',', '.', '!', '?']:
                line[el] = line[el][:ch] + '@' + line[el][ch + 1:]
    print(*list(reversed(line)))
file.close()




