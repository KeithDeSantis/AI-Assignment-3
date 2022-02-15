
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
    bottom_center = "bottom_middle"
    bottom_right = "bottom_right"
    in_center = "in_center"

    if row < goal_row - 1:

        if column < goal_column - 1:
            return top_left

        elif goal_column - 1 < column and column < goal_column + 1:
            return top_center

        elif column > goal_column + 1:
            return top_right

    elif goal_row - 1 < row and row < goal_row + 1:

        if column < goal_column - 1:
            return middle_left

        elif goal_column - 1 < column and column < goal_column + 1:
            return in_center

        elif column > goal_column + 1:
            return middle_right

    elif row > goal_row + 1:

        if column < goal_column - 1:
            return bottom_left

        elif goal_column - 1 < column and column < goal_column + 1:
            return bottom_center

        elif column > goal_column + 1:
            return bottom_right