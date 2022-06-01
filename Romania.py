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


def printGraph():
    for vertex in Romania_Graph:
        for edges in Romania_Graph[vertex]:
            print(f"{vertex} 👉 {edges[0]}, weight : {edges[1]}")


# printGraph()
visited = []


def DFS(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)

        for neighbour in graph[node]:
            DFS(visited, graph, neighbour[0])


DFS(visited, Romania_Graph, "Arad")
