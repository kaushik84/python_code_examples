def execute(numofnodes, node_connections):
    graph = create_dictionary(numofnodes, node_connections)
    traverse(graph)


def create_dictionary(numofnodes, node_connections):
    graph = {}
    for node in range(numofnodes):
        graph[node] = []
    for conn in node_connections:
        graph[conn[0]].append(conn[1])
        graph[conn[1]].append(conn[0])
    return graph


def traverse(graph):
    visited = set()

    def dfs(node):
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                dfs(child)

    keys = list(graph)
    print(keys)
    dfs(keys[4])

    print(visited)



print(execute(7, [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]))
