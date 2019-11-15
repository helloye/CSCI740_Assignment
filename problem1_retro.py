import numpy as np

t = 0
bike_count = 10
profit_count = 0
b_arr = 0.0
c1_arr = 0.0
c2_arr = 0.0
c3_arr = 0.0

def generate_new_arrivals():
    global b_arr
    b_arr = np.random.poisson(6, 1)
    global c1_arr
    c1_arr = np.random.poisson(3, 1)
    global c2_arr
    c2_arr = np.random.poisson(1, 1)
    global c3_arr
    c3_arr = np.random.poisson(4, 1)


def generate_new_arrival_single(type):
    if type is 'b':
        global b_arr
        b_arr = np.random.poisson(6, 1)
    elif type is 'c1':
        global c1_arr
        c1_arr = np.random.poisson(3, 1)
    elif type is 'c2':
        global c2_arr
        c2_arr = np.random.poisson(1, 1)
    elif type is 'c3':
        global c3_arr
        c3_arr = np.random.poisson(4, 1)


def print_current_arrivals():
    print("Bike = " + str(b_arr))
    print("Customer 1 = " + str(c1_arr))
    print("Customer 2 = " + str(c2_arr))
    print("Customer 3 = " + str(c3_arr))

def get_next_event(bike, c1, c2, c3):
    l = (bike, c1, c2, c3)
    min_index = l.index(min(l))

    if min_index is 0:
        return { 'type': 'bike', 'value': bike }
    elif min_index is 1:
        return { 'type': 'c1', 'value': c1 }
    elif min_index is 2:
        return { 'type': 'c2', 'value': c2 }
    elif min_index is 3:
        return { 'type': 'c3', 'value': c3 }

# Count default to 1, assume only 1 count of the event happens (i.e add 1 bike, 1 customer, etc...)
def evaluate_event(type, count=1):
    global profit_count, bike_count
    if type is 'bike':
        bike_count += count
    elif type is 'c1':
        # If more customers than bike
        if count > bike_count:
            profit_count += bike_count * 0.5
            profit_count -= abs((count - bike_count) * 1)
            bike_count = 0
        else:
            profit_count = count * 0.5
            bike_count -= count
    elif type is 'c2':
        # If more customers than bike
        if count > bike_count:
            profit_count += bike_count * 0.1
            profit_count -= abs((count - bike_count) * 0.25)
            bike_count = 0
        else:
            profit_count = count * 0.1
            bike_count -= count
    elif type is 'c3':
        # If more customers than bike
        if count > bike_count:
            profit_count += bike_count * 1.25
            bike_count = 0
        else:
            profit_count = count * 1.25
            bike_count -= count

def print_system_state():
    global bike_count, profit_count, t
    print(str(t) + ") Bike:" + str(bike_count) + " " + "Profit:" + str(profit_count))

def reset_system():
    global t, profit_count, bike_count
    t = 0
    profit_count = 0
    bike_count = 10

'''
MAIN PROGRAM LOOP
'''
for i in range(1, 6):
    generate_new_arrivals()
    while t < 120:
        next_event = get_next_event(b_arr[0], c1_arr[0], c2_arr[0], c3_arr[0])
        evaluate_event(next_event['type'])
        t += next_event['value']
        generate_new_arrival_single(next_event['type'])

    print("Final profit: " + str(profit_count))
    reset_system()
