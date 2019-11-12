import numpy as np

b_arr = np.random.poisson(6, 120)
c1_arr = np.random.poisson(3, 120)
c2_arr = np.random.poisson(1, 120)
c3_arr = np.random.poisson(4, 120)

t = 0
bikes = 10
profit = 0

while t < 120:
    # Bike Arrivals
    bikes += b_arr[t]

    # Customer 1
    c1 = c1_arr[t]
    t1_profit = 0
    t2_profit = 0
    if c1 > bikes:
        t1_profit += bikes * .5
        t1_profit -= abs((c1 - bikes) * 1)
        bikes = 0
    else:
        t_1profit = c1 * .5
        bikes = bikes - c1

    # Customer 2
    c2 = c2_arr[t]
    if c2 > bikes:
        t2_profit += bikes * .1
        t2_profit -= abs((c2 - bikes) * 0.25)
        bikes = 0
    else:
        t2_profit = c2 * .1
        bikes = bikes - c2

    # Calculating aggregated profit/loss for C1 + C2 membership customers
    profit += (t1_profit + t2_profit) * 120

    # Customer 3
    c3 = c3_arr[t]
    if c3 > bikes:
        profit += bikes * 1.25
        profit -= 0
        bikes = 0
    else:
        profit += c3 * 1.25
        bikes = bikes - c3

    t += 1

print("Total Profit: " + str(profit))
