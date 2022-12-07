from aocd import get_data, submit
data = get_data(day=7, year=2022).splitlines()
from collections import defaultdict

dirs_size = defaultdict(int)
paths = []

for line in data:
    words = line.split(" ")
    if words[1] == "cd":
        if words[2] == "..":
            paths.pop()
        else:
            paths.append(words[2])
    elif words[1] == "ls":
        continue
    elif words[0] == "dir":
        continue
    else:
        for i in range(len(paths)):
            dirs_size["/".join(paths[:i+1])] += int(words[0])

max_size = 100_000
result = sum([value for value in dirs_size.values() if value < max_size])
submit(result, part="a", day=7, year=2022)

#part2
space_needed = 70000000 - 30000000
size_needed_to_delete =  dirs_size["/"] - space_needed
result = min([value for value in dirs_size.values() if value > size_needed_to_delete])
submit(result, part="b", day=7, year=2022)
