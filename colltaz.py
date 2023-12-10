import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

currentNum = 3
running = False
sequence = []
numbers = []

def collatzConjecture(a):
    permutations = 0
    global sequence
    global numbers
    numbers.append(a)
    while a != 1:
        if(a%2 == 0):
            a = a/2
            permutations += 1
        elif(a%2 != 0):
            a = a*3+1
            permutations += 1
    sequence.append(permutations)

def onRunButtonClick():
    global running

    running = not running

    if running:
        runCollatzConjecture()

def updatePlot(x,y):
    ax.clear()

    ax.scatter(x,y, label='Collatz Sequence',color='blue',marker='o')

    ax.set_xlabel('Current Number')
    ax.set_ylabel('Value')
    ax.set_title('Collatz Sequence Graph')

    canvas.draw()

def windowFunction():
    window = tk.Tk()
    window.title("Collatz Conjecture")
    window.geometry("1200x675")

    label = tk.Label(window, text="Enter your number:")
    label.pack(pady = 10)

    entry = tk.Entry(window)
    entry.pack(pady=10)

    runButton = tk.Button(window, text="Run", command=onRunButtonClick)
    runButton.pack(pady=10)

    fig, ax = plt.subplots()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    window.mainloop()

# windowFunction()

for i in range(3,10):
    collatzConjecture(i)

print(numbers)
print(sequence)






        