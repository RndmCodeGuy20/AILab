InitialState = [
    [2, 3, 4],
    [None, 1, 5],
    [6, 7, 8],
]

FinalState = [
    [2, 4, None],
    [1, 3, 5],
    [6, 7, 8],
]


def moveBlankUp(puzzleState):
    tempState = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    temp = 0
    for row in range(3):
        for col in range(3):
            tempState[row][col] = puzzleState[row][col]

    for row in range(3):
        for col in range(3):
            if tempState[row][col] == None and row != 0:
                temp = tempState[row - 1][col]
                tempState[row - 1][col] = tempState[row][col]
                tempState[row][col] = temp
                break

    return tempState


def moveBlankRight(puzzleState):
    tempState = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    temp = 0
    for row in range(3):
        for col in range(3):
            tempState[row][col] = puzzleState[row][col]

    for row in range(3):
        for col in range(3):
            if tempState[row][col] == None and col != 2:
                temp = tempState[row][col + 1]
                tempState[row][col + 1] = tempState[row][col]
                tempState[row][col] = temp
                break

    return tempState


def moveBlankDown(puzzleState):
    tempState = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    temp = 0
    for row in range(3):
        for col in range(3):
            tempState[row][col] = puzzleState[row][col]

    for row in range(3):
        for col in range(3):
            if tempState[row][col] == None and row != 2:
                temp = tempState[row + 1][col]
                tempState[row + 1][col] = tempState[row][col]
                tempState[row][col] = temp
                break

    return tempState


def moveBlankLeft(puzzleState):
    tempState = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    temp = 0
    for row in range(3):
        for col in range(3):
            tempState[row][col] = puzzleState[row][col]

    for row in range(3):
        for col in range(3):
            if tempState[row][col] == None and col != 0:
                temp = tempState[row][col - 1]
                tempState[row][col - 1] = tempState[row][col]
                tempState[row][col] = temp
                break

    return tempState


def main():

    global InitialState, FinalState

    frontier = []
    explored = []
    count = 0
    depth = 0

    frontier.append(InitialState)
    explored.append(InitialState)

    while len(frontier) != 0:
        InitialState = frontier.pop(0)
        print(f"\n\nDepth : {depth} ➡️ To be explored : {InitialState}\n")

        if InitialState == FinalState:
            print(f"Goal State : {InitialState} reached after searching {count} nodes.")
            break

        if moveBlankLeft(InitialState) not in explored:
            frontier.append(moveBlankLeft(InitialState))
            explored.append(moveBlankLeft(InitialState))
            count += 1
            print(f"{moveBlankLeft(InitialState)}", end="---")

        if moveBlankRight(InitialState) not in explored:
            frontier.append(moveBlankRight(InitialState))
            explored.append(moveBlankRight(InitialState))
            count += 1
            print(f"{moveBlankRight(InitialState)}", end="---")

        if moveBlankUp(InitialState) not in explored:
            frontier.append(moveBlankUp(InitialState))
            explored.append(moveBlankUp(InitialState))
            count += 1
            print(f"{moveBlankUp(InitialState)}", end="---")

        if moveBlankDown(InitialState) not in explored:
            frontier.append(moveBlankDown(InitialState))
            explored.append(moveBlankDown(InitialState))
            count += 1
            print(f"{moveBlankDown(InitialState)}", end="\n")

        depth += 1


if __name__ == "__main__":
    main()
