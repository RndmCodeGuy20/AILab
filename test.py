## ----------------------------- 8 Puzzle Problem ---------------------------------
##                                                               Date: 27-Mar-2022
##
## Write a program to solve 8 puzzle problem for the given initial and final states
## using Breadth First Search (BFS).
##
##                     Initial State:          Final State:
##                      2    3    4            2    4    -
##                      -    1    5            1    3    5
##                      6    7    8            6    7    8
##
## Create child and store them in frontier and update explored.
##
## ---------------------------------------------------------------------------------

# import queue
# from types import NoneType

initial = [
    ["2", "3", "4"],
    ["1", None, "5"],
    ["6", "7", "8"],
]

final = [
    ["2", "4", None],
    ["1", "3", "5"],
    ["6", "7", "8"],
]


def move_left(initial):

    temp_state = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"],
    ]

    temp = 0

    for i in range(3):
        for j in range(3):
            temp_state[i][j] = initial[i][j]

    for i in range(0, 3):
        for j in range(0, 3):
            if temp_state[i][j] == None and j != 0:
                temp = temp_state[i][j - 1]
                temp_state[i][j - 1] = temp_state[i][j]
                temp_state[i][j] = temp
                break

    return temp_state


# print(move_left(initial), end="\n")


def move_right(initial):

    temp_state = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"],
    ]

    temp = 0

    for i in range(3):
        for j in range(3):
            temp_state[i][j] = initial[i][j]

    for i in range(0, 3):
        for j in range(0, 3):
            if temp_state[i][j] == None and j != 2:
                temp = temp_state[i][j + 1]
                temp_state[i][j + 1] = temp_state[i][j]
                temp_state[i][j] = temp
                break

    return temp_state


# print(move_right(initial))


def move_up(initial):

    temp_state = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"],
    ]

    temp = 0

    for i in range(3):
        for j in range(3):
            temp_state[i][j] = initial[i][j]

    for i in range(0, 2):
        for j in range(0, 2):
            if temp_state[i][j] == None and i != 0:
                temp = temp_state[i - 1][j]
                temp_state[i - 1][j] = temp_state[i][j]
                temp_state[i][j] = temp
                break

    return temp_state


# print(move_up(initial))


def move_down(initial):

    temp_state = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"],
    ]

    temp = 0

    for i in range(3):
        for j in range(3):
            temp_state[i][j] = initial[i][j]

    for i in range(0, 2):
        for j in range(0, 2):
            if initial[i][j] == None and i != 2:
                temp = temp_state[i + 1][j]
                temp_state[i + 1][j] = temp_state[i][j]
                temp_state[i][j] = temp
                break

    return temp_state


# print(move_down(initial))

count = 0
queue = []
queue.append(initial)

while len(queue) != 0:
    initial = queue.pop(0)

    if initial == final:
        print(f"Final State Reached! {count} nodes explored!\n")
        print(initial)
        break

    queue.append(move_up(initial))
    count += 1
    queue.append(move_right(initial))
    count += 1
    queue.append(move_left(initial))
    count += 1
    queue.append(move_down(initial))
    count += 1
