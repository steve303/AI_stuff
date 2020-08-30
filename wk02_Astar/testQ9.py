# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:44:34 2020

@author: stevensu
"""

import numpy as np
from collections import OrderedDict
from collections import deque
maze = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                 [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
                 [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                 [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])



map_distances = dict(
    chi=OrderedDict([("det",283), ("cle",345), ("ind",182)]),
    cle=OrderedDict([("chi",345), ("det",169), ("col",144), ("pit",134), ("buf",189)]),
    ind=OrderedDict([("chi",182), ("col",176)]),
    col=OrderedDict([("ind",176), ("cle",144), ("pit",185)]),
    det=OrderedDict([("chi",283), ("cle",169), ("buf",256)]),
    buf=OrderedDict([("det",256), ("cle",189), ("pit",215), ("syr",150)]),
    pit=OrderedDict([("col",185), ("cle",134), ("buf",215), ("phi",305), ("bal",247)]),
    syr=OrderedDict([("buf",150), ("phi",253), ("new",254), ("bos",312)]),
    bal=OrderedDict([("phi",101), ("pit",247)]),
    phi=OrderedDict([("pit",305), ("bal",101), ("syr",253), ("new",97)]),
    new=OrderedDict([("syr",254), ("phi",97), ("bos",215), ("pro",181)]),
    pro=OrderedDict([("bos",50), ("new",181)]),
    bos=OrderedDict([("pro",50), ("new",215), ("syr",312), ("por",107)]),
    por=OrderedDict([("bos",107)]))


map_times = dict(
    chi=dict(det=280, cle=345, ind=200),
    cle=dict(chi=345, det=170, col=155, pit=145, buf=185),
    ind=dict(chi=200, col=175),
    col=dict(ind=175, cle=155, pit=185),
    det=dict(chi=280, cle=170, buf=270),
    buf=dict(det=270, cle=185, pit=215, syr=145),
    pit=dict(col=185, cle=145, buf=215, phi=305, bal=255),
    syr=dict(buf=145, phi=245, new=260, bos=290),
    bal=dict(phi=145, pit=255),
    phi=dict(pit=305, bal=145, syr=245, new=150),
    new=dict(syr=260, phi=150, bos=270, pro=260),
    pro=dict(bos=90, new=260),
    bos=dict(pro=90, new=270, syr=290, por=120),
    por=dict(bos=120))

def path(previous, s): 
    '''
    `previous` is a dictionary chaining together the predecessor state that led to each state
    `s` will be None for the initial state
    otherwise, start from the last state `s` and recursively trace `previous` back to the initial state,
    constructing a list of states visited as we go
    '''
    if s is None:
        return []
    else:
        return path(previous, previous[s])+[s]

def pathcost(path, step_costs):
    '''
    add up the step costs along a path, which is assumed to be a list output from the `path` function above
    '''
    cost = 0
    for s in range(len(path)-1):
        cost += step_costs[path[s]][path[s+1]]
    return cost


def depth_first(start, goal, state_graph, return_cost=False):
    ''' find a sequence of states from start to the goal '''
	
    dicta={}
    dicta[start] = None
    cityVisited=[start]
    que = deque([start])
    
    dict_result = {}
    
    dict_result = dfs_recurse(start, goal, state_graph, dicta, cityVisited, que) 
    #print(dict_result)
    #output the results
    path_list = path(dict_result, goal)
    #cost = pathcost(path_list, state_graph)
    
    if return_cost==True:
        return path_list
    else:
        return path_list
    
    
def dfs_recurse(start, goal, state_graph, dicta, cityVisited, que): 
#    print('que = ', que)
#    print('start = ', start)
#    print('dicta = ', dicta)
#    print('cityVisited = ', cityVisited)
    
    if start==goal:
        return dicta
    
    for k,v in state_graph[start].items():  #for loop exits once it runs out of items
        if k in cityVisited:
            continue
        else:
            cityVisited.append(k)
            que.append(k)
            dicta[k]=start            
    start = que.pop()        
    return dfs_recurse(start, goal, state_graph, dicta, cityVisited, que)
        

# Solution:
    

def maze_to_graph(maze):
    ''' takes in a maze as a numpy array, converts to a graph '''
    nrow = maze.shape[0]
    ncol = maze.shape[1]
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
    #print('d_maze = ', d_maze)               
    return d_maze
    

### Example for printing output
g_maze = maze_to_graph(maze)
print(g_maze, '\n')
x=maze_sol_dfs = depth_first((1,1), (10,10), g_maze)
print(x)
# print('Depth-first search yields: {}, ({} steps)'.format(maze_sol_dfs, len(maze_sol_dfs)))