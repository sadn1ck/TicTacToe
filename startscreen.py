import pygame
import sys
import time
import tkinter as tk
from tkinter import ttk
from main import PvP
from main2 import PvC
win = tk.Tk()
win.title("PvP | PvC")
def runPvP():
    PvP()
def runPvC():
    PvC()
pvpbutton = ttk.Button(win, text="PvP", command=runPvP)
pvpbutton.grid(column=0, row=0)
pvcbutton = ttk.Button(win, text="PvC", command=runPvC)
pvcbutton.grid(column=1, row=0)
win.mainloop()