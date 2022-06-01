graph = {
    "5": ["3", "7"],
    "3": ["2", "4"],
    "7": ["8"],
    "2": [],
    "4": ["8"],
    "8": [],
}

# for vertex in graph:
#     print(f"Vertex : {vertex}\nConnected Edges : {graph[vertex]}\n")

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
        ["Arad", 140],
        ["Oradea", 151],
        ["Rimnicu Vilcea", 80],
        ["Fagaras", 99],
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
        ["Buchrest", 85],
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

# print(Romania_Graph['Arad'][0])
# for neighbour in Romania_Graph['Arad']:
#     print(neighbour[0])

# DFS algorithm in Python


# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {
    "0": set(["1", "2"]),
    "1": set(["0", "3", "4"]),
    "2": set(["0"]),
    "3": set(["1"]),
    "4": set(["2", "3"]),
}

dfs(graph, "0")
