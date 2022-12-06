from aocd import get_data, submit
data = get_data(day=1, year=2022).splitlines()

def add_numbers_seperated_by_spaces(data: list[str]) -> int:
    indexes = [-1]
    indexes.extend([index for index, nr in enumerate(data) if nr == ""])
    return [sum(map(int, data[indexes[i-1]+1:indexes[i]])) for i in range(1,len(indexes))]

#part1
result = max(add_numbers_seperated_by_spaces(data))
submit(result, part="a", day=1, year=2022)

#part2
result = sum(sorted(add_numbers_seperated_by_spaces(data))[-3:])
submit(result, part="b", day=1, year=2022)


