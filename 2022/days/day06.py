from aocd import get_data, submit

def part1(data: str) -> int:
    rep = 4
    return next(i+rep for i in range(0, len(data))if len(set(data[i:i + rep])) == rep)

def part2(data: str) -> int:
    rep = 14
    return next(i+rep for i in range(0, len(data))if len(set(data[i:i + rep])) == rep)

if __name__ == "__main__":
    import time
    data = get_data(day=6, year=2022)
    start = time.time()
    part1(data)
    part2(data)
    print("Time taken:", str(time.time() - start))

    #submit(part1(data), part="a", day=6, year=2022)
    #submit(part2(data), part="b", day=6, year=2022)

