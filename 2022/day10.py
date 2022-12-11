from aocd import get_data, submit
data = get_data(day=10, year=2022).splitlines()

#part1
lines = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()

from collections import deque
map_circles = ""
result = 0
cycle_value = 1
cycle = 0
index = 0
list_of_cycles = deque([20,60,100,140,180,220])
for line in data:
    words = line.split()
    #addx takes two cycles to complete, noop takes one cycle
    if words[0] == "addx":
        cycle += 2
        cycle_value += int(words[1])
        if int(words[1]) > 0:
            map_circles += "#"
            map_circles += "#"

        else:
            map_circles += "."
            map_circles += "."
    else:
        cycle += 1
        map_circles += "."
    
    if len(list_of_cycles) != 0:
        if cycle >= list_of_cycles[0]-2:
            result2 = cycle_value * list_of_cycles.popleft()
            result += result2

def add_to_map(cycle, map_circles, words):
    if cycle % 40 == 0:
        map_circles += "\n"
    if cycle % 40 == 1 and words[0] == "addx":
        map_circles = map_circles[:-1] + "\n" + map_circles[-1:]
    

    

print(result)
print(map_circles)
        


#part1



#submit(result, part="a", day=10, year=2022)

#part2
#submit(result, part="b", day=10, year=2022)
