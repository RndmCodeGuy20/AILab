InitJugs = [0, 0]


def Full3(jugs):
    tempjugs = [0, 0]
    if jugs[1] == 3:
        return jugs
    else:
        tempjugs[0] = jugs[0]
        tempjugs[1] = 3
    return tempjugs


def Full4(jugs):
    tempjugs = [0, 0]
    if jugs[0] == 4:
        return jugs
    else:
        tempjugs[1] = jugs[1]
        tempjugs[0] = 4
    return tempjugs


def From3to4(jugs):
    tempjugs = [0, 0]
    tempjugs[0] = jugs[0]
    tempjugs[1] = jugs[1]

    if jugs[0] == 4:
        return jugs
    while tempjugs[0] != 4 and tempjugs[1] != 0:
        tempjugs[0] = tempjugs[0] + 1
        tempjugs[1] = tempjugs[1] - 1
    return tempjugs


def From4to3(jugs):
    tempjugs = [0, 0]
    tempjugs[0] = jugs[0]
    tempjugs[1] = jugs[1]

    if jugs[1] == 3:
        return jugs
    while tempjugs[0] != 0 and tempjugs[1] != 3:
        tempjugs[0] = tempjugs[0] - 1
        tempjugs[1] = tempjugs[1] + 1
    return tempjugs


def Empty4(jugs):
    tempjugs = [0, 0]
    tempjugs[0] = jugs[0]
    tempjugs[1] = jugs[1]

    if tempjugs[0] != 0:
        tempjugs[0] = 0
    return tempjugs


def Empty3(jugs):
    tempjugs = [0, 0]
    tempjugs[0] = jugs[0]
    tempjugs[1] = jugs[1]

    if tempjugs[1] != 0:
        tempjugs[1] = 0
    return tempjugs


explored = []
frontier = []
frontier.append(InitJugs)
count = 0

while len(frontier) != 0:
    InitJugs = frontier.pop(0)
    print(f"{InitJugs}")

    if InitJugs[0] == 2:
        print(f"Goal state {InitJugs} found after searching {count} nodes.")
        break

    if Full3(InitJugs) not in explored:
        explored.append(Full3(InitJugs))
        frontier.append(Full3(InitJugs))
        count += 1

    if Full4(InitJugs) not in explored:
        explored.append(Full4(InitJugs))
        frontier.append(Full4(InitJugs))
        count += 1

    if From4to3(InitJugs) not in explored:
        explored.append(From4to3(InitJugs))
        frontier.append(From4to3(InitJugs))
        count += 1

    if From3to4(InitJugs) not in explored:
        explored.append(From3to4(InitJugs))
        frontier.append(From3to4(InitJugs))
        count += 1

    if Empty3(InitJugs) not in explored:
        explored.append(Empty3(InitJugs))
        frontier.append(Empty3(InitJugs))
        count += 1

    if Empty4(InitJugs) not in explored:
        explored.append(Empty4(InitJugs))
        frontier.append(Empty4(InitJugs))
        count += 1
