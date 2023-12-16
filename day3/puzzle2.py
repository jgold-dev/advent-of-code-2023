MAX_ROW_LEN = 140
charmap = []
parts = {}    # part_num: [row, index]
symbols = {}  # overall index

def getAdjParts(row, index):
    matches = []
    # Left
    if charmap[row][index - 1].isdigit():
        matches.append(getPartAtLoc(row, index - 1))
    # Right
    if charmap[row][index + 1].isdigit():
        matches.append(getPartAtLoc(row, index + 1))
    # Down
    if charmap[row + 1][index].isdigit():
        matches.append(getPartAtLoc(row + 1, index))
    # Up
    if charmap[row - 1][index].isdigit():
        matches.append(getPartAtLoc(row - 1, index))
    # Upper Left
    if charmap[row - 1][index - 1].isdigit():
        matches.append(getPartAtLoc(row - 1, index - 1))
    # Lower Left
    if charmap[row + 1][index - 1].isdigit():
        matches.append(getPartAtLoc(row + 1, index - 1))
    # Upper Right
    if charmap[row - 1][index + 1].isdigit():
        matches.append(getPartAtLoc(row - 1, index + 1))
    # Lower Right
    if charmap[row + 1][index + 1].isdigit():
        matches.append(getPartAtLoc(row + 1, index + 1))

    return list(dict.fromkeys(matches))

def getPartAtLoc(row, index):
    for part in parts.keys():
        if parts[part][0] == row and (index >= parts[part][1] and index <= parts[part][2]):
            return part.split('-')[0]
    return -1

with open('puzzle_input.txt') as fh:

    row = 0
    cur_num = ""
    cur_index = -1
    for line in fh:
        line = str.strip(line)

        if cur_num != "":
            key = cur_num + '-' + str(row-1) + '-' + str(cur_index)
            parts[key] = [row-1, cur_index, index - 1]
            cur_num = ""
            cur_index = -1

        line_array = []
        index = 0
        for c in line:
            line_array.append(c)
            if c.isdigit():
                if cur_num == "":
                    cur_index = index
                cur_num = cur_num + c
            else:
                if c != '.':
                    overall_index = (MAX_ROW_LEN * row) + index
                    symbols[overall_index] = c
                if cur_num != "":
                    key = cur_num + '-' + str(row) + '-' + str(cur_index)
                    parts[key] = [row, cur_index, index - 1]
                    cur_num = ""
                    cur_index = -1
            index += 1

        charmap.append(line_array)
        row += 1

    print("Potential Parts ", len(parts) , ": ", parts)

    actual_parts = []
    row = 0
    for line in charmap:
        for index in range(len(line)):
            if line[index] == '*':
                # Does it have exactly 2 adjacent digits
                # if so, multiply them together
                matches = getAdjParts(row, index)
                print(matches)
                if len(matches) == 2:
                    actual_parts.append(int(matches[0]) * int(matches[1]))
        row += 1

#    print("Actual Parts ", len(actual_parts) , ": ", actual_parts)
    actual_parts = list(map(int, actual_parts))
    print("Gears ", len(actual_parts) , ": ", actual_parts)
    print("Sum of Gears: ", sum(actual_parts))