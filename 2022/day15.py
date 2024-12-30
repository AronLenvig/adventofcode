from itertools import product
from aocd import get_data, submit
data = get_data(day=15, year=2022).splitlines()
data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()

#parse data to get sensor cords and becon cords
def parse_data(data : list) -> tuple:
    sensor_cords = []
    becon_cords = []
    for line in data:
        # line eksample: 'Sensor at x=3844106, y=3888618: closest beacon is at x=3225436, y=4052707'
        seperate = line.split(":")
        sensor_cords.append((seperate[0].split(" ")[2].split("=")[1][:-1], seperate[0].split(" ")[3].split("=")[1]))
        becon_cords.append((seperate[1].split(" ")[5].split("=")[1][:-1], seperate[1].split(" ")[6].split("=")[1]))
    
    #convert cords to int
    sensor_cords = [(int(x), int(y)) for x,y in sensor_cords]
    becon_cords = [(int(x), int(y)) for x,y in becon_cords]
    return sensor_cords, becon_cords



def get_manhattan_distance(sensor_cords : tuple, becon_cords : tuple) -> int:
    return abs(int(sensor_cords[0]) - int(becon_cords[0])) + abs(int(sensor_cords[1]) - int(becon_cords[1]))


def create_signals_of_sonsors_to_becons_single_line(sensor_cord : tuple[int,int], becon_cord : tuple[int, int], y_cord : int) -> list[tuple[int, int]]:
    distance = get_manhattan_distance(sensor_cord, becon_cord)
    s_x, s_y = sensor_cord
    signal_cords = []
    distance_to_y_coord = abs(s_y - y_cord)
    # print(distance_to_y_coord)

    loop_lenght = distance - distance_to_y_coord
    # print(loop_lenght)

    if loop_lenght > 1:
        signal_cords.append((s_x, y_cord))
        for i in range(1,loop_lenght+1):
            #add x cords to signal cords list using the distance to y cord
            signal_cords.append((s_x + i, y_cord))
            signal_cords.append((s_x - i, y_cord))

    return signal_cords

def create_signals_of_sonsors_to_beacons(sensor_cord : tuple[int,int], becon_cord : tuple[int, int]) -> list[tuple[int, int]]:
    distance = get_manhattan_distance(sensor_cord, becon_cord)
    s_x, s_y = sensor_cord
    
    signal_cords = [(s_x + i, s_y + j) for i in range(-distance, distance+1)
                                        for j in range(-distance, distance+1)
                                        if abs(i) + abs(j) <= distance]
    
    return signal_cords

def get_all_border_cords_of_sensors_to_beacons(sensor_cord : tuple[int,int], becon_cord : tuple[int, int]) -> list[tuple[int, int]]:
    distance = get_manhattan_distance(sensor_cord, becon_cord)
    s_x, s_y = sensor_cord
    signal_cords = []
    for i in range(1, (distance+1)):
        
    return signal_cords

def find_missing_value_from_sonsors_to_becons(
sensor_cords : list[tuple[int,int]], beacon_cords : list[tuple[int, int]]) -> tuple[int, int]:
    max_x = max(sensor_cords, key=lambda x: x[0])[0]
    min_x = min(sensor_cords, key=lambda x: x[0])[0]
    max_y = max(sensor_cords, key=lambda x: x[1])[1]
    min_y = min(sensor_cords, key=lambda x: x[1])[1]
    for sensor_cord, becon_cord in zip(sensor_cords, beacon_cords):
        # get all outer cords of sensor to becon
        signal_cords = 

        get_manhattan_distance(sensor_cord, becon_cord)
        for sensor_cord, becon_cord in zip(sensor_cords, beacon_cords):
            if get_manhattan_distance(sensor_cord, becon_cord) >= get_manhattan_distance(sensor_cord, becon_cord):
                inside = True
                break
        if not inside:
            return (x,y)
    return None
    





    






def display(sensor_cords, becon_cords, signal_cords):
    #find the max and min x and y
    max_x = max(sensor_cords, key=lambda x: x[0])[0]
    min_x = min(sensor_cords, key=lambda x: x[0])[0]
    max_y = max(sensor_cords, key=lambda x: x[1])[1]
    min_y = min(sensor_cords, key=lambda x: x[1])[1]
    
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x,y) in sensor_cords:
                print("S", end="")
            elif (x,y) in becon_cords:
                print("B", end="")
            elif (x,y) in signal_cords:
                print("#", end="")
            else:
                print(".", end="")
        print()
    # print(signal_cords)

def part1():
    sensor_cords, becon_cords = parse_data(data)
    signal_cords = set()
    y_cord = 11
    for i in range(len(sensor_cords)):
        signal_cords.update(create_signals_of_sonsors_to_becons_single_line(sensor_cords[i], becon_cords[i], y_cord))
    result = len(signal_cords)-1
    display(sensor_cords, becon_cords, signal_cords)
    print(result)

def part2():
    sensor_cords, becon_cords = parse_data(data)
    print(find_missing_value_from_sonsors_to_becons(sensor_cords, becon_cords))
            
part2()
#submit(result, part="a", day=15, year=2022)

#part2
#submit(result, part="b", day=15, year=2022)
