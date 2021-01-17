n = int(input())
intersections = []
for _ in range(n):
    first, second = input().split('-')
    first_start, first_end = list(map(int, first.split(',')))
    second_start, second_end = list(map(int, second.split(',')))
    first_set = [i for i in range(first_start, first_end + 1)]
    second_set = [i for i in range(second_start, second_end + 1)]
    intersections.append(set(first_set).intersection(set(second_set)))
longest_intersection = (sorted(intersections, key= lambda x: len(x))).pop()
print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
