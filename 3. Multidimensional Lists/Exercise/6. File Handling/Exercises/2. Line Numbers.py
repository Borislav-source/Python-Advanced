try:
    file = open('text.txt', 'r')
except FileNotFoundError:
    file = open('text.txt', 'w')
line_number = 0
for line in file:
    letters = 0
    punctuation = 0
    line_number += 1
    for ch in line:
        if ch.isalpha():
            letters += 1
        else:
            if not ch.isspace():
                punctuation += 1
    with open('output.txt', 'a') as out_file:
        out_file.write(f"Line {line_number}: {line.strip()}({letters})({punctuation})\n")
file.close()
