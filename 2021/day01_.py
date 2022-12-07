from aocd import get_data, submit
lines = get_data(day=1, year=2021).splitlines()
lines = list(map(int,lines))

#part1
result = sum(1 for i in range(0,len(lines)-1)if lines[i] < lines[i+1])
submit(result, part="a", day=1, year=2021)

#part2
result = sum(1 for i in range(0,len(lines)-3)if lines[i]+lines[i+1]+lines[i+2] < lines[i+1]+lines[i+2]+lines[i+3])
submit(result, part="b", day=1, year=2021)
