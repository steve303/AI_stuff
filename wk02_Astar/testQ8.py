# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:43:08 2020

@author: stevensu
"""
a_maze = [[1,1,1,1,1],
          [1,0,0,1,1],
          [1,1,0,1,1],
          [1,1,0,0,1],
          [1,1,1,1,1]]
import numpy as np
def maze_to_graph(maze):
    ''' takes in a maze as a numpy array, converts to a graph '''
    # add your code here
    d_maze = {}
    a_maze = maze
    for i in range(len(a_maze)): 
        for j in range(len(a_maze[0])):
            
            if a_maze[i][j]==1: #case where state is a wall
                continue
            else:               #case where state is open
                d_maze[(j,i)]={}
                if j-1 >= 0:          
                    if a_maze[i][j-1]==0:
                        d_maze[(j,i)][(j-1,i)] = 'W'
                        
                if j+1 < len(a_maze[0]):   
                    if a_maze[i][j+1]==0:
                        d_maze[(j,i)][(j+1,i)] = 'E'
                
                if i-1 >= 0:
                    if a_maze[i-1][j]==0:
                        d_maze[(j,i)][(j,i-1)] = 'S'                        
                       
                if i+1 < len(a_maze):
                    if a_maze[i+1][j]==0:
                        d_maze[(j,i)][(j,i+1)] = 'N'                
        
            # add your code here 
    print('d_maze = ', d_maze)               
    return d_maze

maze_to_graph(a_maze)
# Example 1 to print output
# testmaze = np.ones((4,4))
# testmaze[1,1] = 0
# testmaze[2,1] = 0
# testmaze[2,2] = 0
# testgraph = maze_to_graph(testmaze)
# print(testgraph[(1,1)])
# print(testgraph[(1,2)])
# print(testgraph[(2,2)])

########### Example 2 ######
# testmaze = np.array([[1, 1, 1, 1, 1],[1, 0, 0, 0, 1],[1, 0, 0, 0, 1],[1, 1, 1, 1, 1]])
# testgraph = maze_to_graph(testmaze)
# print(testgraph[(1,1)])
# print(testgraph[(1,2)])
# print(testgraph[(2,1)])
# print(testgraph[(2,2)])
# print(testgraph[(3,1)])
# print(testgraph[(3,2)])