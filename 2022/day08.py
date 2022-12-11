from aocd import get_data, submit
data = get_data(day=8, year=2022).splitlines()

columns = data
rows = [list(x) for x in zip(*columns)]

#map columns to int 
columns = [[int(x) for x in column] for column in columns]
rows = [[int(x) for x in row] for row in rows]



#part1
def part1():
    
    visible_trees_index = set()
    print(columns[0][1])

    # find all visable trees to the left view and record there position
    
    for r_index, row in enumerate(columns):

        highest_tree = -1
        for c_index, tree in enumerate(row):
            if tree > highest_tree:
                highest_tree = tree
                visible_trees_index.add((r_index, c_index))

        highest_tree = -1
        for c_index, tree in reversed(list(enumerate(row))):
            if tree > highest_tree:
                highest_tree = tree
                visible_trees_index.add((r_index,  c_index))
    
    for c_index, column in enumerate(rows):
        highest_tree = -1
        for r_index, tree in enumerate(column):
            if tree > highest_tree:
                highest_tree = tree
                visible_trees_index.add((r_index, c_index))

        highest_tree = -1
        for r_index, tree in reversed(list(enumerate(column))):
            if tree > highest_tree:
                highest_tree = tree
                visible_trees_index.add((r_index, c_index))

    submit(len(visible_trees_index), part="a", day=8, year=2022)

#part2
def part2():
    # find the three that has the best view of the forest in a grid where 0 is shortest three and 9 is the tallest
    result = 0

    # Iterate over the columns and rows of the grid
    for r_index, line in enumerate(columns[1:-1], start=1):
        for c_index, tree in enumerate(line[1:-1], start=1):
            if tree < 5:
                continue
            # Check the view in each direction
            down = next((i for i, x in enumerate(rows[c_index][r_index+1:], start=1) if x >= tree), len(rows[c_index][r_index+1:]))
            up = next((i for i, x in enumerate(rows[c_index][r_index-1::-1], start=1) if x >= tree), len(rows[c_index][r_index-1::-1]))
            right = next((i for i, x in enumerate(columns[r_index][c_index+1:], start=1) if x >= tree), len(columns[r_index][c_index+1:]))
            left = next((i for i, x in enumerate(columns[r_index][c_index-1::-1], start=1) if x >= tree), len(columns[r_index][c_index-1::-1]))

            # Update the best view if necessary
            result = max(result, right * left * down * up)

    print(result)
    submit(result, part="b", day=8, year=2022)

part2()

