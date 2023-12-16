MAX_ROW_LEN = 140
charmap = []
parts = {}    # part_num: [row, index]
symbols = {}  # overall index

def hasAdjSymbol(row, index):
    # does the row and the index in the row have an adjacent symbol
    # Left
    if ((MAX_ROW_LEN * row) + (index - 1)) in symbols.keys():
        return True
    # Right
    if ((MAX_ROW_LEN * row) + (index + 1)) in symbols.keys():
        return True
    # Down
    if ((MAX_ROW_LEN * (row + 1)) + index) in symbols.keys():
        return True
    # Up
    if ((MAX_ROW_LEN * (row - 1)) + index) in symbols.keys():
        return True
    # Upper Left
    if ((MAX_ROW_LEN * (row - 1)) + (index - 1)) in symbols.keys():
        return True    
    # Lower Left
    if ((MAX_ROW_LEN * (row + 1)) + (index - 1)) in symbols.keys():
        return True   
    # Upper Right
    if ((MAX_ROW_LEN * (row - 1)) + (index + 1)) in symbols.keys():
        return True
    # Lower Right
    if ((MAX_ROW_LEN * (row + 1)) + (index + 1)) in symbols.keys():
        return True

    return False

def getPartAtLoc(row, index):
    for part in parts.keys():
        if parts[part][0] == row and parts[part][1] == index:
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
            parts[key] = [row-1, cur_index]
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
                    parts[key] = [row, cur_index]
                    cur_num = ""
                    cur_index = -1
            index += 1

        charmap.append(line_array)
        row += 1

#    print("Potential Parts ", len(parts) , ": ", parts)
#    print("Symbols: ", symbols)

    actual_parts = []
    row = 0
    for line in charmap:
        cur_index = -1
        skipAhead = False
        for index in range(len(line)):
            if line[index].isdigit():
                if cur_index == -1:
                    cur_index = index
                if not skipAhead and hasAdjSymbol(row, index):
                    part_num = getPartAtLoc(row, cur_index)
                    actual_parts.append(part_num)
                    skipAhead = True
            else:
                cur_index = -1
                skipAhead = False
            
        row += 1

#    print("Actual Parts ", len(actual_parts) , ": ", actual_parts)
    actual_parts = list(map(int, actual_parts))
    print("\nActual Parts ", len(actual_parts) , ": ", actual_parts)
    print("Sum of Actual Parts: ", sum(actual_parts))