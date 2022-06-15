import Eight_Puzzle_Problem as puzzle8

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


def H1_MisplacedTiles(tempState: list) -> int:
    count = 0
    for i in range(3):
        for j in range(3):
            if tempState[i][j] != FinalState[i][j]:
                count += 1

    return count


indexFinalDict = {
    2: [0, 0],
    4: [0, 1],
    None: [0, 2],
    1: [1, 0],
    3: [1, 1],
    5: [1, 2],
    6: [2, 0],
    7: [2, 1],
    8: [2, 2],
}


def H2_ManhattanDistance(tempState: list) -> int:
    ManhattanDist = 0
    for key in indexFinalDict:
        for row in range(3):
            for col in range(3):
                if tempState[row][col] == key and indexFinalDict[key] != [row, col]:
                    ManhattanDist += abs(indexFinalDict[key][0] - row) + abs(
                        indexFinalDict[key][1] - col
                    )

    return ManhattanDist


def main():
    global InitialState, FinalState
    frontier = []
    explored = []
    count = 0

    frontier.append(
        [
            InitialState,
            H1_MisplacedTiles(InitialState) + H2_ManhattanDistance(InitialState),
        ]
    )
    explored.append(InitialState)

    while len(frontier) != 0:
        frontier.sort(key=lambda heur: heur[1])
        InitialState = frontier.pop(0)[0]
        print(f"{InitialState}")

        if InitialState == FinalState:
            print(f"Goal State : {InitialState} reached after searching {count} nodes.")
            break

        intermitt = puzzle8.moveBlankLeft(InitialState)
        frontier.append(
            [intermitt, H1_MisplacedTiles(intermitt) + H2_ManhattanDistance(intermitt)]
        )
        count += 1

        intermitt = puzzle8.moveBlankRight(InitialState)
        frontier.append(
            [intermitt, H1_MisplacedTiles(intermitt) + H2_ManhattanDistance(intermitt)]
        )
        count += 1

        intermitt = puzzle8.moveBlankDown(InitialState)
        frontier.append(
            [intermitt, H1_MisplacedTiles(intermitt) + H2_ManhattanDistance(intermitt)]
        )
        count += 1

        intermitt = puzzle8.moveBlankUp(InitialState)
        frontier.append(
            [intermitt, H1_MisplacedTiles(intermitt) + H2_ManhattanDistance(intermitt)]
        )
        count += 1


if __name__ == "__main__":
    main()
