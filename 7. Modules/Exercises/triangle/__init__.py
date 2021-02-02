def print_triangle(size, n=0, triangle_list=[]):
    for i in range(1, size + 1):
        triangle_list. append(str(i))
        print(' '.join(triangle_list))
    if len(triangle_list) == 0:
        return
    triangle_list.pop()
    print(' '.join(triangle_list))
    print_triangle(0, n+1)



