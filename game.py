# author: Milad Taimuri
# date: March 17, 2023
# file: game.py a Python program that implements a fifteen puzzle game
# input: user responses with widgets
# output: interactive fifteen puzzle game with gui window and use of dfs and bfs


from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
          




# function to handle button clicks
def clickButton(button):
    # get the name of the button
    name = int(button)
    # update the puzzle
    tiles.update(name)
    # redraw the puzzle
    for i, t in enumerate(tiles.tiles):
        text = StringVar()
        text.set(str(t))
        name = str(t)
        # change the color of the empty tile
        if t == 0:
            gui.nametowidget(name).configure(bg='white')
        else:
            gui.nametowidget(name).configure(bg='coral')
        # add buttons to the window
        # use .grid() or .pack() methods
        button_obj = gui.nametowidget(name)
        button_obj.grid(row=i//tiles.size, column=i%tiles.size)
def shuffle():
    # shuffle the tiles
    tiles.shuffle()
    # redraw the puzzle
    for i, t in enumerate(tiles.tiles):
        text = StringVar()
        if t == 0:
            text.set('')
        else:
            text.set(str(t))
        name = str(t)
        button = Button(gui, textvariable=text, name=name,
            bg='white', fg='black', font=font, height=2, width=5,
            command = lambda button=name: clickButton(button))
        # change the color of the empty tile
        if t == 0:
            button.configure(bg='white')
        else:
            button.configure(bg='coral')
        # add buttons to the window
        # use .grid() or .pack() methods
        button.grid(row=i//tiles.size, column=i%tiles.size)


if __name__ == '__main__':
    # make tiles
    tiles = Fifteen()
    # make a window
    gui = Tk()
    gui.title("Fifteen")
    # make font
    font = font.Font(family='Helvetica', size='25', weight='bold')
    # make buttons
    for i, t in enumerate(tiles.tiles):
        text = StringVar()
        if t == 0:
            text.set('')
        else:
            text.set(str(t))
        name = str(t)
        button = Button(gui, textvariable=text, name=name,
            bg='white', fg='black', font=font, height=2, width=5,
            command = lambda button=name: clickButton(button))
        # the key argument name is used to identify the button
        gui.nametowidget(name).configure(bg='coral')
        # add buttons to the window
        # use .grid() or .pack() methods
        button.grid(row=i//tiles.size, column=i%tiles.size)
    # add shuffle button
    shuffle_button = Button(gui, text='Shuffle', bg='white', fg='black', font=font, height=2, width=5, command=shuffle)
    shuffle_button.grid(row=tiles.size, column=0, columnspan=tiles.size)
    # update the window
    gui.mainloop()
