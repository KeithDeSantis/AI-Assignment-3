import copy
import logging
from threading import *
import csv
import os

import agent
import board
import math
import boardgenerator
from dataentry import dataentry
from time import *


def update_nums_through_move(row, column, direction, action, board_used):
    cost = None
    if action == "FORWARD":
        if direction == "north":
            row -= 1
        elif direction == "east":
            column -= 1
        elif direction == "south":
            row += 1
        elif direction == "west":
            column += 1
        cost = board_used.get_cost(row, column)
    elif action == "BASH":
        if direction == "north":
            row -= 1
        elif direction == "east":
            column -= 1
        elif direction == "south":
            row += 1
        elif direction == "west":
            column += 1
        cost = 3
    elif action == "LEFT":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        cost = math.ceil(board_used.get_cost(row,column) / 2)
    elif action == "RIGHT":
        if direction == "north":
            direction = "west"
        elif direction == "east":
            direction = "north"
        elif direction == "south":
            direction = "east"
        elif direction == "west":
            direction = "south"
        cost = math.ceil(board_used.get_cost(row, column) / 2)

    return [row, column, direction, cost]

def generate_data_from_path(board_used, actions, score, start, goal):
    dataentries = []

    curr_row = start[0]
    curr_column = start[1]
    direction = 'north'
    cost_so_far = 0

    for index in range(len(actions)):
        curr_dataentry = dataentry(0,0,0,0) # these values will be overwritten as they're calculated

        # Collect all feature data for this data entry, right now I only have these four
        curr_dataentry.vertical_distance_to_goal = abs(goal[0] - curr_row) # vert distance
        curr_dataentry.horizontal_distance_to_goal = abs(goal[1] - curr_column) # horiz distance
        curr_dataentry.direction = direction # direction
        curr_dataentry.cost_to_goal = (100 - score) - cost_so_far # cost to goal

        # Update variables for the next action being taken
        actionTaken = actions[index]
        updated_values = update_nums_through_move(curr_row, curr_column, direction, actionTaken, board_used)
        curr_row = updated_values[0]
        curr_column = updated_values[1]
        direction = updated_values[2]
        cost_so_far += updated_values[3]

        # Add the data entry to the list of entries
        dataentries.append(curr_dataentry)

    # This creates the final dataentry, for the goal state we've reached
    curr_dataentry = dataentry(0, 0, 0, 0)  # these values will be overwritten as they're calculated
    curr_dataentry.vertical_distance_to_goal = abs(goal[0] - curr_row)
    curr_dataentry.horizontal_distance_to_goal = abs(goal[1] - curr_column)
    curr_dataentry.direction = direction
    curr_dataentry.cost_to_goal = 0

    dataentries.append(curr_dataentry)

    return dataentries

def write_to_csv(dataset):
    fields = ["Vertical Distance to Goal", "Horizontal Distance to Goal", "Direction", "Cost To Goal"]
    rows = []
    for data in dataset:
        rows.append(data.to_list())

    filename = "output.csv"
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)

def main2(heuristic_number, time_to_run):
    all_data = []
    start = time()

    boardnumber = 0

    while time() - start < time_to_run:
        print(str(boardnumber))
        boardgenerator.generate_board(5, boardnumber)

        board_filename = "board" + str(boardnumber) + ".txt"

        b = board.Board(board_filename)
        a = agent.Agent(b.get_start(), b.get_goal(), b)
        a_star = a.a_star(heuristic_number)

        data = generate_data_from_path(b, a_star[3][::-1][1:], a_star[0], b.get_start(), b.get_goal())

        for d in data:
            all_data.append(d)

        boardnumber += 1

        os.remove(board_filename)
    print("done")
    write_to_csv(all_data)

def main(filename, heuristic_number):
    """
    Main function.
    :return: 1 on success and 0 on failure.
    """

    # Create a board
    b = board.Board(filename)
    print(b)
    # Create an agent
    a = agent.Agent(b.get_start(), b.get_goal(), b)
    # print(a)
    start = perf_counter()
    a_star = a.a_star(heuristic_number)
    end = perf_counter()
    # print(f"Time taken:{end - start}")
    print(f"Score:{a_star[0]}")
    print(f"Number of actions:{a_star[1]}")
    print(f"Nodes expanded:{a_star[2]}")
    print(f"Actions:")
    for action in a_star[3][::-1][1:]:
        print(f"\t{action.lower()}")

if __name__ == "__main__":
    #main("board-6x6.txt", 5)
    main2(7,3)
