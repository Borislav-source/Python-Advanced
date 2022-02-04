def pascal_triangle(rows):
    previous_list = []
    for r in range(1, rows + 1):
        current_list = list('1' * r)
        current_list = list(map(int, current_list))
        if len(current_list) > 2:
            for index in range(1, len(current_list) - 1):
                current_list[index] = previous_list[index - 1] + previous_list[index]
        previous_list = current_list
        print(current_list)
    return


clients_input = int(input())
pascal_triangle(clients_input)
