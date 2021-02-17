from collections import deque
customers = list(map(int, input().split(', ')))
taxi_cars = list(map(int, input().split(', ')))
customers = deque(customers)
time = 0
no_taxis = False

while customers:
    customer = customers.popleft()
    while True:
        if taxi_cars:
            taxi = taxi_cars.pop()
            if taxi >= customer:
                break
        else:
            no_taxis = True
            break
    if no_taxis:
        customers.insert(0, customer)
        break
    time += customer

if customers:
    print(f"""Not all customers were driven to their destinations
Customers left: {', '.join(list(map(str, customers)))}
""")
else:
    print(f"""All customers were driven to their destinations
Total time: {time} minutes

""")