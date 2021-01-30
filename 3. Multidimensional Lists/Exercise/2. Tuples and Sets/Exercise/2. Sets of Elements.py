n, m = list(map(int, input().split()))
n_list = []
m_list = []
for i in range(1, n + m + 1):
    if i <= n:
        n_list.append(input())
    else:
        m_list.append(input())
set_1 = set(n_list)
set_2 = set(m_list)

set_3 = set_1.intersection(set_2)
for number in set_3:
    print(number)