from aocd import get_data, submit
from pprint import pprint
from functools import lru_cache

@lru_cache(maxsize=128)
def is_symbol(letter: str) -> bool:
    # should not be a number or valid latter
    if letter.isalpha():
        return False
    if letter.isdigit():
        return False
    if letter == ".":
        return False
    return True


lines = get_data(day=3, year=2023).splitlines()

# lines = ["467..114..",
# "...*......",
# "..35..633.",
# "......#...",
# "617*......",
# ".....+.58.",
# "..592.....",
# "......755.",
# "...$.*....",
# ".664.598.."]


indexed_lines = {}
numbers = {}
symbols = {}
for line_index, line in enumerate(lines):
    indexed_lines[line_index] = {}
    for letter_index, letter in enumerate(line):
        indexed_lines[(int(line_index), int(letter_index))] = letter
        if letter.isdigit():
            numbers[(int(line_index), int(letter_index))] = letter
        if is_symbol(letter):
            symbols[(int(line_index), int(letter_index))] = letter

connected_numbers = []
last_key = (-1,-1)
str_real_number = []
for key, letter in numbers.items():
    # check if last numbers
    if not str_real_number:
        str_real_number.append((key, letter))
        last_key = key
        continue
    if key[0] != last_key[0]:
        number = int("".join([x[1] for x in str_real_number]))
        first_key = str_real_number[0][0]
        connected_numbers.append({'nr': number, 'first_key': first_key, 'lenght': len(str_real_number)})
        str_real_number.clear()
        str_real_number.append((key, letter))
        last_key = key
        continue
    if key[1] != last_key[1] + 1:
        number = int("".join([x[1] for x in str_real_number]))
        first_key = str_real_number[0][0]
        connected_numbers.append({'nr': number, 'first_key': first_key, 'lenght': len(str_real_number)})
        str_real_number.clear()
        str_real_number.append((key, letter))
        last_key = key
        continue
    if key[1] == last_key[1] + 1:
        str_real_number.append((key, letter))
        # uf last number just add it
        if key == list(numbers.keys())[-1]:
            number = int("".join([x[1] for x in str_real_number]))
            first_key = str_real_number[0][0]
            connected_numbers.append({'nr': number, 'first_key': first_key, 'lenght': len(str_real_number)})
            str_real_number.clear()
            str_real_number.append((key, letter))
        last_key = key
        continue
    raise Exception("Should not be here")
# add the last number



def check_symbol_serounds_number(line_index, letter_index):
    for i in range(3):
        i = i - 1
        for j in range(3):
            j = j - 1
            if (line_index + i, letter_index + j) in list(symbols.keys()):
                return True
    return False

def get_all_connected_number_serounding_symbol(symbol_key):
    line_index = symbol_key[0]
    letter_index = symbol_key[1]
    added_connected_number = []
    numbers = []
    for i in range(3):
        i = i - 1
        for j in range(3):
            j = j - 1
            for connected_number in connected_numbers:
                if connected_number in added_connected_number:
                    continue
                for nr in range(connected_number['lenght']):
                    if (line_index + i, letter_index + j) == (connected_number['first_key'][0], connected_number['first_key'][1] + nr):
                        numbers.append(connected_number['nr'])
                        added_connected_number.append(connected_number)
                        break
    return numbers

connected_number_with_symbols = []
# connected_number_with_gears = []
for connected_number in connected_numbers:
    line_index = connected_number['first_key'][0]
    for nr in range(connected_number['lenght']):
        letter_index = connected_number['first_key'][1] + nr

        if check_symbol_serounds_number(line_index, letter_index):
            connected_number_with_symbols.append(connected_number['nr'])
            break

        # if check_gear_serounds_number(line_index, letter_index):
        #     connected_number_with_gears.append(connected_number['nr'])
        #     break

        # check if any symbols serounds the number


gears = []
symbols_with_gears = [key for key, value in symbols.items() if value == "*"]
print(symbols_with_gears)
for key in symbols_with_gears:
    # if letter != "*":
    #     continue
    gears_numbers = get_all_connected_number_serounding_symbol(key)
    # print(gears_numbers)
    if len(gears_numbers) > 1:
        # multiply all the gears_numbers together not just append them multiply first. Never just "gears.append(gears_numbers)" very bad
        gears.append(gears_numbers[0] * gears_numbers[1])



# pprint(lines[0:3])

# pprint()
# pprint(gears)
# pprint([key for key, value in symbols.items() if value == "*"])

# result = sum(connected_number_with_symbols)
result = sum(gears)
        

# print(result)

#part1
# submit(result, part="a", day=3, year=2023)

#part2
# submit(result, part="b", day=3, year=2023)
