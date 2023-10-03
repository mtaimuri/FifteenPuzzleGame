# author: Milad Taimuri
# date: March 17, 2023
# file: game.py a Python program that implements a fifteen puzzle game
# input: user responses with widgets
# output: interactive fifteen puzzle game with gui window and use of dfs and bfs


# import numpy and choice from random
import numpy as np
from random import choice

class Fifteen:
    # sets self.tiles to an array with a 4x4 layout of the 15 puzzle game
    # and made a nested list of all adjaceney for self.tiles
    def __init__(self, size = 4):
        self.size = size
        self.tiles = np.array([i for i in range(1,self.size**2)] + [0])
        self.adj = [[1, 4], [0, 2, 5], [1, 3, 6], [2, 7],
                    [0, 5, 8], [1, 4, 6, 9], [2, 5, 7, 10], [3, 6, 11],
                    [4, 9, 12], [5, 8, 10, 13], [6, 9, 11, 14], [7, 10, 15],
                    [8, 13], [9, 12, 14], [10, 13, 15], [11, 14]]

        
    # shuffles self.tiles in whatever amount step is set to
    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice(self.adj[index])
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index
        
    # checks if the index of is adjacent to the index of the move    
    def is_valid_move(self, move):
        index = np.where(self.tiles == 0)[0][0]
        move_index = np.where(self.tiles == move)[0][0]
        if (move_index) in self.adj[index]:
            return True
        else:
            return False
    # first checks if the move is valid with the previous function
    # and than swaps the number with each indices    
    def update(self, move):
        if self.is_valid_move(move) == True:
            index = np.where(self.tiles == 0)[0][0]
            move_index = np.where(self.tiles == move)[0][0]
            self.tiles[move_index], self.tiles[index] = self.tiles[index], self.tiles[move_index]
        else:
            return False

    # checks if self.tile is back in order, and if is than it solved(true) and returns false if not solved
    def is_solved(self):
        solved_puzzle = np.array([i for i in range(1,self.size**2)] + [0])
        return np.all(self.tiles == solved_puzzle)
    
    # use enumerate to sort the self.tile and allow it to be drawed
    def draw(self):
        print('+---+---+---+---+')
        for i, t in enumerate(self.tiles):
            if i % self.size == 0:
                print('|', end='')
            if t == 0:
                print('   ', end='|')
            elif t < 10:
                print(f' {t} ', end='|')
            else:
                print(f'{t} ', end='|')
            if (i+1) % self.size == 0:
                print('\n+---+---+---+---+')

        
    # returns self.tiles as a string    
    def __str__(self):
        str_tile = ""
        for i in range(self.size):
            row = self.tiles[i*self.size:(i+1)*self.size]
            str_r = ""
            for t in row:
                if t == 0:
                    str_r += "   "
                else:
                    if t >= 10:
                        str_r += f"{t:2d} "
                    else:
                        str_r += f"{t:2d} "
            str_tile += str_r + "\n"
        return str_tile

    

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
        game.draw()
        if game.is_solved():
            break
    print('Game over!')

    
        
