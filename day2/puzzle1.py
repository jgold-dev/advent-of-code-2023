
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
            if vals[0] > MAX_GREEN:
#                print("Green is over the max")
                return []
        elif color.find("blue") > 0:
            vals[1] = int(color.split(' ')[0])
            if vals[1] > MAX_BLUE:
#                print("Blue is over the max")
                return []
        elif color.find("red") > 0:
            vals[2] = int(color.split(' ')[0])
            if vals[2] > MAX_RED:
#                print("Red is over the max")
                return []

    return vals

with open('puzzle1_input.txt') as fh:

    i = 0
    for line in fh:
        line = str.strip(line)
        i += 1

        # put all colors for each game in a hash
        # { # : [[green, blue, red], [g, b, r], ...], ...}
        hands = line.split(':')[1].split(';')
        temp_hand = []
        for hand in hands:
            colors = hand.split(',')
            vals = parseColors(colors)
            if len(vals) == 0:
                temp_hand = []
                break
            temp_hand.append(vals)
        
        if len(temp_hand) != 0:
            games[i] = temp_hand

    print(sum(games.keys()))