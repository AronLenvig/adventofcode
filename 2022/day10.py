from aocd import get_data, submit
data = get_data(day=10, year=2022).splitlines()

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
        


#part1



#submit(result, part="a", day=10, year=2022)

#part2
#submit(result, part="b", day=10, year=2022)
