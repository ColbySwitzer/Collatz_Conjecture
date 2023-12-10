import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

currentNum = 3
running = False

def onButtonClick():
    running = not running

def onClosing():
    window.destroy()

def collatzConjecture(a,b):
    permutations = 0
    while a != 1:
        if(a%2 == 0):
            a = a/2
            permutations = permutations + 1
        elif(a%2 != 0):
            a = a*3+1
            permutations = permutations + 1
    if(b == "n"):
        return a
    if(b == "p"):
        return permutations

def runCollatzConjecture():
    while(True):
        if(collatzConjecture(currentNum,"n") == 1):
            print(currentNum)
            print(collatzConjecture(currentNum,"p"))
            currentNum = currentNum + 1

window = tk.Tk()
window.title("Collatz Conjecture")
window.geometry("1200x675")

label = tk.Label(window, text="Text Field")
label.pack(pady = 10)

# window.protocol("VM_DELETE_WINDOW", onClosing)

window.mainloop()








        