class dataentry:
    def __init__(self, vertical_distance_to_goal, horizontal_distance_to_goal, direction, cost_to_goal):
        self.vertical_distance_to_goal = vertical_distance_to_goal
        self.horizontal_distance_to_goal = horizontal_distance_to_goal
        self.direction = direction
        self.cost_to_goal = cost_to_goal

    def __str__(self):
        string = "Vertical Distance to Goal: " + str(self.vertical_distance_to_goal) + "\n"
        string = string + "Horizontal Distance to Goal: " + str(self.horizontal_distance_to_goal) + "\n"
        string = string + "Direction: " + self.direction + "\n"
        string = string + "Cost to Goal: " + str(self.cost_to_goal)
        return string

    def to_list(self):
        numerical_direction = 0
        if self.direction == "north":
            numerical_direction = 1
        elif self.direction == "east":
            numerical_direction = 2
        elif self.direction == "south":
            numerical_direction = 3
        elif self.direction == "west":
            numerical_direction = 4
        return [self.vertical_distance_to_goal, self.horizontal_distance_to_goal, numerical_direction, self.cost_to_goal]