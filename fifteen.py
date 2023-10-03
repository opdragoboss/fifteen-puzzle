#
# DO NOT FORGET TO ADD COMMENTS!!!
# assignment: programming assignment 5
# author: Ethan Liu
# date: 3/17/2023
# file: fifteen.py
# input: tile number
# output: puzzle game graph
import numpy as np
from random import choice
from graph import Graph


class Fifteen:
    def __init__(self, size=4):
        self.size = size
        self.tiles = np.array([i for i in range(1, size ** 2)] + [0])
        self.adjacency = [[1, 4], [0, 2, 5], [1, 3, 6], [2, 7],
                          [0, 5, 8], [1, 4, 6, 9], [2, 5, 7, 10], [3, 6, 11],
                          [4, 9, 12], [5, 8, 10, 13], [6, 9, 11, 14], [7, 10, 15],
                          [8, 13], [9, 12, 14], [10, 13, 15], [11, 14]]
        self.board = Graph()
        for i in range(len(self.adjacency)):
            for j in self.adjacency[i]:
                self.board.addEdge(i, j)

    def update(self, move):
        if not self.is_valid_move(move):
            return
        self.transpose(0, move)

    # Swaps two tiles given tile number
    def transpose(self, i, j):
        i = np.where(self.tiles == i)
        j = np.where(self.tiles == j)
        temp = self.tiles[i]
        self.tiles[i] = self.tiles[j]
        self.tiles[j] = temp

    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice(self.adjacency[index])
            self.tiles[index], self.tiles[move_index] = self.tiles[move_index], self.tiles[index]
            index = move_index

    def is_valid_move(self, move):
        empty = np.where(self.tiles == 0)[0][0]
        emptytile = self.board.getVertex(empty)
        a = False
        move_index = np.where(self.tiles == move)[0][0]

        for i in emptytile.getConnections():
            if i.getId() == move_index:
                a = True
        return a

    def is_solved(self):
        isSolved = True
        for i in range(self.size ** 2 - 1):

            if self.tiles[i] != i + 1:
                isSolved = False
        for i in range(self.size ** 2 - 2, -1, -1):
            if self.tiles[i] != i + 1:
                isSolved = False
        return isSolved
    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):

        b = 0
        count = 0
        size = self.size
        while b < size:
            a = 0
            cstr = "|"
            print("+---+---+---+---+")
            while a < size:
                if self.tiles[count] != 0:
                    if len(str(self.tiles[count])) <= 1:
                        cstr += f" {self.tiles[count]} |"
                    else:
                        cstr += f"{self.tiles[count]} |"
                else:
                    cstr += "   |"
                a += 1
                count += 1
            print(cstr)
            b += 1
        print("+---+---+---+---+")

    def __str__(self):

        row = 0
        count = 0
        tile_str = ""
        while row < self.size:
            col = 0
            col_str = ""
            while col < self.size:
                if self.tiles[count] != 0:
                    if len(str(self.tiles[count])) <= 1:
                        col_str += f" {self.tiles[count]} "
                    else:
                        col_str += f"{self.tiles[count]} "
                else:
                    col_str += "   "
                col += 1
                count += 1
            col_str += "\n"
            tile_str += col_str
            row += 1
        return tile_str


if __name__ == '__main__':
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False

    '''You should be able to play the game if you uncomment the code below'''
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        print(game)
        game.draw()
        if game.is_solved():
            break
    print('Game over!')