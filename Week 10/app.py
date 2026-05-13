import tkinter as tk
from tkinter import messagebox
# File read Sign In function

def sign_in():
     
    username = username_entry.get()
    password = password_entry.get()

    try:
        file = open("users.txt", "r")
        users = file.readlines()
        file.close()

        for user in users:
            data = user.strip().split(",")

            if username == data[0] and password == data[1]:
                messagebox.showinfo("Success", "Sign In Successful")
                return

        messagebox.showerror("Error", "Invalid Username or Password")

    except FileNotFoundError:
        messagebox.showerror("Error", "No users found. Please Sign Up first")
    
    
    
# File write Sign Up function

def sign_up():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Warning", "Fields cannot be empty")
        return

    file = open("users.txt", "a")
    file.write(username + "," + password + "\n")
    file.close()

    messagebox.showinfo("Success", "Account Created Successfully")
    
    
    

#sign in window

def sign_in_window():
    global username_entry
    global password_entry

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Sign In", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="$")
    password_entry.pack()

    tk.Button(root, text="Sign In", command=sign_in).pack(pady=5)

    tk.Button(root, text="Go to Sign Up", command=sign_up_window).pack()
    


#sign up window

def sign_up_window():
    global username_entry
    global password_entry

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Sign Up", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Sign Up", command=sign_up).pack(pady=5)

    tk.Button(root, text="Go to Sign In", command=sign_in_window).pack()
    
    
    

# main menu window

def main_menu():
    pass

# root window
root = tk.Tk()
root.title("Application")
root.geometry("300x200")
sign_in_window()

root.mainloop()



            


