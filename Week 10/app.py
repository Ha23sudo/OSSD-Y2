import tkinter as tk
from tkinter import messagebox

# File read Sign In function

def sign_in(name,pas):
    username=name.get()
    password=pas.get()
    if not username and not password:
        messagebox.showerror("Error","Fields can't be empty!")
        return
    try:
        with open("cred.txt", "r") as file:
            content = file.read()
            # Check if the credentials exist in the file text
            if f"{username},{password}\n" in content:
                main_menu(username)
            else:
                messagebox.showerror("Error", "Wrong username or password!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No accounts exist yet. Please Sign Up!")
    

#Clear Function
def clear():
    for widget in root.winfo_children():
        widget.destroy()





# File write Sign Up function

def sign_up(name,pas):
    
    username=name.get()
    password=pas.get()
    if not username or not password:
        messagebox.showerror("Error", "Fields can't be empty!")
        return
    with open("cred.txt", "a") as file:
        file.write(f"{username},{password}\n")
        
    messagebox.showinfo("Success", "Signup successful!")
    sign_in_window()
    
    
    
    
    

#sign in window

def sign_in_window():
    clear()
    tk.Label(root, text="Login",font=("Arial",16)).pack()
    
    tk.Label(root, text="Username").pack()
    name_entry = tk.Entry(root)
    name_entry.pack(pady=2)
    
    tk.Label(root, text="Password").pack()
    pas_entry = tk.Entry(root, show="*")
    pas_entry.pack(pady=2)
    
    tk.Button(root, text="Login", command=lambda: sign_in(name_entry, pas_entry)).pack()
    tk.Button(root, text="Go to Signup", command=sign_up_window).pack()
    


#sign up window

def sign_up_window():
    clear()
    tk.Label(root, text="Signup",font=("Arial",16)).pack()

    tk.Label(root, text="Username").pack()
    name_entry=tk.Entry(root)
    name_entry.pack(pady=2)

    tk.Label(root, text="Password").pack()
    pas_entry=tk.Entry(root, show="*")
    pas_entry.pack(pady=2)

    tk.Button(root, text="Login", command=lambda: sign_up(name_entry, pas_entry)).pack()
    tk.Button(root, text="Go to Signup", command=sign_in_window).pack()
    
    
    

# main menu window

def main_menu(name):
    clear()
    tk.Label(root, text= f"Welcome, {name}" , font=("Arial",16)).pack(pady=15)
    tk.Button(root, text="Option 1").pack(pady=5)
    tk.Button(root, text="Option 2").pack(pady=5)
    tk.Button(root, text="Logout", command=sign_in_window).pack(pady=15)
    

# root window
root = tk.Tk()
root.title("Application")
root.geometry("300x300")
sign_in_window()

root.mainloop()



            


