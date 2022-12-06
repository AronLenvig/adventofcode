from aocd import get_data, submit
data = get_data(day=1, year=2021).splitlines()
data = list(map(int,data))

#part1
result = sum(1 for i in range(0,len(data)-1)if data[i] < data[i+1])
submit(result, part="a", day=1, year=2021)

#part2
result = sum(1 for i in range(0,len(data)-3)if data[i]+data[i+1]+data[i+2] < data[i+1]+data[i+2]+data[i+3])
submit(result, part="b", day=1, year=2021)
