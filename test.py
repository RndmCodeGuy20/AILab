romania = {
    "Arad": [
        "Sibiu",
        "Zerind",
        "Timisoara",
    ],
    "Zerind": [
        "Arad",
        "Oradea",
    ],
    "Oradea": [
        "Zerind",
        "Sibiu",
    ],
    "Sibiu": [
        "Arad",
        "Oradea",
        "Fagaras",
        "Rimnicu",
    ],
    "Timisoara": [
        "Arad",
        "Lugoj",
    ],
    "Giurgiu": [
        "Bucharest",
    ],
    "Urziceni": [
        "Bucharest",
        "Vaslui",
        "Hirsova",
    ],
    "Hirsova": [
        "Urziceni",
        "Eforie",
    ],
    "Eforie": [
        "Hirsova",
    ],
    "Lugoj": [
        "Timisoara",
        "Mehadia",
    ],
    "Mehadia": [
        "Lugoj",
        "Drobeta",
    ],
    "Drobeta": [
        "Mehadia",
        "Craiova",
    ],
    "Craiova": [
        "Drobeta",
        "Rimnicu",
        "Pitesti",
    ],
    "Rimnicu": [
        "Sibiu",
        "Craiova",
        "Pitesti",
    ],
    "Fagaras": [
        "Sibiu",
        "Bucharest",
    ],
    "Pitesti": [
        "Rimnicu",
        "Craiova",
        "Bucharest",
    ],
    "Bucharest": [
        "Fagaras",
        "Pitesti",
        "Giurgiu",
        "Urziceni",
    ],
    "Vaslui": [
        "Iasi",
        "Urziceni",
    ],
    "Iasi": [
        "Vaslui",
        "Neamt",
    ],
    "Neamt": [
        "Iasi",
    ],
}


def DFS(start):
    stack = []
    vis = []
    stack.append(start)

    while len(stack) != 0:
        node = stack.pop()

        if node == "Bucharest":
            print(node)
            break

        if node not in vis:
            print(node)
            vis.append(node)

            for neighbour in romania[node]:
                stack.append(neighbour)


DFS("Arad")
