from aocd import get_data,submit

def part1(data: list) -> int:
    result = 0
    for line in data:
        a = line.split(",")
        a1 = list(map(int,a[0].split("-")))
        a2 = list(map(int,a[1].split("-")))
        if  a1[0] <= a2[0] and a1[1] >= a2[1]:
            result += 1
            continue
        if  a2[0] <= a1[0] and a2[1] >= a1[1]:
            print(a2,a1)
            result += 1
            continue
    return result

def part2(data: list) -> int:
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
    return result


if __name__ == "__main__":
    data = get_data(day=4, year=2022).splitlines()
    print(data[0:10])

    #print(part1(data))
    #print(part2(data))

    #submit(part1(), part="a", day=4, year=2022)
    #submit(part2(data), part="b", day=4, year=2022)
