from aocd import get_data, submit

def add_numbers(data: list) -> int:
    list_of_added_numbers = []
    total=0
    for i in data:
        if i == "":
            list_of_added_numbers.append(total)
            total=0
        else:
            total += int(i)
    return list_of_added_numbers

def part1(data: list) -> int:
    list_of_added_numbers = add_numbers(data)
    return max(list_of_added_numbers())

# part 2
def part2(data: list) -> int:
    list_of_added_numbers = add_numbers(data)
    list_of_added_numbers.sort(reverse=True)
    result = list_of_added_numbers[0] + list_of_added_numbers[1] + list_of_added_numbers[2]
    return result

if __name__ == "__main__":
    import time
    start = time.time()
    data = get_data(day=1, year=2022).splitlines()

    print(part1(data))
    print(part2(data))

    print("Time taken:", str(time.time() - start))
    #submit(part1(data), part="a", day=1, year=2022)
    #submit(part2(data), part="b", day=1, year=2022)

