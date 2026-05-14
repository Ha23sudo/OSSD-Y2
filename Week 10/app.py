import tkinter as tk
from tkinter import messagebox


# File read Sign In function
def sign_in():
    username = entry_username.get()
    password = entry_password.get()

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()

        for user in users:
            saved_user, saved_pass = user.strip().split(",")

            if username == saved_user and password == saved_pass:
                messagebox.showinfo("Success", "Login Successful!")
                main_menu(username)
                return

        messagebox.showerror("Error", "Invalid Username or Password")

    except FileNotFoundError:
        messagebox.showerror("Error", "No users found. Please sign up first.")


# File write Sign Up function
def sign_up():
    username = entry_username.get()
    password = entry_password.get()

    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

    messagebox.showinfo("Success", "Account Created Successfully!")


# sign in window
def sign_in_window():
    clear_window()

    tk.Label(root, text="Sign In").pack()

    global entry_username, entry_password

    tk.Label(root, text="Username").pack()
    entry_username = tk.Entry(root)
    entry_username.pack()

    tk.Label(root, text="Password").pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    tk.Button(root, text="Sign In", command=sign_in).pack()
    tk.Button(root, text="Go to Sign Up", command=sign_up_window).pack()


# sign up window
def sign_up_window():
    clear_window()

    tk.Label(root, text="Sign Up").pack()

    global entry_username, entry_password

    tk.Label(root, text="Username").pack()
    entry_username = tk.Entry(root)
    entry_username.pack()

    tk.Label(root, text="Password").pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    tk.Button(root, text="Sign Up", command=sign_up).pack()
    tk.Button(root, text="Go to Sign In", command=sign_in_window).pack()


# main menu window
def main_menu(username):
    clear_window()
    tk.Label(root, text=f"Welcome {username}", font=("Arial", 16)).pack(pady=50)


# clear screen function
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# root window
root = tk.Tk()
root.title("Application")
root.geometry("300x200")

sign_in_window()

root.mainloop()