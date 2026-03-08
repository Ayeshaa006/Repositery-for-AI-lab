#task 6
#1.BFS without queue & without node
def bfs_without_queue_node(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end="")
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
#testing
graph = {
    '0': ['1', '2'],
    '1': ['0', '3', '4'],
    '2': ['0',],
    '3': ['1'],
    '4': ['2', '3']
    }
print("bfs without queue & node:")
bfs_without_queue_node(graph, '0')




#BFS with queue & node
from collections import deque
class node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
def bfs_with_queue_node(start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    while queue:
        current = queue.popleft()
        print(current.value, end="")
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
#testing
n0 = node('0')
n1 = node('1')
n2 = node('2')
n0.neighbors = [n1, n2]
n1.neighbors = [n0]
n2.neighbors = [n0]
print("\nBFS with queue & node:")
bfs_with_queue_node(n0)