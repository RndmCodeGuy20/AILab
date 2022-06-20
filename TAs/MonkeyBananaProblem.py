"""
@author Shantanu Mane (RndmCodeGuy20)
@branch CSE - AIML
@semester IV
@topic TA2 - Programming Assignment
"""

initialMonkeyPosition = [0, 0, 0]

finalMonkeyPosition = [5, 5, 1]


class Monkey:
    x = 0
    y = 0
    z = 0
    chairStatus = 0
    bananaStatus = 0

    def __init__(self, position, chairStatus, bananaStatus):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.chairStatus = chairStatus
        self.bananaStatus = bananaStatus

    def updatePosition(self, position):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]

    def updateChairStatus(self, chairStatus):
        self.z += 1
        self.chairStatus = chairStatus

    def updateBananaStatus(self, bananaStatus):
        self.bananaStatus = bananaStatus

    def getPosition(self):
        return [self.x, self.y, self.z]


def ManhattanDistance(state, position):
    return abs(state[0] - position[0]) + abs(state[1] - position[1])


def monkeyUp(intermittState):
    tempState = [0, 0, 0]
    for i in range(3):
        tempState[i] = intermittState[i]

    if tempState[1] >= 10:
        return tempState

    tempState[1] += 1

    return tempState


def monkeyDown(intermittState):
    tempState = [0, 0, 0]
    for i in range(3):
        tempState[i] = intermittState[i]

    if tempState[1] <= 0:
        return tempState

    tempState[1] -= 1

    return tempState


def monkeyRight(intermittState):
    tempState = [0, 0, 0]
    for i in range(3):
        tempState[i] = intermittState[i]

    if tempState[0] >= 10:
        return tempState

    tempState[0] += 1

    return tempState


def monkeyLeft(intermittState):
    tempState = [0, 0, 0]
    for i in range(3):
        tempState[i] = intermittState[i]

    if tempState[0] <= 0:
        return tempState

    tempState[0] -= 1

    return tempState


monkey = Monkey(initialMonkeyPosition, 0, 0)


def findBananaInRoom(currentPosition):
    global finalMonkeyPosition
    frontier = []
    explored = []
    frontier.append(
        [currentPosition, ManhattanDistance(currentPosition, finalMonkeyPosition)]
    )
    explored.append(currentPosition)

    while len(frontier) != 0:
        frontier.sort(key=lambda frontier: frontier[1])
        state = frontier.pop(0)[0]
        print(f"{state}\n   ⬇️")

        if state == finalMonkeyPosition:
            monkey.updateBananaStatus(1)
            monkey.updatePosition(state)
            return

        frontier.append(
            [monkeyUp(state), ManhattanDistance(monkeyUp(state), finalMonkeyPosition)]
        )
        explored.append(monkeyUp(state))

        frontier.append(
            [monkeyDown(state), ManhattanDistance(monkeyUp(state), finalMonkeyPosition)]
        )
        explored.append(monkeyDown(state))

        frontier.append(
            [monkeyLeft(state), ManhattanDistance(monkeyUp(state), finalMonkeyPosition)]
        )
        explored.append(monkeyLeft(state))

        frontier.append(
            [
                monkeyRight(state),
                ManhattanDistance(monkeyUp(state), finalMonkeyPosition),
            ]
        )
        explored.append(monkeyRight(state))


def findChairInRoom(initialMonkeyPosition, chairPosition):

    frontier = []
    explored = []
    frontier.append(
        [initialMonkeyPosition, ManhattanDistance(initialMonkeyPosition, chairPosition)]
    )
    explored.append(initialMonkeyPosition)

    while len(frontier) != 0:
        frontier.sort(key=lambda frontier: frontier[1])
        state = frontier.pop(0)[0]
        monkey.updatePosition(state)
        print(f"{state}\n   ⬇️")

        if state == chairPosition:
            print(f" Monkey has found the chair!!!", end=" ➡️ ")
            monkey.updatePosition(state)
            monkey.updateChairStatus(1)
            findBananaInRoom(monkey.getPosition())
            return

        frontier.append(
            [monkeyUp(state), ManhattanDistance(monkeyUp(state), chairPosition)]
        )
        explored.append(monkeyUp(state))

        frontier.append(
            [monkeyDown(state), ManhattanDistance(monkeyUp(state), chairPosition)]
        )
        explored.append(monkeyDown(state))

        frontier.append(
            [monkeyLeft(state), ManhattanDistance(monkeyUp(state), chairPosition)]
        )
        explored.append(monkeyLeft(state))

        frontier.append(
            [monkeyRight(state), ManhattanDistance(monkeyUp(state), chairPosition)]
        )
        explored.append(monkeyRight(state))


findChairInRoom(initialMonkeyPosition, chairPosition=[5, 10, 0])
print(
    f"\nMonkey Coordinates : ({monkey.x}, {monkey.y}, {monkey.z}), Chair Status : {monkey.chairStatus}, Banana Status : {monkey.bananaStatus}"
)
