from aocd import get_data, submit
import time

def part1(data: list) -> int:
    return 11

def part2(data: list) -> int:
    pass

def main(data):
    print(data[0:10])

    #print(part1(data))
    #print(part2(data))

    return 0,0
    return part1(data), part2(data)

if __name__ == "__main__":
    data = get_data(day=7, year=2021).splitlines()
    start = time.time()
    part1,part2 = main(data)
    print("Time taken:", str(round((time.time() - start)*1000,4)), "milliseconds")

    #submit(part1, part="a", day=7, year=2021)
    #submit(part2, part="b", day=7, year=2021)
