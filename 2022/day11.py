from math import floor
from aocd import get_data, submit
from pprint import pprint
from collections import deque
data = get_data(day=11, year=2022).splitlines()

split_data = [list(data[i:i+6]) for i in range(0,len(data),7)]


def create_operation(operation):
    values = operation.split(" ")
    if values[0] == "+":
        return lambda x: x + int(values[1])
    if values[0] == "*":
        if values[1] == "old":
            return lambda x: x * x
        return lambda x: x * int(values[1])

defualt_test = []
def create_monkeys_dict():
    monkeys = {}
    for monkey_data in split_data:
        monkeys[monkey_data[0]] = {}
        monkey=monkeys[monkey_data[0]]
        monkey["starting_items"] = deque(map(int,monkey_data[1].split(":")[1].split(",")))
        monkey["operation"] = create_operation(monkey_data[2].split(":")[1].split("=")[1].strip()[4:])
        monkey["test"] = int(monkey_data[3].split(":")[1].split(" ")[3])
        defualt_test.append(int(monkey_data[3].split(":")[1].split(" ")[3]))
        monkey["if_true"] = "Monkey " + monkey_data[4].split(":")[1].split(" ")[4] + ":"
        monkey["if_false"] = "Monkey " +monkey_data[5].split(":")[1].split(" ")[4] + ":"
        monkey["nr_of_inspections"] = 0
    return monkeys

monkeys = create_monkeys_dict()
print(defualt_test)
lcm = 1
for x in defualt_test:
    lcm = (lcm*x)

def part1():
    for _ in range(20):
        for monkey in monkeys.keys():
            while monkeys[monkey]["starting_items"]:
                item = monkeys[monkey]["starting_items"].popleft()
                monkeys[monkey]["nr_of_inspections"] += 1
                worry_level = monkeys[monkey]["operation"](item)
                boredom = floor(worry_level/3)
                if boredom % monkeys[monkey]["test"] == 0:
                    monkeys[monkeys[monkey]["if_true"]]["starting_items"].append(boredom)
                else:
                    monkeys[monkeys[monkey]["if_false"]]["starting_items"].append(boredom)

    #the two monkeys that have the most nr_of_inspections are the ones that are the most important multiply them together and submit
    list_of_inspections = [monkeys[monkey]["nr_of_inspections"] for monkey in monkeys.keys()]
    list_of_inspections.sort(reverse=True)
    result = list_of_inspections[0] * list_of_inspections[1]
    pprint(monkeys)
    print(result)
    #submit(result, part="a", day=11, year=2022)

#part2
def part2():
    for _ in range(10000):
        for monkey in monkeys.keys():
            while monkeys[monkey]["starting_items"]:
                item = monkeys[monkey]["starting_items"].popleft()
                monkeys[monkey]["nr_of_inspections"] += 1
                worry_level = monkeys[monkey]["operation"](item)
                worry_level %= lcm
                if worry_level % monkeys[monkey]["test"] == 0:
                    monkeys[monkeys[monkey]["if_true"]]["starting_items"].append(worry_level)
                else:
                    monkeys[monkeys[monkey]["if_false"]]["starting_items"].append(worry_level)

    #the two monkeys that have the most nr_of_inspections are the ones that are the most important multiply them together and submit
    list_of_inspections = [monkeys[monkey]["nr_of_inspections"] for monkey in monkeys.keys()]
    list_of_inspections.sort(reverse=True)
    result = list_of_inspections[0] * list_of_inspections[1]
    print(result)
    submit(result, part="b", day=11, year=2022)



part2()
