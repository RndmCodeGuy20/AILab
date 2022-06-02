Romania_Graph = {
    "Arad": [
        ["Zerind", 75],
        ["Timisora", 118],
        ["Sibiu", 140],
    ],
    "Zerind": [
        ["Arad", 75],
        ["Oradea", 71],
    ],
    "Timisora": [
        ["Arad", 118],
        ["Lugoj", 111],
    ],
    "Sibiu": [
        ["Fagaras", 99],
        ["Arad", 140],
        ["Oradea", 151],
        ["Rimnicu Vilcea", 80],
    ],
    "Oradea": [
        ["Zerind", 71],
        ["Sibiu", 151],
    ],
    "Lugoj": [
        ["Timisora", 111],
        ["Mehadia", 70],
    ],
    "Rimnicu Vilcea": [
        ["Sibiu", 80],
        ["Craiova", 146],
        ["Pitesti", 97],
    ],
    "Fagaras": [
        ["Sibiu", 99],
        ["Bucharest", 211],
    ],
    "Mehadia": [
        ["Lugoj", 70],
        ["Dobreta", 75],
    ],
    "Dobreta": [
        ["Craiova", 120],
        ["Mehadia", 75],
    ],
    "Craiova": [
        ["Dobreta", 120],
        ["Rimnicu Vilcea", 146],
        ["Pitesti", 138],
    ],
    "Pitesti": [
        ["Rimnicu Vilcea", 97],
        ["Craiova", 138],
        ["Bucharest", 101],
    ],
    "Bucharest": [
        ["Pitesti", 101],
        ["Fagaras", 211],
        ["Giurgiu", 90],
        ["Urziceni", 85],
    ],
    "Giurgiu": [
        ["Bucharest", 90],
    ],
    "Urziceni": [
        ["Bucharest", 85],
        ["Hirsova", 98],
        ["Vaslui", 142],
    ],
    "Hirsova": [
        ["Urziceni", 98],
        ["Eforie", 86],
    ],
    "Eforie": [
        ["Hirsova", 86],
    ],
    "Vaslui": [
        ["Urziceni", 142],
        ["Lasi", 92],
    ],
    "Lasi": [
        ["Vaslui", 92],
        ["Neamt", 87],
    ],
    "Neamt": [
        ["Lasi", 87],
    ],
}

visited = []
stack = []


def DFS(start):
    stack.append(start)
    depth = 0
    distance = 0

    while len(stack) != 0:
        node = stack.pop()

        if node not in visited:
            print(f"{node}", end=" 👉 ")
            visited.append(node)
            depth += 1

            if node == "Bucharest" or "Bucharest" in visited:
                break

            for neighbour in Romania_Graph[node]:
                stack.append(neighbour[0])
            distance += neighbour[1]

    return [depth, distance]


val = DFS("Arad")

print(
    f"\n\nDepth at which Bucharest was found = {val[0]}\nDistance from start to goal = {val[1]}"
)
