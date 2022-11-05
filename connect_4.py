import numpy as np

ROW_SIZE = 6
COL_SIZE = 7


def create_board():
    return np.zeros((6, 7))


def game_over():
    return False


def is_valid_selection(board, col):
    if 0 <= col <= 6:
        if board[-1][col] == 0:
            return True


def position_in_col(board, col):
    for i in range(ROW_SIZE):
        if board[i][col] == 0:
            return i


def drop_coin(board, row, col, player_number):
    board[row][col] = player_number


def print_board(board):
    print(np.flip(board, 0))


def check_position(board, row, col, player_number):
    return board[row][col] == player_number


def check_upward(board, row, col, player):
    list_of_positions = 0
    new_row = row + 1
    while new_row < ROW_SIZE:
        if check_position(board, new_row, col, player):
            list_of_positions += 1
        else:
            break
        new_row += 1
    return list_of_positions


def check_downward(board, row, col, player):
    list_of_positions = 0
    new_row = row - 1
    while 0 <= new_row:
        if check_position(board, new_row, col, player):
            list_of_positions += 1
        else:
            break
        new_row -= 1
    return list_of_positions


def check_left(board, row, col, player):
    list_of_positions = 0
    new_col = col - 1
    while 0 <= new_col:
        if check_position(board, row, new_col, player):
            list_of_positions += 1
        else:
            break
        new_col -= 1
    return list_of_positions


def check_right(board, row, col, player):
    list_of_positions = 0
    new_col = col + 1
    while 0 <= new_col < COL_SIZE:
        if check_position(board, row, new_col, player):
            list_of_positions += 1
        else:
            break
        new_col += 1
    return list_of_positions


def check_diagonal_north_east(board, row, col, player):
    list_of_positions = 0
    new_row = row - 1
    new_col = col + 1

    while 0 <= new_col < COL_SIZE and 0 <= new_row < ROW_SIZE:
        if check_position(board, new_row, new_col, player):
            list_of_positions += 1
        else:
            break
        new_row -= 1
        new_col += 1
    return list_of_positions


def check_diagonal_south_west(board, row, col, player):
    list_of_positions = 0
    new_row = row + 1
    new_col = col - 1

    while 0 <= new_col < COL_SIZE and 0 <= new_row < ROW_SIZE:
        if check_position(board, new_row, new_col, player):
            list_of_positions += 1
        else:
            break
        new_row += 1
        new_col -= 1
    return list_of_positions


def check_diagonal_east_south(board, row, col, player):
    list_of_positions = 0
    new_row = row - 1
    new_col = col - 1
    while 0 <= new_col < COL_SIZE and 0 <= new_row < ROW_SIZE:
        if check_position(board, new_row, new_col, player):
            list_of_positions += 1
        else:
            break
        new_row -= 1
        new_col -= 1
    return list_of_positions


def check_diagonal_north_west(board, row, col, player):
    list_of_positions = 0
    new_row = row + 1
    new_col = col + 1
    while 0 <= new_col < COL_SIZE and 0 <= new_row < ROW_SIZE:
        if check_position(board, new_row, new_col, player):
            list_of_positions += 1
        else:
            break
        new_row +=1
        new_col += 1

    return list_of_positions

def is_winning_move(board, row, col, player):

    list_of_positions_horizontal = 1 + check_upward(board, row, col, player) + check_downward(board, row, col, player)

    list_of_positions_vertical = 1 + check_left(board, row, col, player) + check_right(board, row, col, player)

    list_of_positions_north_east_to_south_west = 1+ check_diagonal_north_east(board, row, col, player) + \
                                                 check_diagonal_south_west(board, row, col, player)

    list_of_positions_south_east_to_north_west = 1 + check_diagonal_east_south(board, row, col,player) + \
                                                 check_diagonal_north_west(board, row, col, player)
    print(f"player :{player} number of points horitzontal: {list_of_positions_horizontal}")
    print(f"player :{player} number of points vertical: {list_of_positions_vertical}")
    print(f"player :{player} number of points check_diagonal_north_east: {check_diagonal_north_east(board, row, col, player)}")
    print(f"player :{player} number of points check_diagonal_south_west: {check_diagonal_south_west(board, row, col, player)}")
    print(
        f"player :{player} number of points check_diagonal_east_south: {check_diagonal_east_south(board, row, col, player)}")
    print(f"player :{player} number of points check_diagonal_north_west: {check_diagonal_north_west(board, row, col, player)}")
    if list_of_positions_horizontal >= 4 or list_of_positions_vertical >= 4 or list_of_positions_north_east_to_south_west >= 4 or list_of_positions_south_east_to_north_west >=4:
        return True
    return False


if __name__ == "__main__":
    board = create_board()
    turn = 0

    while not game_over():
        if turn % 2 == 0:
            player_1_selection = int(input("please input the selection for player1: "))
            turn += 1
            if is_valid_selection(board, player_1_selection):
                row = position_in_col(board, player_1_selection)
                drop_coin(board, row, player_1_selection, 1)
                if is_winning_move(board, row, player_1_selection, 1):
                    print("player1 wins")

        elif turn % 2 != 0:
            player_2_selection = int(input("please input the selection for player2: "))
            turn += 1
            if is_valid_selection(board, player_2_selection):
                row = position_in_col(board, player_2_selection)
                drop_coin(board, row, player_2_selection, 2)
                if is_winning_move(board, row, player_2_selection, 2):
                    print("player2 wins")

        print_board(board)
