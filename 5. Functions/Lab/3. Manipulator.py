import os
data = input()
while not data == 'End':
    data = data.split('-')
    command = data[0]
    if command == 'Create':
        file_name = data[1]
        open(f'{file_name}', 'w')
    elif command == 'Add':
        file_name = data[1]
        content = data[2]
        try:
            with open(f'{file_name}', 'a') as f:
                f.write(f'{content}\n')
        except FileNotFoundError:
            with open(f'{file_name}', 'w') as f:
                f.write(f'{content}\n')
    elif command == 'Replace':
        file_name = data[1]
        old_string = data[2]
        new_string = data[3]
        try:
            with open(f'{file_name}', 'rt') as f:
                cont = f.read()
                cont = cont.replace(old_string, new_string)
                f.close()
                f = open(f'{file_name}', 'wt')
                f.write(cont)
                f.close()
        except FileNotFoundError:
            print('An error occurred')
    elif command == 'Delete':
        file_name = data[1]
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print('An error occurred')
    data = input()
