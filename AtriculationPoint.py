"""The script finds all the articulation points in a connected undirected graph"""

"""check whether the graph is connected by traversing all the nodes using DFS (Depth First Search) 
    input: graph as dictionary 
    output: bool
"""
def isConnected(graph):
    trav = set()
    start = None
    for k in graph:
        start = k
        break

    # Traverse the Graph using Depth First Search (recursive loop)
    def DFS(node):
        trav.add(node)

        for child in graph[node]:
            if child not in trav:
                DFS(child)
        return

    DFS(start)
    if len(trav) == len(graph):
        return True
    return False

"""create graph as a data structure (dictionary)
    input : nodeNum (integer) - number of nodes
    input : edges (List) - edges of the graph
    output: graph as dictionary 
"""
def getGraph(nodeNum, edges):
    g = {}
    # Create a empty list for each node n
    for n in range(nodeNum):
        g[n] = []

    # Add edges corresponding to each node in the list
    for edg in edges:
        g[edg[0]].append(edg[1])
        g[edg[1]].append(edg[0])

    return g

#
"""find the articulation points (critical nodes) in a graph
    input : nodeNum (integer) - number of nodes
    input : edges (List) - edges of the graph
    output: ans (List) - list of articulation points
"""
def findCriticalNodes(nodeNum, edges):
    ans = []
    for n in range(nodeNum):
        g = getGraph(nodeNum, edges)
        del g[n]
        # for each node n in graph, remove the node and check if the graph is still connected
        for node in g:
            if n in g[node]:
                g[node].remove(n)

        if (not isConnected(g)):
            ans.append(n)

    return ans


def main():
    if __name__ == "__main__":
        """
        userInput1 - numOfNodes as an Integer, the nodes will be a set of integers = {0, ..., numOfNodes - 1} 
        Eg. numOfNodes = 3, nodes = {0, 1, 2}
        userInput2 - edges between the nodes as an 2D list 
        """
        numOfNodes = 7
        edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
        print('Articulation points: ' + str(findCriticalNodes(numOfNodes, edges)))

main()