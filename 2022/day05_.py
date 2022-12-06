from aocd import get_data, submit
from collections import deque
data = get_data(day=5, year=2022).splitlines()

def fill_stacks(stacks_display) -> dict:
    stacks = {}
    for nr in stacks_display[-1].replace(" ", ""):
        stacks[nr] = deque()
    for line in stacks_display[0:-1]:
        for nr, index in enumerate(range(1,len(line),4)):
            if line[index] != " ":
                stacks[str((nr%9)+1)].appendleft(line[index])
    return stacks

def get_instructions() -> tuple:
    instructions = [data[i].split(" ") for i in range(data.index("")+1, len(data))]
    return zip(*[(instruction[1], instruction[3], instruction[5]) for instruction in instructions])

stacks_display = []
instructions = []
for i in range(data.index("")):
    stacks_display.append(data[i])

#part1
stacks = fill_stacks(stacks_display)
for move,from_,to in zip(*get_instructions()):
    for _ in range(int(move)):
        stacks[to].append(stacks[from_].pop())

result = "".join([stack[-1] for stack in stacks.values()])
submit(result, part="a", day=5, year=2022)

#part2
stacks = fill_stacks(stacks_display)
for move,from_,to in zip(*get_instructions()):
    reverse_stack = deque()
    for _ in range(int(move)):
        reverse_stack.append(stacks[from_].pop())
    for i in list(reverse_stack)[::-1]:
        stacks[to].append(i)

result = "".join([stack[-1] for stack in stacks.values()])
submit(result, part="b", day=5, year=2022)
