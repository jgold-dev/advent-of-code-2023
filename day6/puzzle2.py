
with open('puzzle_input.txt') as fh:

    time = 51926890
    record = 222203111261225

    wins_by_time = 0
    for i in range(1, time):
        dist = i * (time - i)
        if dist > record:
            wins_by_time += 1
    
    print("# of ways to win for Time ", time, ": ", wins_by_time)
