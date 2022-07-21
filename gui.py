from cProfile import label
from cgitb import text
from curses import window
from sqlite3 import Row
from tkinter import *


def click():
    inputText = textEntry.get()

window = Tk()
window.title("Birth year calculator")
window.config(background="black", height=100, width=100)

Label (window, text="Please enter your birth year: ", bg="yellow").grid(row = 0, column = 0)
textEntry = Entry(window, width="20", bg="yellow")
textEntry.grid(row=0, column=4)

Button(window, text="submit ", width=8, bg="yellow", command=click).grid( row= 1, column = 4)

window.mainloop()