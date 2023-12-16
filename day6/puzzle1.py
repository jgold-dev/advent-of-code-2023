
with open('puzzle_input.txt') as fh:

    times = []
    records = []
    for line in fh:
        line = str.strip(line)

        if line.startswith("Time"):
            times = str.strip(line.split(':')[1]).split(' ')
            times = list(filter(None, times))
            times = list(map(int, times))
        else:
            records = str.strip(line.split(':')[1]).split(' ')
            records = list(filter(None, records))
            records = list(map(int, records))

    print(times)
    print(records)

    index = 0
    winning_options = []
    for t in times:
        record = records[index]
        wins_by_time = 0
        for i in range(1, t):
            dist = i * (t - i)
            if dist > record:
                wins_by_time += 1
        
        print("# of ways to win for Time ", t, ": ", wins_by_time)
        winning_options.append(wins_by_time)
    
        index += 1

    product = 1
    for w in winning_options:
        product = product * w

    print("Product =", product)



