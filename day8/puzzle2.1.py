#INPUT_FILE = "puzzle2_ex.txt"
#input = "LR"

INPUT_FILE = "puzzle_input.txt"
input = "LLRRRLRLLRRLLRLRLRLRRLRRRLRRRLRLRRLLRLLRRRLRRLRRRLRLRRRLRRLRLRRRLRRRLRRLRLRRRLRRLRRLRRRLRLRLLRLLRLLRLRRRLRRLRRLRRRLRLRRRLRLRLRLRRRLRRRLRLRLRLRRRLRLLRRLLRLLRRLRRRLLRRRLLRRLRLRRLRLLRLLLLRRLLRRLRRLRLLLRRRLRRLRRRLRRLLRLRRRLRLLRRRLLLLRLRRRLRLRRLRRLRRLLRLRLRRLLLRRLLRLRRLRRRR"
print("Input Len:", len(input))
STEPS = 0

def follow_map(map, a_key):
    global STEPS
    
    isEnd = False
    new_key = a_key
    while not isEnd:
        for s in input:
            old_key = new_key
            new_key = get_next_step(map, old_key, s)
            STEPS += 1
            #print(old_key,"path",s,"to",new_key)

            # if all new keys end in Z, then we've found the end
            if new_key[len(new_key) - 1] == 'Z':
                isEnd = True
                break
    return new_key

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

    print(len(a_keys),"paths end with 'A':", a_keys)

    step_map = []
    for a_key in a_keys:
        next_key = follow_map(map, a_key)
        print(a_key, "=>", STEPS)
        step_map.append(STEPS)
        STEPS = 0

    stop = False
    multiplier = 1
    max = 21251
    while not stop:
        if (max * multiplier) % 11567 == 0 \
            and (max * multiplier) % 16409 == 0 \
            and (max * multiplier) % 15871 == 0 \
            and (max * multiplier) % 18023 == 0 \
            and (max * multiplier) % 14257 == 0:
            stop = True
            break
        elif multiplier % 100000000 == 0:
            print(multiplier)
        multiplier += 1
    print("Multiplier is:", multiplier,"=>",(21251*multiplier))


"""         next_key = follow_map(map, a_key)
        step_map[a_key] = [STEPS]
        while STEPS < 1000000:
            next_key = follow_map(map, next_key)
            step_map[a_key].append(STEPS)
        STEPS = 0
    print(step_map)
"""

"""     match = True
    for a_key in step_map.keys():
        for step_val in step_map[a_key]:
            match = True
            for step_arr in step_map.values():
                if not step_val in step_arr:
                    match = False
                    break
            if match:
                print("Match found at Step Val: ", step_val)
                break
        if match:
            break """

            