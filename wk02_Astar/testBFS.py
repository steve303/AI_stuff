# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:26:10 2020

@author: stevensu
"""
from collections import deque
from collections import OrderedDict
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
    #print(previous)
    
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
    

def breadth_first(start, goal, state_graph, return_cost=False):
 #add your code here
    cityVisited = [start]
    que = deque([])  #fifo queue for bfs
    dicta = {}  #used to keep track of parent-maps child to parent; used in path() function
    dicta[start] = None  #initialize the start city with None as parent  
    
    for k,v in map_distances[start].items():  #"prime the pump" initialize the lists and que
        cityVisited.append(k)
        que.append(k)
        dicta[k]=start
 
    #print(lista)
    #print(cityVisited)
    #print(sorted(lista))
    #print(dicta)
    
    while len(que): 
        next = que.popleft()
        #print('next = ', next)
        if next == goal:  # the "true" branch will exit since goal is found
            break
        else:  #the "false" branch continues the BFS by expanding frontier nodes
           
            for k,v in map_distances[next].items():  # k are the frontier nodes
               
                if k in cityVisited:
                    continue  #bypass the current city, k, since it is already processed
                else: #put in que and cityVisited
                    cityVisited.append(k)
                    que.append(k)
                    dicta[k]=next
                    
                                   
    #output the results
    path_list = path(dicta, goal)
    cost = pathcost(path_list, map_distances)
    if return_cost==True:
        return (path_list,cost) 
    else:
        return path_list
   
    
 #add your code here

#breadth_first('chi','pit',map_distances,True)
#path,cost = breadth_first('chi','bos',map_distances,True)
path_list, cost = breadth_first('por','ind',map_distances,True)
print(path_list)
print(cost)