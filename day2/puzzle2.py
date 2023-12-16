
games = {}
MAX_GREEN = 13
MAX_BLUE = 14
MAX_RED = 12

def parseColors(colors):
    vals = [0, 0, 0]
    for color in colors:
        color = str.strip(color)
        if color.find("green") > 0:
            vals[0] = int(color.split(' ')[0])
        elif color.find("blue") > 0:
            vals[1] = int(color.split(' ')[0])
        elif color.find("red") > 0:
            vals[2] = int(color.split(' ')[0])

    return vals

with open('puzzle1_input.txt') as fh:

    i = 0
    for line in fh:
        line = str.strip(line)
        i += 1

        # put all colors for hand in an array, and all hands for a
        # game in an array, e.g., { # : [[green, blue, red], [g, b, r], ...], ...}
        hands = line.split(':')[1].split(';')
        temp_hand = []
        for hand in hands:
            colors = hand.split(',')
            vals = parseColors(colors)
            temp_hand.append(vals)
        
        games[i] = temp_hand

    # find max of each color
    powers = []
    for g in games.keys():
        max = [0, 0, 0]
        for hand in games[g]:
            if hand[0] > max[0]:
                max[0] = hand[0]
            if hand[1] > max[1]:
                max[1] = hand[1]
            if hand[2] > max[2]:
                max[2] = hand[2]
        powers.append(max[0] * max[1] * max[2])

    print(sum(powers))