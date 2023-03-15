
import time
import sys
def dfs(maze):
    sys.setrecursionlimit(10000) #change this parameter for larger mazes
    start_time = time.perf_counter()
    total_count = 0
    start = (0, maze[0].index('-'))  # Find the starting point at the top row
    visited_check = set()# keeps track of visited nodes 
    visited_save = []
    path = []  # List to keep track of the path taken to reach the exit
    # Function to check if a given position is valid to move into
    def is_valid(pos,visited):
        row, col = pos
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == '-' and pos not in visited:
            return True
        return False

    # Function to get the neighbors of a given position
    def get_neighbors(pos,visited):
        row, col = pos
        neighbors = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
        valid_neighbors = [pos for pos in neighbors if is_valid(pos,visited)]
        return valid_neighbors
    def traverse(node,path,visited):
        nonlocal total_count
        visited.add(node) #add node to set of visited nodes
        visited_save.append(node)
        total_count+=1
        path.append(node) #add node to the current path
        
        if(node[0] == len(maze)-1): # if we reached goal 
            return path
        
        neighbors = get_neighbors(node,visited_check) # get all valid neighbors of the node
        for neighbor in neighbors:
            answer_path = traverse(neighbor,path,visited)
            if answer_path:
                return path
        path.pop() #pop the node in a path if the node doesnt lead to the goal
        return None # None if there is no path to the exit , or no exit
    
    path = traverse(start,path,visited_check)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    if(path):
        print("Total count of visited nodes is: "+str(total_count))
        print("Total length of the final path is: "+str(len(path)))
        print("Total execution time is "+ str(execution_time))
    return path, visited_save   