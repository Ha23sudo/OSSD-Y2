import tkinter as tk
count=0

def increment():
    global count
    count+=1
    counter.config(text=str(count))


root = tk.Tk()

counter=tk.Label(root, text="0").pack()
incremet=tk.Button(root, text="Increment").pack()
decrement=tk.Button(root, text="Decrement").pack()
reset=tk.Button(root, text="Reset").pack()




















