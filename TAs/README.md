# <center>Teacher's Assignment 1 - Romania Graph Solver Using Different Algorithms</center>

### Date: June 6, 2022 <br>

### Roll Number: 63 <br>

### Student: Shantanu Mane <br>

### Tags: Assignment <br>

# _Code ⬇️_

```python
import simple_chalk as chalk

class City:
    def __init__(self, name: str, heuristic: int) -> None:
        self.name = name
        self.heuristic = heuristic

Arad = City("Arad", 366)
Bucharest = City("Bucharest", 0)
Craiova = City("Craiova", 160)
Dobreta = City("Dobreta", 242)
Eforie = City("Eforie", 161)
Fagaras = City("Fagaras", 178)
Giurgui = City("Giurgui", 77)
Hirsova = City("Hirsova", 151)
Lasi = City("Lasi", 226)
Lugoj = City("Lugoj", 244)
Mehadia = City("Mehadia", 241)
Neamt = City("Neamt", 234)
Oradea = City("Oradea", 380)
Pitesti = City("Pitesti", 98)
Rimnicu = City("Rimnicu", 193)
Sibiu = City("Sibiu", 253)
Timisora = City("Timisora", 329)
Urziceni = City("Urziceni", 80)
Vaslui = City("Vaslui", 199)
Zerind = City("Zerind", 374)

Romania_Graph = {
    Arad.name: [
        [Timisora, 118],
        [Zerind, 75],
        [Sibiu, 140],
    ],
    Zerind.name: [
        [Arad, 75],
        [Oradea, 71],
    ],
    Timisora.name: [
        [Arad, 118],
        [Lugoj, 111],
    ],
    Sibiu.name: [
        [Fagaras, 99],
        [Arad, 140],
        [Oradea, 151],
        [Rimnicu, 80],
    ],
    Oradea.name: [
        [Zerind, 71],
        [Sibiu, 151],
    ],
    Lugoj.name: [
        [Timisora, 111],
        [Mehadia, 70],
    ],
    Rimnicu.name: [
        [Sibiu, 80],
        [Craiova, 146],
        [Pitesti, 97],
    ],
    Fagaras.name: [
        [Sibiu, 99],
        [Bucharest, 211],
    ],
    Mehadia.name: [
        [Lugoj, 70],
        [Dobreta, 75],
    ],
    Dobreta.name: [
        [Craiova, 120],
        [Mehadia, 75],
    ],
    Craiova.name: [
        [Dobreta, 120],
        [Rimnicu, 146],
        [Pitesti, 138],
    ],
    Pitesti.name: [
        [Rimnicu, 97],
        [Craiova, 138],
        [Bucharest, 101],
    ],
    Bucharest.name: [
        [Pitesti, 101],
        [Fagaras, 211],
        [Giurgui, 90],
        [Urziceni, 85],
    ],
    Giurgui.name: [
        [Bucharest, 90],
    ],
    Urziceni.name: [
        [Bucharest, 85],
        [Hirsova, 98],
        [Vaslui, 142],
    ],
    Hirsova.name: [
        [Urziceni, 98],
        [Eforie, 86],
    ],
    Eforie.name: [
        [Hirsova, 86],
    ],
    Vaslui.name: [
        [Urziceni, 142],
        [Lasi, 92],
    ],
    Lasi.name: [
        [Vaslui, 92],
        [Neamt, 87],
    ],
    Neamt.name: [
        [Lasi, 87],
    ],
}

def DFS(start):
    visited = []
    stack = []
    pathcost = 0
    depth = 0
    stack.append(start)

    while len(stack) != 0:
        node = stack.pop()

        if node is Bucharest.name:
            print(chalk.greenBright(node))
            break

        if node not in visited:
            # Order of explored nodes depend on their location in the adjacency list,
            # DFS exploits this approach and visits the top node in the stack and explores that node,
            # in some cases this TOS node might be the one which was previously explored.
            # This can cause a loop in the exploration and will never give the goal node.
            # TODO: To convert this program to tree search, remove this condition.
            print(chalk.greenBright(node), end=" 👉 ")
            visited.append(node)
            depth += 1

            for neighbour in Romania_Graph[node]:
                stack.append(neighbour[0].name)
            pathcost += neighbour[1]

    return [pathcost, depth]

def DLFS(start, limit=3):
    visited = []
    stack = []
    pathcost = 0
    depth = 0
    stack.append(start)

    for i in range(limit):
        node = stack.pop()

        if node is Bucharest.name:
            print(chalk.redBright(node))
            break

        if node not in visited:
            print(chalk.redBright(node), end=" 👉 ")
            visited.append(node)
            depth += 1

            for neighbour in Romania_Graph[node]:
                stack.append(neighbour[0].name)
            pathcost += neighbour[1]

    return [pathcost, depth]

goalReached = False
count = 0

def IterDFS(start, limit):
    global goalReached, count

    if goalReached:
        return

    visited = []
    stack = []
    stack.append(start)

    for j in range(limit):
        node = stack.pop()

        if node is Bucharest.name:
            print(chalk.greenBright(node))
            goalReached = True
            break

        if node not in visited:
            print(chalk.greenBright(node), end=" 👉 ")
            visited.append(node)

            for neighbour in Romania_Graph[node]:
                stack.append(neighbour[0].name)

    count += 1
    print("\n")
    IterDFS("Arad", count)

def A_Star_Search(start):
    stack = []
    visited = []
    totalPathCost = start[1]  # totalPathCost = pathCost + Heuristic
    stack.append(start)

    while len(stack) != 0:
        # for i in range(2):
        stack.sort(key=lambda el: el[1], reverse=True)
        node = stack.pop()

        if len(visited) != 0:
            for prevNode in Romania_Graph[visited[len(visited) - 1]]:
                if prevNode[0].name is node[0]:
                    totalPathCost = totalPathCost + prevNode[1] + node[1]

        if node[0] is Bucharest.name:
            print(chalk.greenBright(node[0]))
            break

        if node[0] not in visited:
            print(chalk.greenBright(node[0]), end=" 👉 ")
            visited.append(node[0])

            for neighbour in Romania_Graph[node[0]]:
                stack.append([neighbour[0].name, neighbour[0].heuristic + neighbour[1]])

    return totalPathCost

print(chalk.magenta.bgGray.underline(f"\n\t\t\t\t\t 🔍⛵🌊🦭🔎 Romania Graph Solver 🔍⛵🌊🦭🔎"))
print(
    chalk.grey(
        "\n-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n\n"
    )
)

print(chalk.cyan("DFS : \t"))
rezDFS = DFS("Arad")
print(
    chalk.blue(
        f"\nDepth First Search to find 'Bucharest' ➡️ \nPath Cost : {rezDFS[0]}\t\tDepth : {rezDFS[1]}"
    )
)
print(
    chalk.grey(
        "\n-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n\n"
    )
)

print(chalk.cyan("DLFS : \t"))
rezDLFS = DLFS("Arad")
print(
    chalk.yellow(
        f"\n\nDepth Limited First Search to find 'Bucharest' ➡️ \nPath Cost : {rezDLFS[0]}\t\tDepth : {rezDLFS[1]}\n\nWith maximum depth = 3, goal state could not be reached!!!"
    )
)
print(
    chalk.grey(
        "\n-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n\n"
    )
)

print(chalk.cyan("IterDFS : \t"))
IterDFS("Arad", count)
print(
    chalk.blueBright(
        f"Iterative Depth First Search to find 'Bucharest' ➡️ \nGoal State was reached after {count} iterations!"
    )
)
print(
    chalk.grey(
        "\n-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n\n"
    )
)

print(chalk.cyan("A* : \t"))
rezDFS = A_Star_Search(start=[Arad.name, Arad.heuristic])
print(chalk.blue(f"\nA* Search to find 'Bucharest' ➡️ \nPath Cost : {rezDFS}"))
print(
    chalk.grey(
        "\n-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"
    )
)
```

