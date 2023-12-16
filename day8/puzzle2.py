#INPUT_FILE = "puzzle2_ex.txt"
#input = "LR"

INPUT_FILE = "puzzle_input.txt"
input = "LLRRRLRLLRRLLRLRLRLRRLRRRLRRRLRLRRLLRLLRRRLRRLRRRLRLRRRLRRLRLRRRLRRRLRRLRLRRRLRRLRRLRRRLRLRLLRLLRLLRLRRRLRRLRRLRRRLRLRRRLRLRLRLRRRLRRRLRLRLRLRRRLRLLRRLLRLLRRLRRRLLRRRLLRRLRLRRLRLLRLLLLRRLLRRLRRLRLLLRRRLRRLRRRLRRLLRLRRRLRLLRRRLLLLRLRRRLRLRRLRRLRRLLRLRLRRLLLRRLLRLRRLRRRR"
print("Input Len:", len(input))
STEPS = 0

def follow_map(map, a_keys):
    global STEPS
    
    isEnd = False
    new_keys = a_keys
    while not isEnd:
        for s in input:
            old_keys = new_keys.copy()
            for i in range(len(new_keys)):
                new_keys[i] = get_next_step(map, old_keys[i], s)
            STEPS += 1
#            print(old_keys,"path",s,"to",new_keys)

            # if all new keys end in Z, then we've found the end
            all_zzz = True
            for i in range(len(new_keys)):
                if new_keys[i][len(new_keys[i]) - 1] != 'Z':
                    all_zzz = False
            if all_zzz:
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

    a_keys = []
    for key in map.keys():
        if key[len(key) - 1] == 'A':
            a_keys.append(key)

    print(len(a_keys),"paths end with 'A':",a_keys)
    follow_map(map, a_keys)

    print("Steps:",STEPS)
