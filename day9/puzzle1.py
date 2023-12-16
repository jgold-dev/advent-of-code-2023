#INPUT_FILE = "puzzle1_ex.txt"
INPUT_FILE = "puzzle_input.txt"

def calc_diffs(history, diffs):
    diff_hist = [None] * (len(history) - 1)
    for i in range(len(history) - 1):
        diff_hist[i] = history[i + 1] - history[i]
    all_zeroes = True
    for i in range(len(diff_hist) - 1):
        if diff_hist[i] != 0:
            all_zeroes = False
            break
    diffs.append(diff_hist)
    if not all_zeroes:
        return calc_diffs(diff_hist, diffs)
    else:
        return 0

histories = []
with open(INPUT_FILE) as fh:
    for line in fh:
        line = str.strip(line)
        history = list(map(int, line.split(' ')))
        histories.append(history)   

histories_next = {}
for history in histories:
    print("History:",history)
    diffs = []
    calc_diffs(history, diffs)
#    for i in range(len(diffs) - 1):
#        print(diffs[i])
    
    last_diff = 0
    for i in reversed(range(0, len(diffs) - 1)):
        last_diff = diffs[i][0] - last_diff
    print("Last Diff:", last_diff)
    histories_next[histories.index(history)] = history[0] - last_diff
print("Sum of Next Vals:", sum(histories_next.values()))
