# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:22:32 2020

@author: stevensu
"""
from collections import OrderedDict
#from collections import deque
import heapq

map_distances = dict(
    chi=dict(det=283, cle=345, ind=182),
    cle=dict(chi=345, det=169, col=144, pit=134, buf=189),
    ind=dict(chi=182, col=176),
    col=dict(ind=176, cle=144, pit=185),
    det=dict(chi=283, cle=169, buf=256),
    buf=dict(det=256, cle=189, pit=215, syr=150),
    pit=dict(col=185, cle=134, buf=215, phi=305, bal=247),
    syr=dict(buf=150, phi=253, new=254, bos=312),
    bal=dict(phi=101, pit=247),
    phi=dict(pit=305, bal=101, syr=253, new=97),
    new=dict(syr=254, phi=97, bos=215, pro=181),
    pro=dict(bos=50, new=181),
    bos=dict(pro=50, new=215, syr=312, por=107),
    por=dict(bos=107))


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

# Solution:

class Frontier_PQ:
    ''' frontier class for uniform search, ordered by path cost '''
# add your code here
    def __init__(self, start, cost):
        heap0 = []
        state0 = OrderedDict()
        state0[start] = 0 
        heapq.heappush(heap0,(cost, start))
        self.state = state0
        self.heap = heap0
        
    def add(self, currentCity, cost):
        heapq.heappush(self.heap, (cost,currentCity))
        return
        
    def pop(self):
        (k,v) = heapq.heappop(self.heap)
        return (k,v)
    
    def replace(self, city, cost):
        for i in range(len(self.heap)):
            (k,v) = self.heap[i]
            if v==city:
                self.heap[i]= (cost, city)
                heapq.heapify(self.heap)
                break
            else:
                continue
                
        return    
# add your code here                    


def uniform_cost(start, goal, state_graph, return_cost=False):
# add your code here
    frontC = Frontier_PQ(start, 0) #declare Frontier_PQ class
    cityVisited = []  #cities which were expanded to get children
    currentCity = start
    previous = {start:None}
    
    print(frontC.heap)
    print(frontC.state)
#    print(cityVisited)
#    print(previous)
    
#    cost0, state0 = frontC.heap[0] #root of priority queue
    
    while len(frontC.heap): #while priority queue has elements 
         (cost0, city) = frontC.pop()
         currentCity = city
         
         if currentCity==goal:
             path_list = path(previous, goal)
             cost_min = cost0
             if return_cost==True:
                 return (path_list, cost_min)
             else:
                 return path_list
         else:
             for (k,v) in map_times[currentCity].items():
                 print('k,v = ', k,v)
                 if k == currentCity:
                     continue
                 else:
                     #cityVisited.append(k)  #is k visted yet? it will be added to the heap but not expanded
                     #previous[k]=currentCity  #is this correct??? no, we are at expanding the root's children
                     newCost = cost0 + v 
                     if( ((k in frontC.state)==True) and (frontC.state[k]>newCost) ):
                     #if( ((True)==True) and (True) ): 
                         print('branch 1')
                         frontC.replace(k,newCost)  #update with lower cost 
                         frontC.state[k]=newCost
                         previous[k]=currentCity
                     elif  ((k in frontC.state) != True):
                         print('branch 2')
                         frontC.add(k, newCost)
                         frontC.state[k]=newCost 
                         previous[k]=currentCity
                     else:
                         print('lower cost not found')
                         continue #don't put in priority queue
                         
                         
                         
                     print(k,' heap = ', frontC.heap)
                     print(k, 'state = ', frontC.state, '\n')
                     
         cityVisited.append(currentCity)      
         print('cityVisited = ', cityVisited)                                
         print(frontC.heap)    
         
         #frontC.pop()
         
        
    
    return -1 #error occurred or no soln found
    
# add your code here                

start = 'new'
goal = 'chi'
graph = map_times
print(uniform_cost(start, goal, graph, True))