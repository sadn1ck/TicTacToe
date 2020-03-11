import pygame
import sys
import tkinter as tk
from tkinter import ttk
from main import PvP
from main2 import PvC
win = tk.Tk()
win.geometry("180x50")
win.title("PvP | PvC")
def runPvP():
    PvP()
def runPvC():
    PvC()
pvpbutton = ttk.Button(win, text="PvP", command=runPvP)
pvpbutton.grid(column=0, row=0)
pvcbutton = ttk.Button(win, text="PvC", command=runPvC)
pvcbutton.grid(column=2, row=0)
win.resizable(False, False)
win.mainloop()