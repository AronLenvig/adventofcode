from aocd import get_data, submit
import numpy as np
lines = get_data(day=6, year=2023).splitlines()

# lines = ["Time:      7  15   30",
# "Distance:  9  40  200"]

times = lines[0].split(" ")
distances = lines[1].split(" ")

times = [time for time in times if time != ""][1:]
distances = [distance for distance in distances if distance != ""][1:]

times = "".join(times)
distances = "".join(distances)
# times = [times]
# distances = [distances]
time = int(times)
distance = int(distances)

list_possible_times = []
result = 0
# for i, time in enumerate(times):
possible_times = 0
for nr in range(time):
    if nr*(time - nr) > distance:
        # print("nr",nr,"nr*(time-nr)", nr*(int(distances[i]) - nr), "distance:", int(distances[i]))
        possible_times += 1
    elif possible_times != 0:
        break

result = possible_times

# print(list_possible_times)

# result = np.prod(list_possible_times)
print(result)


#part1
# submit(result, part="a", day=6, year=2023)

#part2
submit(result, part="b", day=6, year=2023)
