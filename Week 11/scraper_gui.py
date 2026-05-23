from scrapper import get_cars_data
import tkinter as tk
from tkinter import ttk
# improve the user interface creatively and use other widgets as well.
def set_textarea(data):
    textarea.delete(1.0, tk.END)
    
    if not data:
        textarea.insert(tk.END, "  No results found.")
        return
    
    textarea.insert(tk.END, f"  {'NAME':<45} {'PRICE':>20}\n")
    textarea.insert(tk.END, "  " + "─" * 65 + "\n")
    
    for i, car in enumerate(data):
        name  = car['name'].strip()
        price = car['price'].strip()
        bg = "#f0f0f0" if i % 2 == 0 else "#ffffff"
        textarea.insert(tk.END, f"  {name:<45} {price:>20}\n", f"row{i}")
        textarea.tag_configure(f"row{i}", background=bg)


root = tk.Tk()
root.title("Car Price Scraper")
root.geometry("600x460")
root.configure(bg="#f5f5f5")

#Step 1
car_manufact=['toyota', 'honda', 'suzuki']

dropdown=ttk.Combobox(root, values=car_manufact)

dropdown.current(2)
dropdown.pack(pady=20)
search_button=tk.Button(root, text="Search",command=lambda: set_textarea(get_cars_data(dropdown.get())))
search_button.pack(pady=10)
textarea=tk.Text(root, height=25, width=70)
textarea.pack(pady=20)



root.mainloop()