
with open('puzzle_input.txt') as fh:

    orig_card_count = 6
    card_winners = {}
    card_count = {}
    card = 1
    for line in fh:
        line = str.strip(line)

        all_nums = line.split(":")[1]
        winning_nums = all_nums.split('|')[0].split(' ')
        while "" in winning_nums:
            winning_nums.remove("")
        card_nums = all_nums.split('|')[1].split(' ')
        while "" in card_nums:
            card_nums.remove("")

        winners = list(set(winning_nums) & set(card_nums))
        card_winners[card] = len(winners)
        card_count[card] = 1
        card += 1

    print("Card Win Count: ", card_winners)
    for card in card_winners.keys():
        for i in range(1, card_winners[card] + 1):
            card_count[card + i] += 1
        for x in range(1, card_count[card]):
            for i in range(1, card_winners[card] + 1):
                card_count[card + i] += 1
#        print("Card ", card, ": ", card_count)

    print("Final Card Count: ", card_count)
    print("Total # of Cards: ", sum(card_count.values()))
    