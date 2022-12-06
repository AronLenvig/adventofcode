from aocd import get_data, submit
import time

def add_numbers(data: list[str]) -> list[int]:
    list_of_added_numbers = []
    total=0
    for nr in data:
        if nr == "":
            list_of_added_numbers.append(total)
            total=0
        else:
            total += int(nr)
    return list_of_added_numbers

def part1(data: list[str]) -> int:
    list_of_added_numbers = add_numbers(data)
    return max(list_of_added_numbers)

def part2(data: list[str]) -> int:
    list_of_added_numbers = add_numbers(data)
    list_of_added_numbers.sort(reverse=True)
    result = list_of_added_numbers[0] + list_of_added_numbers[1] + list_of_added_numbers[2]
    return result

def main(data : list[str]) -> tuple[int, int]:
    #print(data[0:10])

    #print(part1(data))
    # print(part2(data))

    #return 0,0
    return part1(data), part2(data)

if __name__ == "__main__":
    data = get_data(day=1, year=2022).splitlines()
    start = time.time()
    part1_,part2_ = main(data)
    print("Time taken:", str(round((time.time() - start)*1000,4)), "milliseconds")

    if part1_:
        submit(part1_, part="a", day=1, year=2022)
    if part2_:
        submit(part2_, part="b", day=1, year=2022)
