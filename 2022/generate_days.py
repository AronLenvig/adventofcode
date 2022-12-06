# generate python functions for each day of advent of code

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def generate_day(day):
    with open(f"{__location__}/days/day{day:02d}.py", "w") as f:
        f.write(
f"""from aocd import get_data, submit

def part1(data: list) -> int:
    pass

def part2(data: list) -> int:
    pass


if __name__ == "__main__":
    import time
    start = time.time()
    data = get_data(day={day}, year=2022).splitlines()
    print(data[0:10])

    #print(part1(data))
    #print(part2(data))

    #submit(part1(data), part="a", day={day}, year=2022)
    #submit(part2(data), part="b", day={day}, year=2022)


    print("Time taken:", str(time.time() - start))
""")

if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: python generate_days.py <day>")
    #     exit(1)
    # generate_day(sys.argv[1])
    #for i in range(6, 26):
    #    generate_day(i)
    pass