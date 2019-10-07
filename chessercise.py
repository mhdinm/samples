import argparse
import sys

# A mapping from letter to corresponding location integer
algebraic = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8,
    1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h",
}

def parse_args(input_args):
    pieces = {
        "BISHOP": can_bishop_move,
        "KING": can_king_move,
        "KNIGHT": can_horse_move,
        "QUEEN": can_queen_move,
        "ROOK": can_rook_move,
    }

    # Help check inputs for correctness
    valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    valid_algebraic_positions = []
    for letter in valid_letters:
        for number in range(1, 9):
            valid_algebraic_positions.append(letter + str(number))

    # Actually parse the args
    parser = argparse.ArgumentParser()
    parser.add_argument('-piece', type=str, required=True, choices=pieces.keys(), help="The chess piece name")
    parser.add_argument('-position', type=str, required=True, choices=valid_algebraic_positions, help="Chess algebraic notation position; a3, b7, etc.")
    args = parser.parse_args(input_args)

    return args.position, pieces[args.piece]



def get_valid_moves(position, movement_test):
    # For each position, check to see if piece can move to it
    results = []
    x, y = notation_to_coordinates(position)
    for test_y in range(1, 9):
        for test_x in range(1, 9):
            if movement_test(x, y, test_x, test_y):
                results.append(coordinates_to_notation(test_x, test_y))

    # For clean code everywhere else, remove the current position from the results
    if position in results:
        results.remove(position)
    return results



# Go from "a3" to (1, 3)
def notation_to_coordinates(position):
    return algebraic[position[0]], int(position[1])

# Go from (1, 3) to "a3"
def coordinates_to_notation(x, y):
    return algebraic[x] + str(y)



# As long as both X and Y change the same (diagonal), bishop can move
def can_bishop_move(from_x, from_y, to_x, to_y):
    return abs(to_x - from_x) == abs(to_y - from_y)

# Is it a 2x1 L shape from _ to _?
def can_horse_move(from_x, from_y, to_x, to_y):
    return ( abs(to_x - from_x) == 2 and abs(to_y - from_y) == 1 or 
             abs(to_x - from_x) == 1 and abs(to_y - from_y) == 2 )

# Move up to one spot any direction for king
def can_king_move(from_x, from_y, to_x, to_y):
    return abs(to_x - from_x) <= 1 and abs(to_y - from_y) <= 1

# Queens move exactly like a rook *and* a bishop
def can_queen_move(from_x, from_y, to_x, to_y):
    return ( can_rook_move(from_x, from_y, to_x, to_y) or 
             can_bishop_move(from_x, from_y, to_x, to_y) )

# As long as either X or Y doesn't change (line), rook can move
def can_rook_move(from_x, from_y, to_x, to_y):
    return to_x - from_x == 0 or to_y - from_y == 0



if __name__ == '__main__': 
    position, movement_test = parse_args(sys.argv[1:])
    result = get_valid_moves(position, movement_test)
    print(', '.join(result))
