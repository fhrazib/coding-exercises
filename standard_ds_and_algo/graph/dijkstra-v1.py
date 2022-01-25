def pick_min_cost_vertex(processed, cost, n):
    min_cost = float('inf')
    vertex = None

    for i in range(n):
        if not processed[i]:
            if min_cost > cost[i]:
                min_cost = cost[i]
                vertex = i
    return vertex


def simple_dijkstra(graph, source):
    n = len(graph[0])
    inf = float('inf')
    parents = [-1] * n
    processed = [False] * n
    cost = [inf] * n

    cost[source] = 0
    # We only need to process (|V| - 1) nodes. Then the last node will be left processed automatically
    # Last node need to be processed
    for i in range(n - 1):
        u = pick_min_cost_vertex(processed, cost, n)
        processed[u] = True

        for v in range(n):
            if graph[u][v] != 0 and (not processed[v]):
                if (cost[u] + graph[u][v]) < cost[v]:
                    cost[v] = cost[u] + graph[u][v]
                    parents[v] = u

    print('parents: ', parents)
    print('cost:    ', cost)


def main():

    # Expected output
    # parents:  [-1, 0, 0, 1, 3, 3]
    # costs:    [0, 1, 4, 3, 7, 9]
    graph = [
        [0, 1, 4, 0, 0, 0],
        [1, 0, 4, 2, 7, 0],
        [4, 4, 0, 3, 5, 0],
        [0, 2, 3, 0, 4, 6],
        [0, 7, 5, 4, 0, 7],
        [0, 0, 0, 6, 7, 0]
    ]
    simple_dijkstra(graph, 0)
    pass


if __name__ == "__main__":
    main()
