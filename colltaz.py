import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

currentNum = 3
running = False


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

def onButtonClick():
    # running = not running
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 1, 4, 5]
    updatePlot(x,y)


def updatePlot(x,y):
    ax.clear()

    ax.scatter(x,y, label='Scatter Plot',color='blue',marker='o')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Scatter Plot Example')

    canvas.draw()

window = tk.Tk()
window.title("Collatz Conjecture")
window.geometry("1200x675")

label = tk.Label(window, text="Enter your name:")
label.pack(pady = 10)

entry = tk.Entry(window)
entry.pack(pady=10)

button = tk.Button(window, text="Click me", command=onButtonClick)
button.pack(pady=10)

fig, ax = plt.subplots()

canvas = FigureCanvasTkAgg(fig, master=window)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# window.protocol("VM_DELETE_WINDOW", onClosing)

window.mainloop()








        