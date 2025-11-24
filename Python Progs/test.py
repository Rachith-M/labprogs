from collections import deque
def print_board(board):
    for row in board:
        print(" ".join(map(str,row)))
    print()
def move_blank(board,direction):
    new_board=[row.copy() for row in board]
    for i in range(3):
        for j in range(3):
            if new_board[i][j]==0:
                if direction=='up' and i>0:
                    new_board[i][j],new_board[i-1][j]=new_board[i-1][j],new_board[i][j]
                elif direction=='down'and i<2:
                    new_board[i][j],new_board[i+1][j]=new_board[i+1][j],new_board[i][j]
                elif direction=='left' and j>0:
                    new_board[i][j],new_board[i][j-1]=new_board[i][j-1],new_board[i][j]
                    
                elif direction=='right'and j<2:
                    new_board[i][j],new_board[i][j+1]=new_board[i][j+1],new_board[i][j]
                else:
                    return None
                return new_board
    return None
def is_goal(board,goal_board):
    return board==goal_board
def bfs(initial_board,goal_board):
    visited=set()
    queue=deque([(initial_board,[])])
    while queue:
        current_board,path=queue.popleft()
        if is_goal(current_board,goal_state):
            print("solution found")
            return path
        visited.add(tuple(map(tuple,current_board)))
        for direction in ['up','down','left','right']:
            new_board=move_blank(current_board,direction)
            if new_board and tuple(map(tuple,new_board)) not in visited:
                queue.append((new_board,path+[direction]))
if __name__=="__main__":
    initial_state = [[1, 2, 0],
                     [3, 4, 5],
                     [7, 8, 6]]

    goal_state = [[0, 1, 2],
                     [3, 4, 5],
                     [7, 8, 6]]
    print(" initial_state")
    print_board(initial_state)
    print("goal_state")
    print_board(goal_state)
    solution_path=bfs(initial_state,goal_state)
    if solution_path:
        print("Solution path:")
        for step,move in enumerate(solution_path,1):
            print(f"step:{step},move:{move}")
    else:
        print("no solution found")