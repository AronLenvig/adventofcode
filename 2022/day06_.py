from aocd import get_data, submit
data = get_data(day=6, year=2022).splitlines()
line = data[0]

def get_result(rep):
    return next(i+rep for i in range(0, len(line))if len(set(line[i:i + rep])) == rep)

#part1
result = get_result(4)
submit(result, part="a", day=6, year=2022)

#part2
result = get_result(14)
submit(result, part="b", day=6, year=2022)
