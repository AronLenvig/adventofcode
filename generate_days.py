# generate python functions for each day of advent of code

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def generate_day(day,year):
    #check if days folder exists, if not create it
    if not os.path.exists(f"{__location__}/{year}"):
        os.makedirs(f"{__location__}/{year}")
    with open(f"{__location__}/{year}/day{day:02d}.py", "w") as f:
        f.write(
f"""from aocd import get_data, submit
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
    data = get_data(day={day}, year={year}).splitlines()
    start = time.time()
    part1_,part2_ = main(data)
    print("Time taken:", str(round((time.time() - start)*1000,4)), "milliseconds")

    if part1_:
        submit(part1_, part="a", day={day}, year={year})
    if part2_:
        submit(part2_, part="b", day={day}, year={year})
""")

if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: python generate_days.py <day>")
    #     exit(1)
    # generate_day(sys.argv[1])
    for i in range(1, 26):
        generate_day(i,2021)
    pass