from aocd import get_data, submit
lines = get_data(day=9, year=2022).splitlines()
from collections import defaultdict

def adjust(head, tail):
    # Calculate the row and column differences between the head and tail
    row_difference = (head[0] - tail[0])
    col_difference = (head[1] - tail[1])

    # Move the tail closer to the head in the row and column direction
    # until it is within one row and one column of the head
    while abs(row_difference) > 1 or abs(col_difference) > 1:
        tail = (
            head[0] - 1 if tail[0] < head[0] else head[0] + 1, 
            head[1] - 1 if tail[1] < head[1] else head[1] + 1
        )
        row_difference = (head[0] - tail[0])
        col_difference = (head[1] - tail[1])

    # Return the new position of the tail
    return tail


def main():
    # Set the initial position of the head and tail
    head = (0, 0)
    tail = [(0, 0) for _ in range(9)]

    # Set the directions that the head and tail will move in
    ROW_DIRECTION = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
    COL_DIRECTION = {'L': -1, 'U': 0, 'R': 1, 'D': 0}

    # Initialize sets to keep track of the points visited by the head and tail
    points_1 = set([tail[0]])
    points_2 = set([tail[8]])

    # Iterate over the list of instructions
    for line in lines:
        # Split each instruction into the direction and the number of steps to move
        direction, amount = line.split()
        amount = int(amount)

        # Move the head and tail the specified number of steps in the specified direction
        for _ in range(amount):
            head = (head[0] + ROW_DIRECTION[direction], head[1] + COL_DIRECTION[direction])
            tail[0] = adjust(head, tail[0])
            for i in range(1, 9):
                tail[i] = adjust(tail[i-1], tail[i])
            points_1.add(tail[0])
            points_2.add(tail[8])

    # Print the number of unique points visited by the head and tail
    print(len(points_1))
    print(len(points_2))    


if __name__ == "__main__":
    main()


