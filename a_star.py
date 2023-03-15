import heapq
import sys
import time
import math
def a_star(maze):
    
    start_time = time.perf_counter()
    start = (0,maze[0].index('-'))
    end = (len(maze)-1,maze[-1].index('-'))
    
    paths = {}

    queue = [] #creation of priority queue 
    heapq.heappush(queue,(0,start)) # push start with the highest priority
    
    def heuristic(node,goal):
        """Calculate the Manhattan distance between two nodes."""
        x1, y1 = node
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)
    def heuristic2(current,goal):
        """
        Calculates the Euclidean distance heuristic between two points in 2D space.

        :param current: tuple representing the current point (x, y)
        :param goal: tuple representing the goal point (x, y)
        :return: Euclidean distance between the current point and the goal point
        """
        dx = current[0] - goal[0]
        dy = current[1] - goal[1]
        return math.sqrt(dx*dx + dy*dy)
    
    def get_neighbors(node):
        row, col = node 
        neighbors = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
        valid_neighbors = [pos for pos in neighbors if is_valid(pos)]
        return valid_neighbors
    
    def is_valid(pos):
        """ Check if the node is valid"""
        row, col = pos
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == '-':
            return True
        return False
    def reconstruct_path(node):
        """Reconstruct path from the node, using paths dictionary"""
        nonlocal start_time
        
        path = [node]

        while node in paths:
            node = paths[node]
            path.append(node)
        path.reverse()
        
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        
        print("Total count of visited nodes is: "+str(len(paths)))
        print("Total length of the final path is: "+str(len(path)))
        print("Total execution time is "+ str(execution_time))
        
        return path , paths.keys()
    
    #initiate g_score and f_score 
    g_score = {start:0}
    f_score = {start: heuristic(start,end)}
    
    
    while (len(queue)!=0):
        node = heapq.heappop(queue) #get the node with the lowest f score
        priority,node = node
        row,col = node 
        if(row == len(maze)-1):
            
            return reconstruct_path(node)
        
        for neighbor in get_neighbors(node):
            next_g_score = g_score[node]+1 #next node will be +1 further from the start
            
            if neighbor not in g_score or next_g_score < g_score[neighbor]:
                # update data structures 
                paths[neighbor] = node
                g_score[neighbor] = next_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end)
                #push neighbor to priority queue
                
                heapq.heappush(queue,(f_score[neighbor],neighbor))
    #if goal is not found return None
    return None