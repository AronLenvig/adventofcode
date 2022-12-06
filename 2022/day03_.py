from aocd import get_data, submit
data = get_data(day=3, year=2022).splitlines()

def get_int_from_letter(s : str) -> int:
    """returns an int where a = 1, z = 26, A = 27 and Z = 52"""
    if s.isupper():
        return ord(s) - 38
    else:
        return ord(s) - 96

#part1
result = 0
for line in data:
    half = int(len(line) / 2)
    compartment1 = line[0 : half]
    compartment2 = line[half : len(line)]
    result += next(get_int_from_letter(letter) for letter in compartment1 if letter in compartment2)
     
submit(result, part="a", day=3, year=2022)

#part2
result = 0
for line_index in range(0, len(data), 3):
    group1 = data[line_index]
    group2 = data[line_index + 1]
    group3 = data[line_index + 2]
    result += next(get_int_from_letter(letter) for letter in group1 if letter in group2 and letter in group3)
    
submit(result, part="b", day=3, year=2022)
