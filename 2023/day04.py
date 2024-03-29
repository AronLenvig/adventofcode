from aocd import get_data, submit
lines = get_data(day=4, year=2023).splitlines()
from pprint import pprint

# lines = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
# "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
# "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
# "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
# "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
# "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

all_cards = {}
for i in range(len(lines)):
    all_cards[i] = 1


winning_results = []
for i, line in enumerate(lines):
    a = line.split(":")
    b = a[1].split("|")
    played_cards = b[0].strip().split(" ")
    winning_card = b[1].strip().split(" ")

    w_result = 0
    for played_card in played_cards:
        if not played_card :
            continue

        if played_card in winning_card:
            w_result += 1

            # print(played_card)

            # if w_result == 0:
            #     w_result = 1
            # else:
            #     w_result = w_result * 2
    
    # winning_results.append(w_result)
    
    for j in range(w_result):
        all_cards[i + j+1] += all_cards[i]


# pprint(all_cards)

result = sum(all_cards.values())
print(result)


# print(lines[1])
# print(winning_results)

# result = sum(winning_results)


#part1
# submit(result, part="a", day=4, year=2023)

#part2
submit(result, part="b", day=4, year=2023)
