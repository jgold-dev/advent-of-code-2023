# INPUT_FILE = "puzzle1_ex.txt"
# input = "LLR"

INPUT_FILE = "puzzle_input.txt"
input = "LLRRRLRLLRRLLRLRLRLRRLRRRLRRRLRLRRLLRLLRRRLRRLRRRLRLRRRLRRLRLRRRLRRRLRRLRLRRRLRRLRRLRRRLRLRLLRLLRLLRLRRRLRRLRRLRRRLRLRRRLRLRLRLRRRLRRRLRLRLRLRRRLRLLRRLLRLLRRLRRRLLRRRLLRRLRLRRLRLLRLLLLRRLLRRLRRLRLLLRRRLRRLRRRLRRLLRLRRRLRLLRRRLLLLRLRRRLRLRRLRRLRRLLRLRLRRLLLRRLLRLRRLRRRR"

STEPS = 0

def follow_map(map, key):
    global STEPS
    
    isEnd = False
    old_key = key
    new_key = key
    while not isEnd:
        for s in input:
            old_key = new_key
            new_key = get_next_step(map, old_key, s)
#            print(old_key,"path",s,"to",new_key)
            STEPS += 1
            if new_key == 'ZZZ':
                isEnd = True
                break


def get_next_step(map, key, path):
    if path == 'L':
        return map[key][0]
    elif path == 'R':
        return map[key][1]
    else:
        print("BAD PATH: ", path)
        return 0

with open(INPUT_FILE) as fh:

    map = {}
    for line in fh:
        line = str.strip(line)
        key = line.split(" = ")[0]
        val_str = line.split(" = ")[1]
        vals = []
        vals.append(val_str.split(", ")[0][1:])
        vals.append(val_str.split(", ")[1][0:-1])
        map[key] = vals

#    print(map)
    follow_map(map, "AAA")

    print("Steps:",STEPS)
