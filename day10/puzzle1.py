INPUT_FILE = "puzzle1_ex.txt"
# INPUT_FILE = "puzzle_input.txt"


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

def navigate_paths(field_map, full_paths):
    for path in full_paths:
        p = path[-1]
        # get the last item in the path and start looking
        # creating new paths for each new direction
        # Left
        left = p[1] - 1 
        if left > 0:
            if field_map[p[0]][left] not in ['7','J']:
                path.append([p[0]], left)


field_map = {}  # key is row, array is column
start = []      # Coordinate Pair: [row, column]
with open(INPUT_FILE) as fh:
    for line in fh:
        line = str.strip(line)
        field_row = []
        row = 0
        for c in range(len(line)):
            field_row.append(line[c])
            if line[c] == 'S':
                start = [len(field_map), c]
            row += 1
        field_map[row] = field_row
# Based on Start, go through all directions of all paths
# However, there are rules.
# Looking left, cannot go to west, 7 or J
# Looking right, cannot go east, L or F
# Looking down, cannot go vertical, |
# Looking up, cannot go horizontal, -
# And ground is a dead-end
full_paths = [[start]]
navigate_paths(field_map, full_paths)

max_path_len = 0
for path in full_paths:
    print(path)
    if len(path) > max_path_len:
        max_path_len =len(path)
print("Max Path Len is:", max_path_len - 1)