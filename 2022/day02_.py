from aocd import get_data, submit
data = get_data(day=2, year=2022).splitlines()

win = 6
draw = 3
lose = 0

x = 1 #rock
y = 2 #paper
z = 3 #scissors

#part1
outcomes = {
    'A X': draw+x, 'A Y': win+y, 'A Z': lose+z,
    'B X': lose+x, 'B Y': draw+y, 'B Z': win+z,
    'C X': win+x, 'C Y': lose+y, 'C Z': draw+z
    }
result = sum([outcomes[line] for line in data])
submit(result, part="a", day=2, year=2022)

#part2
outcomes = {
    'A X': lose+z, 'A Y': draw+x, 'A Z': win+y,
    'B X': lose+x, 'B Y': draw+y, 'B Z': win+z,
    'C X': lose+y, 'C Y': draw+z, 'C Z': win+x
}
result = sum([outcomes[line] for line in data])
submit(result, part="b", day=2, year=2022)
