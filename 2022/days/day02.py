from aocd import get_data,submit

def part1(data: list) -> int:
    """rock paper scissors game where player 1 inputs A,B,C and player 2 inputs X,Y,Z, and the winner gets 6 points, the loser gets 0 points, and a draw gets 3 points
    #make a dict of the possible outcomes player 1 A, B, C and player 2 X, Y, Z and the points they get for winning, losing, or drawing"""
    win = 6
    draw = 3
    lose = 0

    x = 1 #rock
    y = 2 #paper
    z = 3 #scissors

    outcomes = {
        'A X': draw+x, 'A Y': win+y, 'A Z': lose+z,
        'B X': lose+x, 'B Y': draw+y, 'B Z': win+z,
        'C X': win+x, 'C Y': lose+y, 'C Z': draw+z
    }
    return sum([outcomes[line] for line in data])

def part2(data: list) -> int:
    """rock paper scissors game where player 1 inputs A,B,C and player 2 inputs X,Y,Z, and the winner gets 6 points, the loser gets 0 points, and a draw gets 3 points
    make a dict of the possible outcomes player 1 A, B, C and  X means player 2 loses, Y means player 2 draws, Z means player 2 wins count the result for each line and add it to the total"""
    win = 6
    draw = 3
    lose = 0

    x = 1 #rock
    y = 2 #paper
    z = 3 #scissors

    outcomes = {
        'A X': lose+z, 'A Y': draw+x, 'A Z': win+y,
        'B X': lose+x, 'B Y': draw+y, 'B Z': win+z,
        'C X': lose+y, 'C Y': draw+z, 'C Z': win+x
    }
    return sum([outcomes[line] for line in data])

if __name__ == "__main__":
    data = get_data(day=2, year=2022).splitlines()

    print(part1(data))
    print(part2(data))

    #submit(part1(data), part="a", day=2, year=2022)
    #submit(part2(data), part="b", day=2, year=2022)