# _Explanation_ ⬇️

1. DFS Function
   - Explores nodes in Depth First Search order.
   - Tree search is _not_ implemented, as it creates looping
   - > Note : tree search can be implemented and will give a valid output, but that will solely depend on the position of child nodes in the adjacency list. Which makes it un-generalised.
2. DLFS Function

   - Explores nodes in Depth Limited Search pattern.
   - Depth limit is given as 3.
   - Goal node cannot be reached in depth 3 in any path possible.

3. IDFS Function

   - Explores nodes in Iterative DFS.
   - Increases limit of DFS in every iteration until goal node is reached.

4. A\* Function
   - Explores nodes in A\* search pattern
   - Heuristic is airline / straightline distance from each and every node to goal node.

# _Output ⬇️_

```python
🔍⛵🌊🦭🔎 Romania Graph Solver 🔍⛵🌊🦭🔎

-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

DFS :
Arad 👉 Sibiu 👉 Rimnicu 👉 Pitesti 👉 Bucharest

Depth First Search to find 'Bucharest' ➡️
Path Cost : 418		Depth : 4

-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

DLFS :
Arad 👉 Sibiu 👉 Rimnicu 👉

Depth Limited First Search to find 'Bucharest' ➡️
Path Cost : 317		Depth : 3

With maximum depth = 3, goal state could not be reached!!!

-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

IterDFS :

Arad 👉

Arad 👉 Sibiu 👉

Arad 👉 Sibiu 👉 Rimnicu 👉

Arad 👉 Sibiu 👉 Rimnicu 👉 Pitesti 👉

Arad 👉 Sibiu 👉 Rimnicu 👉 Pitesti 👉 Bucharest

Iterative Depth First Search to find 'Bucharest' ➡️
Goal State was reached after 5 iterations!

-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

A* :
Arad 👉 Sibiu 👉 Rimnicu 👉 Pitesti 👉 Bucharest

A* Search to find 'Bucharest' ➡️
Path Cost : 1746

-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
```
