from collections import defaultdict
graph = defaultdict(list)
graph['A'] = ['B','C']
graph['B'] = ['D','E']
graph['C'] = ['F']
graph['D'] = []
graph['E'] = ['G','H']
graph['F'] = []
graph['G'] = []
graph['H'] = []
def depth_limit_search(node,goal,limit,current_depth = 0):
    print(f"Visiting node: {node} | Current depth: {current_depth}")
    if node==goal:
        return True
    if  current_depth==limit:
        return False

    for neighbour in graph[node]:
        if depth_limit_search(neighbour,goal,limit,current_depth + 1):
            return True
    return False
    
def iterative_deepening_search(start,goal,max_depth):
    for limit in range(max_depth+1):
        print(f"\n--- Searching up to depth {limit}")
        if depth_limit_search(start, goal, limit):
            print(f"\n Goal '{goal}' found at depth {limit}")
            return True
    print(f"\n Goal '{goal}' not found within depth {max_depth}")
    return False

start_node = 'A'
goal_node = 'H'
max_depth = 3
iterative_deepening_search(start_node,goal_node,max_depth)