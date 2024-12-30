from aocd import get_data, submit
lines = get_data(day=4, year=2021).splitlines()
# print(lines)

# lines = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
# """.splitlines()
lines.append("")



class BingoPlade:
    """BingoPlade 5 columns.
        numbers: list of 25 numbers"""
    def __init__(self, numbers):
        self.numbers = numbers
        self.columns = [numbers[0:5], numbers[5:10], numbers[10:15], numbers[15:20], numbers[20:25]]
        self.bingo_numbers_column_with_bingo = []


    
    def check_if_any_column_is_bingo(self, bingo_numbers):
        for column in self.columns:
            if all(number in bingo_numbers for number in column):
                self.bingo_numbers_column_with_bingo = column
                return True
        return False
    
    def get_bingo_col_with_bingo(self):
        return self.bingo_numbers_column_with_bingo
    
    def get_sum_of_all_numbers_not_in_bingo_numbers(self, bingo_numbers):
        return sum(number for number in self.numbers if number not in bingo_numbers)

    

#map lines[0] to int bingo_numbers and split , to list
bingo_numbers = [int(number.strip()) for number in lines[0].split(",")]
# print(bingo_numbers)
bingo_plades = []
plade_numbers = []
for line in lines[2:]:
    numbers = line.split(",")
    if numbers[0] == "":
        bingo_plades.append(BingoPlade(plade_numbers))
        # print(plade_numbers)
        plade_numbers = []
    else:
        numbers_list = [int(number.strip()) for number in numbers[0].split(" ") if number != ""]
        plade_numbers.extend(numbers_list)

# for bingo_plade in bingo_plades:
#     print(bingo_plade.check_if_any_column_is_bingo(bingo_numbers[0:25]))

current_bingo_numbers_selected = []
# for bingo_plade in bingo_plades:
#     print(bingo_plade.numbers)
# loop through the bingo_numbers add them to current_bingo_numbers_selected and check if any of the bingo_plades is bingo
for bingo_number in bingo_numbers:
    current_bingo_numbers_selected.append(bingo_number)
    # print(current_bingo_numbers_selected)
    
    for bingo_plade in bingo_plades:
        # print(bingo_plade.numbers)
        if bingo_plade.check_if_any_column_is_bingo(current_bingo_numbers_selected):
            print("BINGO")
            print(bingo_plade.numbers)
            print(current_bingo_numbers_selected)

            # find all bingo_plade.numbers not in current_bingo_numbers_selected
            print(sum([number for number in bingo_plade.numbers if number not in current_bingo_numbers_selected]))

            # print(bingo_plade.get_bingo_col_with_bingo())
            print(bingo_number)
            # # print the the plade that was bingo
            sum_of_all_none_selected_in_plade = bingo_plade.get_sum_of_all_numbers_not_in_bingo_numbers(current_bingo_numbers_selected)

            # print(sum_of_all_none_selected_in_plade)
            print(sum_of_all_none_selected_in_plade * bingo_number)
            exit()

#part1
#submit(result, part="a", day=4, year=2021)


#part2
#submit(result, part="b", day=4, year=2021)
