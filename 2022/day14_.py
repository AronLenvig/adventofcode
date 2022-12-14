from aocd import get_data, submit
commands = get_data(day=14, year=2022).splitlines()

def create_cords(commands):
    
    display_map = set()
    for command in commands:
        cords = command.split(" -> ")
        last_x = 0
        last_y = 0
        for cord in cords:
            x, y = cord.split(",")
            x = int(x)
            y = int(y)

            if last_x == 0 and last_y == 0:
                pass
            else:
                if x < last_x:
                    for i in range(x, last_x+1):
                        display_map.add((i,y))
                elif x > last_x:
                    for i in range(last_x, x+1):
                        display_map.add((i,y))
                elif y < last_y:
                    for i in range(y, last_y+1):
                        display_map.add((x,i))
                elif y > last_y:
                    for i in range(last_y, y+1):
                        display_map.add((x,i))
            last_x = int(x)
            last_y = int(y)
        
    return display_map

def display_lengths(display_cords):
    x_items = []
    y_items = []
    for items in display_cords:
        x_items.append(items[0])
        y_items.append(items[1])

    min_x = min(x_items)
    min_y = 0
    max_x = max(x_items)
    max_y = max(y_items)
    return min_x, min_y, max_x, max_y


def display(display_cords, sand_cords):
    min_x, min_y, max_x, max_y = display_lengths(display_cords)

    for y in range(min_y, max_y+4):
        for x in range(min_x, max_x+1):
            if (500,0) == (x,y):
                print("+", end="")
            elif (x,y) in display_cords:
                print("#", end="")
            elif (x,y) in sand_cords:
                print("o", end="")
            else:
                print(".", end="")
        print()


def part1():
    sand_cords = set()
    display_cords = create_cords(commands)
    result = -1
    min_x, min_y, max_x, max_y = display_lengths(display_cords)
    end_loop = False
    while True:
        result += 1
        x,y = (500,0)
        while True:
            if min_x > x > max_x or y > max_y:
                end_loop = True
                break
            if (x,y+1) not in display_cords and (x,y+1) not in sand_cords:
                y += 1
            elif (x-1,y+1) not in display_cords and (x-1,y+1) not in sand_cords: # move down left
                x -= 1
                y += 1
            elif (x+1,y+1) not in display_cords and (x+1,y+1) not in sand_cords: # move down right
                x += 1
                y += 1
            else:
                sand_cords.add((x,y))
                break
        if end_loop:
            break
    display(display_cords,sand_cords)
    print(result)
    submit(result, part="a", day=14, year=2022)

#part2
def part2():
    sand_cords = set()
    display_cords = create_cords(commands)
    min_x, min_y, max_x, max_y = display_lengths(display_cords)
    result = 0
    end_loop = False
    while True:
        result += 1
        x,y = (500,0)
        while True:
            if y == max_y+1:
                sand_cords.add((x,y))
                break
            if (x,y+1) not in display_cords and (x,y+1) not in sand_cords:
                y += 1
            elif (x-1,y+1) not in display_cords and (x-1,y+1) not in sand_cords: # move down left
                x -= 1
                y += 1
            elif (x+1,y+1) not in display_cords and (x+1,y+1) not in sand_cords: # move down right
                x += 1
                y += 1
            else:
                if (x,y) == (500,0):
                    end_loop = True
                sand_cords.add((x,y))
                break
        if end_loop:
            break
    display(display_cords,sand_cords)
    print(result)
    submit(result, part="b", day=14, year=2022)

part2()