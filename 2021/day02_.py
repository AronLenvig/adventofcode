from aocd import get_data, submit
lines = get_data(day=2, year=2021).splitlines()
print(lines)

#part1
horizontal = 0
depth = 0
for line in lines:
    words = line.split()
    if words[0] == "forward":
        horizontal += int(words[1])
    elif words[0] == "up":
        depth -= int(words[1])
    else:
        depth += int(words[1])

result = horizontal * depth
submit(result, part="a", day=2, year=2021)

#part2
horizontal = 0
depth = 0
aim = 0
for line in lines:
    words = line.split()
    if words[0] == "forward":
        horizontal += int(words[1])
        aim += int(words[1]) * depth
    elif words[0] == "up":
        depth -= int(words[1])
    else:
        depth += int(words[1])

result = horizontal * aim
submit(result, part="b", day=2, year=2021)
