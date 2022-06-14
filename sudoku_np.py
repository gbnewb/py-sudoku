import numpy as np


def parse(raw: str):
    if len(raw) != 81:
        raise ValueError('The length of the raw sudoku string is not 81!')
    board = np.zeros((9, 9), dtype=np.int8)
    i = 0
    for y in range(9):
        for x in range(9):
            if raw[i] != '.':
                board[y, x] = int(raw[i])
            i += 1
    return board          

              
def str_3x3(array):
    return '\n'.join([' '.join([str(num or '-') for num in row]) for row in array])


def check_print(board):
    if not validator(board):
        print('The board is not valid!')
    print(str_3x3(board))
    
          
def point_validator(board, point):
        """check if the given point is valid in the Sudoku object

        Args:
            point (tuple): a (x,y) coordinate

        Returns:
            True or False
        """
        y, x = point
        value = board[y, x]
        if value:
            board[y, x] = 0
            row = board[y]
            column = board[:, x]
            subgrid = [board[i, j] for i in range(y//3*3, y//3*3+3) for j in range(x//3*3, x//3*3+3)]
            if (value in row) or (value in column) or (value in subgrid):
                board[y, x] = value
                return False
        board[y, x] = value
        return True


def validator(board):
        valid_items = np.arange(10)
        if len(board) != 9:
            return False
        else:
            for x_axis in board:
                if len(x_axis) != 9:
                    return False
                for item in x_axis:
                    if item not in valid_items:
                        return False
        for y in range(9):
            for x in range(9):
                if not point_validator(board, (y, x)):
                    return False
        return True
    

def attempt(board, algorithm='BackTracking'):
        unfilled = [(i, j) for i in range(9) for j in range(9) if board[i, j] == 0]
        
        if algorithm == 'BackTracking':
            back_tracking_count = 0
            trash = {}
            trash_full = {}
            i = 0
            y, x = unfilled[i]
            [trash.setdefault(point, set()) for point in unfilled]
            [trash_full.setdefault(point, set(range(1, 10))) for point in unfilled]
                
            while trash != trash_full:
                back_tracking_count += 1
                board[y, x] += 1
                trash[unfilled[i]].add(board[y, x])
                if point_validator(board, (y, x)):
                    if i == len(unfilled) - 1:
                        return board, back_tracking_count
                    i += 1
                    y, x = unfilled[i]
                else:
                    while board[y, x] == 9:
                        board[y, x] = 0
                        i -= 1
                        y, x = unfilled[i]
            return board