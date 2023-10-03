#
# DO NOT FORGET TO ADD COMMENTS!!!
# assignment: programming assignment 5
# author: Ethan Liu
# date: 3/17/2023
# file: game.py
# input: mouse clicks
# output: puzzle game
from tkinter import *
import tkinter.font as font
from fifteen import Fifteen

def update(pos):
    tiles.update(tiles.tiles[pos])

    a= ''
    for i in range(len(btn_tiles)):
        if tiles.tiles[i] != 0:
            btn_tiles[i].set(tiles.tiles[i])
            gui.nametowidget(i).configure(bg='orange')
        else:
            gui.nametowidget(i).configure(bg='white')
            btn_tiles[i].set(a)


def shuffle():
    tiles.shuffle()

    for i in range(len(btn_tiles)):
        if tiles.tiles[i] != 0:
            btn_tiles[i].set(tiles.tiles[i])
            gui.nametowidget(str(i)).configure(background='orange')
        else:
            btn_tiles[i].set("")
            gui.nametowidget(str(i)).configure(background='white')


def buttons(pos, val, tilevars, font):
    a = StringVar()
    tilevars.append(a)
    if val == 0:
        background = 'white'
    else:
        background = 'orange'
    button = Button(gui, textvariable=a, name=str(pos), bg=background, fg='black', height=3, width=5,
                    command=lambda: update(pos), font=font)
    if val == 0:
        a.set(str(""))
    else:
        a.set(str(val))

    return button


if __name__ == '__main__':

    # make tiles
    tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')

    btn_tiles = []
    col = 0
    row = 0
    for i in range(len(tiles.tiles)):
        button = buttons(i, tiles.tiles[i], btn_tiles, font)

        # the key argument name is used to identify the button
        #gui.nametowidget(str(i)).configure(background='orange')

        button.grid(row=row, column=col)

        col += 1
        if col >= tiles.size:
            row += 1
            col = 0

    # update the window
    shuffle_button = Button(gui, text="Shuffle", bg='orange', fg='black', height=3, width=10, command=lambda: shuffle())
    shuffle_button.grid(row=5, column=1, columnspan=2)

    gui.mainloop()