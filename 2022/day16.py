from aocd import get_data, submit
import time

def part1(data: list[str]) -> int:
    return 11

def part2(data: list[str]) -> int:
    pass

def main(data):
    print(data[0:10])

    #print(part1(data))
    #print(part2(data))

    return 0,0
    return part1(data), part2(data)

if __name__ == "__main__":
    data = get_data(day=16, year=2022).splitlines()
    start = time.time()
    part1_,part2_ = main(data)
    print("Time taken:", str(round((time.time() - start)*1000,4)), "milliseconds")

    if part1_:
        submit(part1_, part="a", day=16, year=2022)
    if part2_:
        submit(part2_, part="b", day=16, year=2022)
