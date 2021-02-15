from itertools import product
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from .config import *
import math
import json


class knight:
    def __init__(self, x, y, distance):
        self._x = x
        self._y = y
        self._distance = distance
        
    def get_distance(self):
        return self._distance
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
  

@csrf_exempt
def knight_game(request):
    N, curr_position, target_position = request_inputes(request)
    if is_valid_position(curr_position, N) and is_valid_position(target_position, N):
        return HttpResponse(knight_bfs(curr_position, target_position, N))
    else:
        return HttpResponse(status=400)


def request_inputes(request):
    body_utf = request.body.decode('utf-8')
    body = json.loads(body_utf)
    curr_pos = []
    target_pos = []
    N = body["N"] 
    
    curr_pos_x = body["knight_position_x"] - 1
    curr_pos_y = body["knight_position_y"] - 1
    
    target_pos_x = body["knight_targetPosition_x"] - 1
    target_pos_y = body["knight_targetPosition_y"] - 1
    
    curr_pos.extend((curr_pos_x, curr_pos_y))
    target_pos.extend((target_pos_x, target_pos_y))
    return (N, curr_pos, target_pos)


def is_valid_position(position, N):
    return (position[X_INDEX] >= 0 and position[Y_INDEX] >= 0 and position[X_INDEX] < N and position[Y_INDEX] < N) 


def knight_bfs(curr_pos, target_pos, N):
    visited = [[False for i in range(N)] for j in range(N)]
    queue = []
    queue.append(knight(curr_pos[X_INDEX], curr_pos[Y_INDEX], 0))
    visited[curr_pos[X_INDEX]][curr_pos[Y_INDEX]] = True
    
    if tuple(curr_pos) == tuple(target_pos):
        return 0
    
    while (len(queue) > 0):
        top = queue.pop(0)
        top_adjacent_distance = top.get_distance() + 1
          
        for next_position in knight_moves(top, N):
            if tuple(next_position) == tuple(target_pos):
                return top_adjacent_distance
            
            if visited[next_position[0]][next_position[1]] == False:
                queue.append(knight(next_position[X_INDEX], next_position[Y_INDEX], top_adjacent_distance))
                visited[next_position[X_INDEX]][next_position[Y_INDEX]] = True

    return math.inf


def knight_moves(position, N):
    x = position.get_x()
    y = position.get_y()
    moves = list(product([x-1, x+1], [y-2, y+2])) + list(product([x-2, x+2], [y-1, y+1]))
    moves = [(x,y) for [x, y] in moves if is_valid_position([x, y], N)]
    return moves
