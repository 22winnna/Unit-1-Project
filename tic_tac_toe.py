#!/usr/bin/env python3
# Project 1D: Quarterly Sales

# grids
grid = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

turn = 'x'

# win combination
win_com = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],
           [1,4,7],[2,5,8],[3,6,9],[3,5,7]]

# displays welcome message
def main():
    print(grid[0][0], grid[0][1], grid[0][2])
    print(grid[1][0], grid[1][1], grid[1][2])
    print(grid[2][0], grid[2][1], grid[2][2])
print("Welcome to Tic Tac Toe")

# print grids
def show():
    print()
    print("+---+---+---+")
    print("|" ,grid[0][0], "|" ,grid[0][1], "|" ,grid[0][2], "|")
    print("+---+---+---+")
    print("|" ,grid[1][0], "|" ,grid[1][1], "|" ,grid[1][2], "|")
    print("+---+---+---+")
    print("|" ,grid[2][0], "|" ,grid[2][1], "|" ,grid[2][2], "|")
    print("+---+---+---+")

# list in lists for grids
full_grid = [[grid[0][0]], [grid[0][1]], [grid[0][2]], [grid[1][0]], [grid[1][1]], [grid[1][2]], [grid[2][0]], [grid[2][1]], [grid[2][2]]]

# pick a row and a column
while True:
    show()
    if turn == 'x':
        print("X's turn")
        row_choice = int(input("Pick a row (1,2,3): "))
        if row_choice < 1 or row_choice > 3:
            print("Try again.")
            
        column_choice = int(input("Pick a column (1,2,3): "))
        if column_choice < 1 or column_choice > 3:
            print("Try again.")
        else:
            grid[row_choice - 1][column_choice - 1] = "x"
        
        x_win = 0
        # check for x win
        if grid[0][0] == "x" and grid[0][1] == "x" and grid[0][2] == "x":
            x_win = 1
        if grid[1][0] == "x" and grid[1][1] == "x" and grid[1][2] == "x":
            x_win = 1
        if grid[2][0] == "x" and grid[2][1] == "x" and grid[2][2] == "x":
            x_win = 1
        if grid[0][0] == "x" and grid[1][1] == "x" and grid[2][2] == "x":
            x_win = 1
        if grid[0][0] == "x" and grid[1][0] == "x" and grid[2][0] == "x":
            x_win = 1
        if grid[0][1] == "x" and grid[1][1] == "x" and grid[2][1] == "x":
            x_win = 1
        if grid[0][2] == "x" and grid[1][2] == "x" and grid[2][2] == "x":
            x_win = 1
        if grid[0][2] == "x" and grid[1][1] == "x" and grid[2][0] == "x":
            x_win = 1
        if x_win == 1: 
            print("X wins!")
            print()
            print("Game over!")
            break

    # change turn to o
        turn = 'o'
        continue
    # if turn is o:
    if turn == 'o':
        print("O's turn")
        row_choice = int(input("Pick a row (1,2,3): "))
        if row_choice < 1 or row_choice > 3:
            print("Try again.")

        column_choice = int(input("Pick a column (1,2,3): "))
        if column_choice < 1 or column_choice > 3:
            print("Try again.")
        else:
            grid[row_choice - 1][column_choice - 1] = "o"

        o_win = 0
        # check for o win
        if grid[0][0] == "o" and grid[0][1] == "o" and grid[0][2] == "o":
            o_win = 1
        if grid[1][0] == "o" and grid[1][1] == "o" and grid[1][2] == "o":
            o_win = 1
        if grid[2][0] == "o" and grid[2][1] == "o" and grid[2][2] == "o":
            o_win = 1
        if grid[0][0] == "o" and grid[1][1] == "o" and grid[2][2] == "o":
            o_win = 1
        if grid[0][0] == "o" and grid[1][0] == "o" and grid[2][0] == "o":
            o_win = 1
        if grid[0][1] == "o" and grid[1][1] == "o" and grid[2][1] == "o":
            o_win = 1
        if grid[0][2] == "o" and grid[1][2] == "o" and grid[2][2] == "o":
            o_win = 1
        if grid[0][2] == "o" and grid[1][1] == "o" and grid[2][0] == "o":
            o_win = 1
        if o_win == 1:
            print("O wins!")
            print()
            print("Game over!")
            break

        turn = 'x'
        continue