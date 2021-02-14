from django.shortcuts import render
from itertools import product
import math
class knight:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance
    
    
def knight_bfs(curr_pos, target_pos, N):
    
    visited = [[False for i in range(N)] for j in range(N)]
    queue = []
    queue.append(knight(curr_pos[0], curr_pos[1], 0))
    visited[curr_pos[0]][curr_pos[1]] = True
    
    while (len(queue) > 0):
        top = queue.pop(0)
        
        for next_position in knight_moves(top, N):
            if visited[next_position[0]][next_position[1]] == False:
                queue.append(knight(next_position[0], next_position[1], top.distance + 1))
                visited[next_position[0]][next_position[1]] = True
            
            if tuple(next_position) == tuple(target_pos):
                return top.distance + 1
    
    return math.inf


def knight_moves(position, N):
    x = position.x
    y = position.y
    moves = list(product([x-1, x+1], [y-2, y+2])) + list(product([x-2, x+2], [y-1, y+1]))
    moves = [(x,y) for [x, y] in moves if x >= 0 and y >= 0 and x < N  and y < N]
    return moves        
