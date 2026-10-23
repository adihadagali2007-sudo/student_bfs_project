from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))

    return None


# Academic support pathway graph
graph = {
    "Start": ["Identify Weak Subject"],
    "Identify Weak Subject": ["Revise Concepts", "Ask Teacher"],
    "Revise Concepts": ["Practise Questions"],
    "Ask Teacher": ["Revise Concepts"],
    "Practise Questions": ["Take Mock Test"],
    "Take Mock Test": ["Review Performance"],
    "Review Performance": []
}

path = bfs(graph, "Start", "Review Performance")

if path:
    print("BFS Academic Support Path:")
    print(" -> ".join(path))
else:
    print("No pathway found.")