#task 7
#A* algorithm
import heapq
def a_star_algorithm(graph, heuristics, start, goal):
    open_list = [(heuristics[start], start, [start], 0)]
    visited = set()
    while open_list:
        (f_score, current_node, path, g_cost) = heapq.heappop(open_list)
        if current_node in visited:
            continue
        if current_node == goal:
            return path, g_cost
        visited.add(current_node)
        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in visited:
                new_g_cost = g_cost + weight
                new_f_score = new_g_cost + heuristics.get(neighbor, 0)
                heapq.heappush(open_list, (new_f_score, neighbor, path + [neighbor], new_g_cost))
    return none, float('inf')
#example
example_graph = {
    'A' : [('B', 1), ('C', 3)],
    'B' : [('D', 3)],
    'C' : [('D', 1)],
    'D' : [('E', 2)],
    'E' : []
}
#heuristics values
example_heuristics = {
    'A': 5, 'B': 4, 'C': 2, 'D': 1, 'E': 0
}
path, cost = a_star_algorithm(example_graph, example_heuristics, 'A', 'E')
print(f"shortest path: {path}")
print(f"total cost: {cost} ")
