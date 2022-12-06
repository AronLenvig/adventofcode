from aocd import get_data, submit
data = get_data(day=6, year=2022).splitlines()
line = data[0]

def reaping_last_index(number):
    return next(index+number for index in range(0, len(line)) if len(set(line[index:index + number])) == number)

#part1
result = reaping_last_index(4)
submit(result, part="a", day=6, year=2022)

#part2
result = reaping_last_index(14)
submit(result, part="b", day=6, year=2022)
