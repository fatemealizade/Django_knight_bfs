from django.test import TestCase
from .views import knight_bfs, knight_game
from django.test import Client
import json

class KnightTestClass(TestCase):
    
    def setUp(self):
        self.client = Client()
    
    def test_knight_bfs_n_6_curr_pos_4_5_target_pos_1_1(self):
        response = knight_bfs([3, 4],[0, 0], 6)
        self.assertEquals(response, 3)
    
    def test_knight_bfs_n_6_curr_pos_1_1_target_pos_6_6(self):
        response = knight_bfs([0, 0], [5, 5], 6)
        self.assertEquals(response, 4)
        
    def test_knight_bfs_current_pos_equal_target_pos(self):
        response = knight_bfs([0, 0], [0, 0], 5)
        self.assertEquals(response, 0)
    
    def test_knight_game_negative_curr_pos(self):
        knight_bfs_dict = {
            "N" : 6,
            "knight_position_x":-1,
            "knight_position_y":1,
            "knight_targetPosition_x":6,
            "knight_targetPosition_y":6
            }
        response = self.client.post(path='/shortestpath/',
                                    data=json.dumps(knight_bfs_dict),
                                    content_type="application/json")
        self.assertEquals(response.status_code, 400)
        
    def test_knight_game_curr_pos_out_of_chess_board(self):
        knight_bfs_dict = {
            "N" : 6,
            "knight_position_x":7,
            "knight_position_y":1,
            "knight_targetPosition_x":6,
            "knight_targetPosition_y":6
            }
        response = self.client.post(path='/shortestpath/',
                                    data=json.dumps(knight_bfs_dict),
                                    content_type="application/json")
        self.assertEquals(response.status_code, 400)
        
    def test_knight_game_negative_target_pos(self):
        knight_bfs_dict = {
            "N" : 6,
            "knight_position_x":7,
            "knight_position_y":1,
            "knight_targetPosition_x":-7,
            "knight_targetPosition_y":6
            }
        response = self.client.post(path='/shortestpath/',
                                    data=json.dumps(knight_bfs_dict),
                                    content_type="application/json")
        self.assertEquals(response.status_code, 400)
    
    def test_knight_game_target_pos_out_of_chess_board(self):
        knight_bfs_dict = {
            "N" : 6,
            "knight_position_x":7,
            "knight_position_y":1,
            "knight_targetPosition_x":10,
            "knight_targetPosition_y":6
            }
        response = self.client.post(path='/shortestpath/',
                                    data=json.dumps(knight_bfs_dict),
                                    content_type="application/json")
        self.assertEquals(response.status_code, 400)