from aocd import get_data,submit

def get_int_from_letter(c : str) -> int:
    """returns an int where a = 1, z = 26, A = 27 and Z = 52"""
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96

def part1(data : list) -> int:
    """find the letter that is in all three compartments and add the value of the letter to the result"""
    result = 0
    for line in data:
        half = int(len(line) / 2)
        compartment1 = line[0 : half]
        compartment2 = line[half : len(line)]
        #find a letter that is in both compartments
        for letter in compartment1:
            if letter in compartment2:
                result += get_int_from_letter(letter)
                break
    return result
        
def part2(data : list) -> int:
    """find the letter that is in all three lines and add the value of the letter to the result"""
    result = 0
    for line_index in range(0, len(data), 3):
        group1 = data[line_index]
        group2 = data[line_index + 1]
        group3 = data[line_index + 2]
        #find a letter that is in all three groups
        for letter in group1:
            if letter in group2 and letter in group3:
                result += get_int_from_letter(letter)
                break
    return result
        
if __name__ == "__main__":
    data = get_data(day=3, year=2022).splitlines()

    print(part1(data))
    print(part2(data))

    #submit(part1(data), part="a", day=3, year=2022)
    #submit(part2(data), part="b", day=3, year=2022)
