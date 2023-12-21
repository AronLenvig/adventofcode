from aocd import get_data, submit
lines = get_data(day=5, year=2023).splitlines()
from pprint import pprint
import time
# from functools import lru_cache
# pprint(lines[0:5])

# lines = ["seeds: 79 14 55 13",
# "",
# "seed-to-soil map:",
# "50 98 2",
# "52 50 48",
# "",
# "soil-to-fertilizer map:",
# "0 15 37",
# "37 52 2",
# "39 0 15",
# "",
# "fertilizer-to-water map:",
# "49 53 8",
# "0 11 42",
# "42 0 7",
# "57 7 4",
# "",
# "water-to-light map:",
# "88 18 7",
# "18 25 70",
# "",
# "light-to-temperature map:",
# "45 77 23",
# "81 45 19",
# "68 64 13",
# "",
# "temperature-to-humidity map:",
# "0 69 1",
# "1 0 69"
# "",
# "humidity-to-location map:",
# "60 56 37",
# "56 93 4",
# ]


# seeds.sort()

# print(seeds[1:])
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []

all_maps = [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map]

add_to = seed_to_soil_map

print("mapping")
for line in lines[2:]:
    line = line.strip()
    if not line.endswith(":"):
        pass
    elif line == "seed-to-soil map:":
        add_to = seed_to_soil_map
        continue
    elif line == "soil-to-fertilizer map:":
        add_to = soil_to_fertilizer_map
        continue
    elif line == "fertilizer-to-water map:":
        add_to = fertilizer_to_water_map
        continue
    elif line == "water-to-light map:":
        add_to = water_to_light_map
        continue
    elif line == "light-to-temperature map:":
        add_to = light_to_temperature_map
        continue
    elif line == "temperature-to-humidity map:":
        add_to = temperature_to_humidity_map
        continue
    elif line == "humidity-to-location map:":
        add_to = humidity_to_location_map
        continue

    if line == "":
        continue

    line = line.split(" ")
    if len(line) != 3:
        raise
    
    _add_to = {}
    _add_to["target"] = int(line[0])
    _add_to["source"] = int(line[1])
    _add_to["steps"] =  int(line[2])

    add_to.append(_add_to)

def convertion(seed: int, convert_map: list[dict[str, int]]) -> int:
    for convert in convert_map:
        if convert["source"] > seed or convert["source"] + convert["steps"] < seed:
            continue
        return seed - convert["source"] + convert["target"]
    return seed

def convert_range(start_seed, end_seed, maps):
    # Initialize the current range as a list of seeds
    current_seeds = list(range(start_seed, end_seed))

    for convert_map in maps:
        new_seeds = []

        for seed in current_seeds:
            converted = seed
            for convert in convert_map:
                if convert["source"] <= seed < convert["source"] + convert["steps"]:
                    converted = seed - convert["source"] + convert["target"]
                    break
            new_seeds.append(converted)

        # Update the current seeds for the next map
        current_seeds = new_seeds

    # Find the minimum value in the transformed seeds
    min_value = min(current_seeds)
    return min_value

start_time = time.time()

init_seeds = lines[0].split(" ")[1:]
min_final_seed = float('inf')

for i in range(0, len(init_seeds), 2):
    start_seed = int(init_seeds[i])
    print("start_seed", start_seed, "range", int(init_seeds[i + 1]))

    end_seed = start_seed + int(init_seeds[i + 1])

    # Convert the entire range
    converted_seed = convert_range(start_seed, end_seed, all_maps)

    # Update the minimum value
    min_final_seed = min(min_final_seed, converted_seed)

result = min_final_seed
end_time = time.time()

print(result, end_time - start_time)


#part1
# submit(result, part="a", day=5, year=2023)

#part2
# submit(result, part="b", day=5, year=2023)
