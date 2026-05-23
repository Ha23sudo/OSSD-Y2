import tkinter as tk
count=0

def increment():
    global count
    count+=1
    counter.config(text=str(count))

def decrement():
    global count
    count-=1
    counter.config(text=str(count))

def reset():
    global count
    count=0
    counter.config(text=str(count))


root = tk.Tk()
root.geometry("400x400")
counter=tk.Label(root, text="0")
counter.pack()
increment_button=tk.Button(root, text="Increment", command=increment)
increment_button.pack()
decrement_button=tk.Button(root, text="Decrement", command=decrement)
decrement_button.pack()
reset_button=tk.Button(root, text="Reset", command=reset)
reset_button.pack()
root.mainloop()



















