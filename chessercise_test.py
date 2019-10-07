import argparse
import unittest
import sys

import chessercise

class TestChessMethods(unittest.TestCase):

    def test_parse_args(self):
        expected_position = 'a3'
        bad_position = 'a9'
        expected_function = 'can_king_move'
        
        position, movement_test = chessercise.parse_args(['-position', expected_position, '-piece', 'KING'])
        self.assertEqual(expected_position, position)
        self.assertEqual(expected_function, movement_test.__name__)
        
        with self.assertRaises(SystemExit):
            chessercise.parse_args(['-position', bad_position, '-piece', 'KING'])

    def test_coordinate_transform(self):
        expected_x = 1
        expected_y = 3
        expected_position = 'a3'
        self.assertEqual(expected_position, chessercise.coordinates_to_notation(expected_x, expected_y))
        x, y = chessercise.notation_to_coordinates(expected_position)
        self.assertEqual(expected_x, x)
        self.assertEqual(expected_y, y)



    def test_can_bishop_move(self):
        good = [[3, 3, 4, 2], [3, 4, 5, 2]] # Diagonal
        bad = [[3, 3, 4, 3], [3, 4, 4, 4]]  # Not diagonal
        for case in good:
            self.assertTrue(chessercise.can_bishop_move(*case))
        for case in bad:
            self.assertFalse(chessercise.can_bishop_move(*case))
        
    def test_can_horse_move(self):
        good = [[3, 3, 5, 2], [3, 4, 5, 5]] # Ls
        bad = [[3, 3, 4, 3], [3, 3, 4, 4]]  # Not Ls
        for case in good:
            self.assertTrue(chessercise.can_horse_move(*case))
        for case in bad:
            self.assertFalse(chessercise.can_horse_move(*case))
        
    def test_can_king_move(self):
        good = [[3, 3, 4, 2], [3, 4, 3, 5]] # 1 away
        bad = [[3, 3, 5, 3], [3, 3, 4, 1]]  # 2+ away
        for case in good:
            self.assertTrue(chessercise.can_king_move(*case))
        for case in bad:
            self.assertFalse(chessercise.can_king_move(*case))
        
    def test_can_queen_move(self):
        good = [[3, 3, 3, 7], [3, 4, 5, 2]] # Both rook and bishop moves
        bad = [[3, 3, 5, 2], [3, 4, 5, 5]]  # Horse moves
        for case in good:
            self.assertTrue(chessercise.can_queen_move(*case))
        for case in bad:
            self.assertFalse(chessercise.can_queen_move(*case))
        
    def test_can_rook_move(self):
        good = [[3, 3, 3, 7], [3, 3, 1, 3]] # Lines
        bad = [[3, 3, 4, 5], [3, 3, 2, 2]]  # Not lines
        for case in good:
            self.assertTrue(chessercise.can_rook_move(*case))
        for case in bad:
            self.assertFalse(chessercise.can_rook_move(*case))



    def test_get_valid_moves(self):
        position = 'a3'
        expected = {
            'bishop': ['c1', 'b2', 'b4', 'c5', 'd6', 'e7', 'f8'],
            'horse': ['b1', 'c2', 'c4', 'b5'],
            'king': ['a2', 'b2', 'b3', 'a4', 'b4'],
            'queen': ['a1', 'c1', 'a2', 'b2', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
                      'a4', 'b4', 'a5', 'c5', 'a6', 'd6', 'a7', 'e7', 'a8', 'f8'],
            'rook': ['a1', 'a2', 'b3', 'c3', 'd3', 'e3', 'f3', 
                     'g3', 'h3', 'a4', 'a5', 'a6', 'a7', 'a8'],
        }
        moves = {
            'bishop': chessercise.can_bishop_move,
            'horse': chessercise.can_horse_move,
            'king': chessercise.can_king_move,
            'queen': chessercise.can_queen_move,
            'rook': chessercise.can_rook_move,
        }

        for type in expected.keys():
            self.assertSequenceEqual(expected[type], chessercise.get_valid_moves(position, moves[type]))



if __name__ == '__main__':
    unittest.main()