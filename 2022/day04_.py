from aocd import get_data, submit
data = get_data(day=4, year=2022).splitlines()

#part1
result = 0
for line in data:
    a = line.split(",")
    a1 = list(map(int,a[0].split("-")))
    a2 = list(map(int,a[1].split("-")))
    if  a1[0] <= a2[0] and a1[1] >= a2[1]:
        result += 1
        continue
    if  a2[0] <= a1[0] and a2[1] >= a1[1]:
        result += 1
        continue
submit(result, part="a", day=4, year=2022)

#part2
result = 0
for line in data:
    a = line.split(",")
    a1 = list(map(int,a[0].split("-")))
    a2 = list(map(int,a[1].split("-")))
    if  a1[0] <= a2[0] <= a1[1] or a1[0] <= a2[1] <= a1[1]:
        result += 1
        continue
    if  a2[0] <= a1[0] <= a2[1] or a2[0] <= a1[1] <= a2[1]:
        result += 1
        continue
submit(result, part="b", day=4, year=2022)
