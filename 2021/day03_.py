from aocd import get_data, submit
lines = get_data(day=3, year=2021).splitlines()
from collections import defaultdict, Counter

#part1

list_bineries = defaultdict(list)
for line in lines:
    for i in range(len(line)):
        list_bineries[i].append(line[i])

most_commons = []
least_commons = []
for bineries in list_bineries.values():
    most_commons.append(Counter(bineries).most_common(1)[0][0])
    least_commons.append(Counter(bineries).most_common()[-1][0])

gamma = int("".join(most_commons),2)
epsilon = int("".join(least_commons),2)
result = gamma * epsilon

submit(result, part="a", day=3, year=2021)

#part2
#submit(result, part="b", day=3, year=2021)
