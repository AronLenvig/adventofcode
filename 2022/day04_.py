from aocd import get_data,submit
import time

def part1(data: list[str]) -> int:
    result = 0
    for line in data:
        a = line.split(",")
        a1 = list(map(int,a[0].split("-")))
        a2 = list(map(int,a[1].split("-")))
        if  a1[0] <= a2[0] and a1[1] >= a2[1]:
            result += 1
            continue
        if  a2[0] <= a1[0] and a2[1] >= a1[1]:
            result += 1
            continue
    return result

def part2(data: list[str]) -> int:
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


def main(data):
    # print(data[0:10])

    print(part1(data))
    print(part2(data))

    return 0,0
    return part1(data), part2(data)

if __name__ == "__main__":
    data = get_data(day=4, year=2022).splitlines()
    start = time.time()
    part1_,part2_ = main(data)
    print("Time taken:", str(round((time.time() - start)*1000,4)), "milliseconds")

    if part1_:
        submit(part1_, part="a", day=4, year=2022)
    if part2_:
        submit(part2_, part="b", day=4, year=2022)
