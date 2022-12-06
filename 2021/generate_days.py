# generate python functions for each day of advent of code

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def generate_day(day):
    #check if days folder exists, if not create it
    if not os.path.exists(f"{__location__}/days"):
        os.makedirs(f"{__location__}/days")
    with open(f"{__location__}/days/day{day:02d}.py", "w") as f:
        f.write(
f"""from aocd import get_data, submit
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
    data = get_data(day={day}, year=2021).splitlines()
    start = time.time()
    part1,part2 = main(data)
    print("Time taken:", str(round((time.time() - start)*1000,4)), "milliseconds")

    #submit(part1, part="a", day={day}, year=2021)
    #submit(part2, part="b", day={day}, year=2021)
""")

if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: python generate_days.py <day>")
    #     exit(1)
    # generate_day(sys.argv[1])
    for i in range(1, 26):
        generate_day(i)
    pass