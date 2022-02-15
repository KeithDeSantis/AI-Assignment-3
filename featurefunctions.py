
def identify_sector_of_agent(row, column, goal_row, goal_column):
    """
    Determines the sector which the agent is in relative to the goal
    :param row:
    :param column:
    :param goal_row:
    :param goal_column:
    :return:
    """

    top_left = "top_left"
    top_center = "top_center"
    top_right = "top_right"
    middle_left = "middle_left"
    middle_right = "middle_right"
    bottom_left = "bottom_left"
    bottom_center = "bottom_center"
    bottom_right = "bottom_right"
    in_center = "in_center"

    if row < goal_row - 1:

        if column < goal_column - 1:
            return top_left

        elif goal_column - 1 <= column and column <= goal_column + 1:
            return top_center

        elif column > goal_column + 1:
            return top_right

    elif goal_row - 1 <= row and row <= goal_row + 1:

        if column < goal_column - 1:
            return middle_left

        elif goal_column - 1 <= column and column <= goal_column + 1:
            return in_center

        elif column > goal_column + 1:
            return middle_right

    elif row > goal_row + 1:

        if column < goal_column - 1:
            return bottom_left

        elif goal_column - 1 <= column and column <= goal_column + 1:
            return bottom_center

        elif column > goal_column + 1:
            return bottom_right

def get_sector_cost(row, col, goal_row, goal_col, board):
    sector = identify_sector_of_agent(row, col, goal_row, goal_col)
    # check the cost near the goal based on location of robot
    if(sector is "top_left"):
        """
        [X][X][ ]
        [X][G][ ]
        [ ][ ][ ]
        """
        return board.get_cost(goal_row-1, goal_col-1) + board.get_cost(goal_row, goal_col-1) + board.get_cost(goal_row-1, goal_col)
    elif(sector is "top_center"):
        """
        [X][X][X]
        [ ][G][ ]
        [ ][ ][ ]
        """
        return board.get_cost(goal_row-1, goal_col-1) + board.get_cost(goal_row-1, goal_col+1) + board.get_cost(goal_row-1, goal_col)
    elif(sector is "top_right"):
        """
        [ ][X][X]
        [ ][G][X]
        [ ][ ][ ]
        """
        return board.get_cost(goal_row-1, goal_col) + board.get_cost(goal_row-1, goal_col+1) + board.get_cost(goal_row, goal_col+1)
    elif(sector is "middle_left"):
        """
        [X][ ][ ]
        [X][G][ ]
        [X][ ][ ]
        """
        return board.get_cost(goal_row-1, goal_col-1) + board.get_cost(goal_row, goal_col-1) + board.get_cost(goal_row+1, goal_col-1)
    elif(sector is "middle_right"):
        """
        [ ][ ][X]
        [ ][G][X]
        [ ][ ][X]
        """
        return board.get_cost(goal_row-1, goal_col+1) + board.get_cost(goal_row, goal_col+1) + board.get_cost(goal_row+1, goal_col+1)
    elif(sector is "bottom_left"):
        """
        [ ][ ][ ]
        [X][G][ ]
        [X][X][ ]
        """
        return board.get_cost(goal_row, goal_col-1) + board.get_cost(goal_row+1, goal_col-1) + board.get_cost(goal_row+1, goal_col)
    elif(sector is "bottom_center"):
        """
        [ ][ ][ ]
        [ ][G][ ]
        [X][X][X]
        """
        return board.get_cost(goal_row+1, goal_col-1) + board.get_cost(goal_row+1, goal_col) + board.get_cost(goal_row+1, goal_col+1)
    elif(sector is "bottom_right"):
        """
        [ ][ ][ ]
        [ ][G][X]
        [ ][X][X]
        """
        return board.get_cost(goal_row, goal_col+1) + board.get_cost(goal_row+1, goal_col) + board.get_cost(goal_row+1, goal_col+1)
    elif(sector is "in_center"):
        """
        [ ][ ][ ]
        [ ][G][ ]
        [ ][ ][ ]
        """
        return 0