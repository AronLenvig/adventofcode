# generate python functions for each day of advent of code

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def generate_day(day, year):
    #check if days folder exists, if not create it
    if not os.path.exists(f"{__location__}/{year}"):
        os.makedirs(f"{__location__}/{year}")
    with open(f"{__location__}/{year}/day{day:02d}.py", "w") as f:
        f.write(
f"""from aocd import get_data, submit
lines = get_data(day={day}, year={year}).splitlines()

#part1
#submit(result, part="a", day={day}, year={year})

#part2
#submit(result, part="b", day={day}, year={year})
""")

if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: python generate_days.py <day>")
    #     exit(1)
    # generate_day(sys.argv[1])
    for i in range(2, 26):
        generate_day(i,2021)
    pass