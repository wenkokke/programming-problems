# Detect whether a given graph is cyclic

from collections import defaultdict

# graph : dict[int -> list(int)]

def detect_cycle(graph):

    indegree = defaultdict(lambda: 0)
    for u in graph.keys():
        for v in graph[u]:
            indegree[v] += 1

    retn = []
    start = [u for u in graph.keys() if indegree[u] == 0]
    while len(start) > 0:
        u = start.pop()
        retn.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                start.append(v)

    return any(indegree[u] != 0 for u in graph.keys())


if __name__ == "__main__":
    print detect_cycle({
        'a': [],
        'b': ['a'],
        'c': ['a', 'b']
    })
    print detect_cycle({
        'a': ['b'],
        'b': ['a'],
        'c': ['a', 'b']
    })
