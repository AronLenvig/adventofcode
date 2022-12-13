from aocd import get_data, submit
data = get_data(day=13, year=2022)
from functools import cmp_to_key
# seperate the data by double new line

groups = data.split("\n\n")

#part1
def part1():
    result = 0
    for i,group in enumerate(groups , start=1):
        lines = group.splitlines()
        list1 = eval(lines[0])
        list2 = eval(lines[1])
        value = compare(list1,list2)
        if value == 1:
            result += i
    submit(result, part="a", day=13, year=2022)

def part2():
    items = []
    for group in groups:
        lines = group.splitlines()
        items.append(eval(lines[0]))
        items.append(eval(lines[1]))

    items.append([[2]])
    items.append([[6]])
    
    items = sorted(items, key=cmp_to_key(lambda item1,item2: compare(item1,item2)))[::-1]
    result = 1
    for i,p in enumerate(items,start=1):
        if p==[[2]] or p==[[6]]:
            result *= i
    submit(result, part="b", day=13, year=2022)

def compare(list1,list2):
        
    if type(list1) == int and type(list2) == int:
        if list1 < list2:
            return 1
        if list1 == list2:
            return 0
        else:
            return -1

    if type(list1) == list and type(list2) == list:
        i = 0
        while i<len(list1) and i<len(list2):
            value = compare(list1[i], list2[i])
            if value == 1:
                return 1
            if value == -1:
                return -1
            i += 1
        if i==len(list1) and i<len(list2):
            return 1
        elif i==len(list2) and i<len(list1):
            return -1
        else:
            return 0

    if type(list1) == list and type(list2) != list:
        return compare(list1,[list2])

    if type(list1) != list and type(list2) == list:
        return compare([list1],list2)
                
# part2()
# part1()
