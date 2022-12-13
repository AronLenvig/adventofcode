from pprint import pprint
from aocd import get_data, submit
lines = get_data(day=12, year=2022).splitlines()

#part1
from collections import deque

graph = []
for line in lines:
    graph.append(line)
row_lenght = len(graph)
column_lenght = len(graph[0])

# convert graph to numbers (1-26)
graph_numbers = [[0 for _ in range(column_lenght)] for _ in range(row_lenght)]
for r in range(row_lenght):
    for c in range(column_lenght):
        if graph[r][c]=='S':
            graph_numbers[r][c] = 1
        elif graph[r][c] == 'E':
            graph_numbers[r][c] = 26
        else:
            graph_numbers[r][c] = ord(graph[r][c])-ord('a')+1


def part1():
    cordinations = deque()
    for r in range(row_lenght):
        for c in range(column_lenght):
            if graph[r][c]=='S':
                cordinations.append(((r,c), 0))
    result = get_end_result(cordinations)
    submit(result, part="a", day=12, year=2022)

def part2():
    cordinations = deque()
    for r in range(row_lenght):
        for c in range(column_lenght):
            if graph_numbers[r][c] == 1: 
                cordinations.append(((r,c), 0))
    result = get_end_result(cordinations)
    submit(result, part="b", day=12, year=2022)

def get_end_result(cordinations : list):
    tried_cordinations = set()
    while cordinations:
        (r,c),d = cordinations.popleft()
        if (r,c) in tried_cordinations:
            continue
        tried_cordinations.add((r,c))
        if graph[r][c]=='E':
            return d
        for r_direction,c_direction in [(-1,0),(0,1),(1,0),(0,-1)]:
            r_new_direction = r + r_direction
            c_new_direction = c + c_direction
            if 0<=r_new_direction<row_lenght and 0<=c_new_direction<column_lenght and graph_numbers[r_new_direction][c_new_direction]<=1+graph_numbers[r][c]:
                cordinations.append(((r_new_direction,c_new_direction),d+1))

part1()
part2()