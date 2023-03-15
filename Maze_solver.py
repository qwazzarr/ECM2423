#!/usr/bin/env python
# coding: utf-8

# In[20]:


def list_transform(file_path):
    # Initialize an empty list to hold the 2D list
    result = []
    
    # Open the file in read mode
    with open(file_path, 'r') as f:
        # Read the lines from the file
        lines = f.readlines()
        
        # Iterate over each line and split it by whitespace
        for line in lines:
            row = line.strip().split()
            
            
            # Add the row to the result list
            result.append(row)
    #delete empty rows
    result = list(filter(lambda x: len(x)!= 0, result))
            
    return result


# In[60]:


def dfs(maze):
    start = (0, maze[0].index('-'))  # Find the starting point at the top row
    visited = set()  # Keeps track of visited nodes
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

    # stack realisation of dfs
#     while stack:
#         curr_pos = stack.pop()
#         visited.add(curr_pos)
#         path.append(curr_pos)

#         if curr_pos[0] == len(maze)-1:  # If it's '-' and the last row it's exit.
#             return path
        
#         neighbors = get_neighbors(curr_pos)
#         if(len(neighbors) == 0):
            
#         stack.extend(neighbors)
    #recursion realisation of dfs
    def traverse(node,path,visited):
        visited.add(node)
        path.append(node)
        
        if(node[0] == len(maze)-1):
            return path
        
        neighbors = get_neighbors(node,visited)
        for neighbor in neighbors:
            answer_path = traverse(neighbor,path,visited)
            if answer_path:
                return path
        path.pop()
        return None # None if there is no path to the exit , or no exit
    
    path = traverse(start,path,visited)
    return path


# In[61]:


def solution(file_path):
    result = list_transform(file_path)
    path = dfs(result)
    
    def print_maze(maze):
        
        for i in maze:
            print(' '.join(i))
    if path is not None:
        print("The path taken to reach the goal is:")
        move_count =0
        for pos in path:
            move_count+=1
            row, col = pos
            result[row][col] = '*'
            print_maze(result)
            print("Move count is "+str(move_count))
        return path
    else:
        print("No path found!")
        return("No path found!")


# In[63]:


solution("maze-Medium.txt")


# In[ ]:




