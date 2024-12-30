from pprint import pprint
from aocd import get_data, submit
# data = get_data(day=16, year=2022).splitlines()

data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()



pipes = {}

#part1
# eksample code to parse "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB" should equal {"AA": {"paths": ["DD", "II", "BB"]}, {"rate": 0}}
for line in data:
    words = line.split()

    paths = words[9:]
    #remove the last comma from does item that have comma in it from paths
    for i in range(len(paths)):
        if paths[i][-1] == ",":
            paths[i] = paths[i][:-1]
    
    pipes[words[1]] = {"paths": paths, "rate": int(words[4][5:-1]), "used": False}

current_place = "AA"
pprint(pipes)



def get_all_path_lenght(current_place : str) -> dict:
    
    list_of_pipe_checked = {current_place : 0} 
    loop_paths = pipes[current_place]["paths"]
    lenght = 1
    while True:
        next_loop_paths = []
        for path in loop_paths:
            list_of_pipe_checked[path] = lenght
            paths = pipes[path]["paths"]
            valid_paths = [path for path in paths if path not in list_of_pipe_checked.keys()]
            next_loop_paths.extend(valid_paths)

        if next_loop_paths == []:
            break

        lenght += 1
        loop_paths = next_loop_paths
    return list_of_pipe_checked



        
    

    
    
   
minutes = 30
points = 0
while True:
    # start in pipes["AA"] check all the pipes paths every move cost 1 minutes and used = True rate = 0, open a rate cost 1 minutes
    # you only have 30 minutes you need to open as many valves as possible

    # Action
    # check the best path here:
    
    best_path = 0
    best_path_name = ""
    best_time_to_open = 0

    path_all_lenght = get_all_path_lenght(current_place)
    for path in path_all_lenght.keys():
        if pipes[path]["used"]:
            continue
        time_to_open = path_all_lenght[path] + 1

        if minutes - time_to_open < 0:
            continue
        
        path_takes = (pipes[path]["rate"] * (minutes-time_to_open)) / time_to_open

        if path_takes > best_path:
            best_path = path_takes
            best_path_name = path
            best_time_to_open = time_to_open


    if best_path_name == "":
        break
    pipes[best_path_name]["used"] = True
    minutes -= best_time_to_open
    points += pipes[best_path_name]["rate"] * (minutes-best_time_to_open)
    print(best_time_to_open)
    print(best_path_name)
    current_place = best_path_name

    if minutes == 0:
        break
    
print(points)
        



#submit(result, part="a", day=16, year=2022)

#part2
#submit(result, part="b", day=16, year=2022)
