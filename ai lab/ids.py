t= {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}


def dfs_limited(node,goal,depth):
    if node == goal:
        return True

    if depth<=0:
        return False
    
    for neighbour in t.get(node,[]):
        if dfs_limited(neighbour,goal,depth - 1):
            return True
    return False


def ids(start,goal,max_depth):
    for depth in range(max_depth + 1):
        if dfs_limited(start,goal,depth):
            print(f"Goal {goal} found at depth {depth}")
            return True
    print(f"Goal {goal} not found!")
    return False

start_node = 'A'
goal_node = 'G'
depth_limit = 4
ids(start_node, goal_node,depth_limit)