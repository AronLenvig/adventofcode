from aocd import get_data, submit
lines = get_data(day=2, year=2023).splitlines()
# print(lines[0])

# lines = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green.",
# "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
# "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
# "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
# "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

def a():
    max_red = 12
    max_green = 13
    max_blue = 14

    def check_if_valid_game_round(max_red, max_green, max_blue, game_rounds):
        for game_round in game_rounds:
            round_turns = game_round.strip().split(",")
            for round_turn in round_turns:
                # print(round_turn)
                number, color = round_turn.strip().split(" ")
                if color == "red":
                    if int(number) > max_red:
                        return False
                elif color == "green":
                    if int(number) > max_green:
                        return False
                elif color == "blue":
                    if int(number) > max_blue:
                        return False
        return True

    numbers = []
    for game in lines:
        game_name, body = game.split(":")
        game_rounds = body.split(";")
        result = check_if_valid_game_round(max_red, max_green, max_blue, game_rounds)
        # print(game_name, result)
        # print(game_rounds)
        if result:
            name, nr = game_name.strip().split(" ")
            numbers.append(int(nr))

    result = sum(numbers)

    #part1
    # submit(result, part="a", day=2, year=2023)
        
def b():
    def get_highest_(game_rounds) -> tuple[int,int,int]:
        current_high_red = 0
        current_high_green = 0
        current_high_blue = 0
        for game_round in game_rounds:
            round_turns = game_round.strip().split(",")
            for round_turn in round_turns:
                # print(round_turn)
                number, color = round_turn.strip().split(" ")
                if color == "red":
                    if int(number) > current_high_red:
                        current_high_red = int(number)
                elif color == "green":
                    if int(number) > current_high_green:
                        current_high_green = int(number)
                elif color == "blue":
                    if int(number) > current_high_blue:
                        current_high_blue = int(number)
        return (current_high_red, current_high_green, current_high_blue)

    numbers = []
    for game in lines:
        game_name, body = game.split(":")
        game_rounds = body.split(";")
        max_red, max_green, max_blue = get_highest_(game_rounds)
        numbers.append(max_red * max_green * max_blue)

    result = sum(numbers)

    #part2
    # submit(result, part="b", day=2, year=2023)

# a()
# b()
    


