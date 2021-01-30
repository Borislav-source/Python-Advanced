import os
# try:
#     file = open('text2.txt', 'r')
# except:
#     file = open('text2.txt', 'w')
# file.close()
# os.remove('text2.txt')


# line = "-I was quick to judge him, but it wasn't his fault."
# line = line.split()
# for el in range(len(line)):
#     for ch in range(len(line[el])):
#         if line[el][ch] in ['-', ',', '.', '!', '?']:
#             line[el] = line[el][:ch] + '@' + line[el][ch + 1:]
# print(line)
# for el in range(1, len(line) + 1):
#     print(line[-el], end=' ')

a = ['sdsd.py', 'fgfg.html', 'fdfg.txt']

for el in a:
    tail = os.path.splitext(el)
    print(tail[1])