
card_map = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, \
            '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, \
            '4': 4, '3': 3, '2': 2, 'J': 1 }

HIGH, ONE, TWO, THREE, FULL, FOUR, FIVE = range(7)

def get_card_count(card_no, hand):
    card_count = 0
    for c in hand:
        if c == card_no:
            card_count += 1
    return card_count

def identify_hand(hand)

def sort_cards(cards):
    sorted_cards = []
    for c in cards:
        for sc in sorted_cards:
            rc = compare_cards(c, sc)
            if rc == -1:
                sorted_cards.insert(sorted_cards.index(sc), c)
                break
        if c not in sorted_cards:
            sorted_cards.append(c)

    return sorted_cards

def compare_cards(c1, c2):
    # c1 is new card, c2 is old card
    for index in range(5):
        if card_map[c1[index]] > card_map[c2[index]]:
            return -1
        elif card_map[c1[index]] < card_map[c2[index]]:
            return 1
        else:
            continue

    return 0


with open('puzzle1_ex.txt') as fh:

    hands = {}
    hand_ranks = {}
    hand_types = {}
    hand_wilds = {}
    for line in fh:
        line = str.strip(line)
        line_split = line.split(' ')
        hands[line_split[0]] = int(line_split[1])

    high_rank = len(hands)
    five_k = []
    four_k= []
    fh_k = []
    three_k = []
    two_p = []
    one_p = []
    high = []
    for hand in hands.keys():
        # Figure out what type of hand this is
        # Get a count of each card in the hand { card: count }
        has5K = False
        has4K = False
        has3K = False
        hasFH = False
        has2P = False 
        has1P = False
        good_cards = []
        for c in card_map.keys():
            count = get_card_count(c, hand)
            if count == 5:
                good_cards.append(c)
                has5K = True
                break
            elif count == 4:
                good_cards.append(c)
                has4K = True
                break
            elif count == 3:
                good_cards.append(c)
                has3K = True
            elif count == 2:
                if not has1P and not has2P:
                    has1P = True
                elif not has2P:
                    has2P = True
                    has1P = False
                good_cards.append(c)

        # Do we have any Jokers?
        if 'J' in hand:
            if has5K:
                hand_wilds[hand] = hand.replace("J","A")
            elif has4K:
                # replace good cards with wild. its now 5K
                hand_wilds[hand] = hand.replace("J", good_cards[0])
                has4K = False
                has5K = True
            elif has3K:
                # replace good cards with wild. its now 4K
                hand_wilds[hand] = hand.replace("J", good_cards[0])
                has3K = False
                has4K = True
            elif has1P:
                # replace good cards with wild. its now 3K
                hand_wilds[hand] = hand.replace("J", good_cards[0])
                has3K = True
                has1P = False
            elif has2P:
                # replace good cards with wild. its now FH
                if card_map[good_cards[0]] > card_map[good_cards[1]]:
                    hand_wilds[hand] = hand.replace("J", good_cards[0])
                else:
                    hand_wilds[hand] = hand.replace("J", good_cards[1])
                has3K = True
                has1P = True
                has2P = False
            else:
                # high card is now 1P
                high_card = 'J'
                for c in range(len(hand)):
                    if card_map[hand[c]] > high_card:
                        high_card = hand[c]
                hand_wilds[hand] = hand.replace("J", high_card)
                has1P = True
            print("Wilds! ", hand, "=>", hand_wilds[hand])

        if has3K and (has1P or has2P):
            hasFH = True

        if has5K:
            five_k.append(hand)
            hand_types[hand] = FIVE
        elif has4K:
            four_k.append(hand)
            hand_types[hand] = FOUR
        elif hasFH:
            fh_k.append(hand)
            hand_types[hand] = FULL
        elif not hasFH and has3K:
            three_k.append(hand)
            hand_types[hand] = THREE
        elif not hasFH and has2P:
            two_p.append(hand)
            hand_types[hand] = TWO
        elif not hasFH and has1P:
            one_p.append(hand)
            hand_types[hand] = ONE
        else:
            high.append(hand)
            hand_types[hand] = HIGH

        # Figure out total hand and assign type
        print (hand, "is a", hand_types[hand])

    # Within each each, sort the rank and assign
    # for each character in the map, see what hands start with that character
    # For all the ones that are the same, go to the next card in the hand
    # 
    if len(five_k) > 1:
        five_k  = sort_cards(five_k)
    if len(four_k) > 1:
        four_k  = sort_cards(four_k)
    if len(fh_k) > 1:
        fh_k    = sort_cards(fh_k)
    if len(three_k) > 1:
        three_k = sort_cards(three_k)
    if len(two_p) > 1:
        two_p   = sort_cards(two_p)
    if len(one_p) > 1:
        one_p   = sort_cards(one_p)
    if len(high) > 1:
        high    = sort_cards(high)

    cur_rank = high_rank
    for h in five_k:
        hand_ranks[h] = cur_rank
        cur_rank -= 1
    for h in four_k:
        hand_ranks[h] = cur_rank
        cur_rank -= 1
    for h in fh_k:
        hand_ranks[h] = cur_rank
        cur_rank -= 1
    for h in three_k:
        hand_ranks[h] = cur_rank
        cur_rank -= 1
    for h in two_p:
        hand_ranks[h] = cur_rank
        cur_rank -= 1
    for h in one_p:
        hand_ranks[h] = cur_rank
        cur_rank -= 1
    for h in high:
        hand_ranks[h] = cur_rank
        cur_rank -= 1

    # go through hash and multiply rank by bid
    for h in hand_ranks:
        print(h, hand_ranks[h])
    print(hand_ranks)

    sum = 0
    for h in hands:
        sum += hands[h] * hand_ranks[h]

    print("Sum:", sum)