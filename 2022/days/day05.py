from aocd import get_data, submit
from collections import deque

def parsedata(data: list):
    stacks_display = []
    instructions = []

    for i in range(data.index("")):
        stacks_display.append(data[i])
    for i in range(data.index("")+1, len(data)):
        instructions.append(data[i])
    
    stacks = {}

    for nr in stacks_display[-1].replace(" ", ""):
        stacks[nr] = deque()

    for line in stacks_display[0:-1]:
        for nr, index in enumerate(range(1,len(line),4)):
            if line[index] != " ":
                stacks[str((nr%9)+1)].appendleft(line[index])
    
    #follow instructions and move stacks around
    moves = []
    froms = []
    tos = []
    for instruction in instructions:
        list_instruction = instruction.split(" ")
        moves.append(list_instruction[1])
        froms.append(list_instruction[3])
        tos.append(list_instruction[5])
    
    return moves,froms,tos,stacks
    

def part1(data: list) -> int:
    moves,froms,tos,stacks  = parsedata(data)
    for move,from_,to in zip(moves,froms,tos):
        for _ in range(int(move)):
            stacks[to].append(stacks[from_].pop())
    
    #return the last letter of all the stacks
    result = ""
    for stack in stacks.values():
        result += stack[-1]
    return result


def part2(data: list) -> int:
    moves,froms,tos,stacks  = parsedata(data)
    for move,from_,to in zip(moves,froms,tos):
        reverse_stack = deque()
        for i in range(int(move)):
            reverse_stack.append(stacks[from_].pop())
        for i in list(reverse_stack)[::-1]:
            stacks[to].append(i)
    #return the last letter of all the stacks
    result = ""
    for stack in stacks.values():
        result += stack[-1]
    return result

if __name__ == "__main__":
    import time
    data = get_data(day=5, year=2022).splitlines()

    #timeit(part1(data))
    #timeit(part2(data))


    #print(part1(data))
    #print(part2(data))

    #submit(part1(data), part="a", day=5, year=2022)
    #submit(part2(data), part="b", day=5, year=2022)



