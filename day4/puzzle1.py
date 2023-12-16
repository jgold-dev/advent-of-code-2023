
with open('puzzle_input.txt') as fh:

    # Points is 1-2-4-8, or 2^(n-1)
    scores = []
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
        if len(winners) > 0:
            score = pow(2, len(winners) - 1)
            scores.append(score)

        print(winning_nums, " | ", card_nums, " => ", winners, " == ", score)

    print("Sum of Scores: ", sum(scores))
