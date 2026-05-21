from scrapper import get_cars_data
import tkinter as tk
from tkinter import ttk
# improve the user interface creatively and use other widgets as well.
def set_textarea(data):
    textarea.delete(1.0, tk.END)
    for car in data:
        textarea.insert(tk.END, f"Name: {car['name']}, Price: {car['price']}\n")

root=tk.Tk()
root.title("Car Price Scraper")
root.geometry("600x400")

#Step 1
car_manufact=['toyota', 'honda', 'suzuki']

dropdown=ttk.Combobox(root, values=car_manufact)

dropdown.current(2)
dropdown.pack(pady=20)
search_button=tk.Button(root, text="Search",command=lambda: set_textarea(get_cars_data(dropdown.get())))
search_button.pack(pady=10)
textarea=tk.Text(root, height=25, width=60)
textarea.pack(pady=20)




root.mainloop()






