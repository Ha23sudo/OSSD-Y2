import tkinter as tk
from tkinter import messagebox


# File read Sign In function
def sign_in():

    user = username_entry.get()
    pwd = password_entry.get()

    try:
        with open("test.txt","r") as file:

            for line in file:
                u,p = line.strip().split(",")

                if user == u and pwd == p:
                    main_menu(user)
                    return

        messagebox.showerror(
            "Login Failed",
            "Incorrect username or password"
        )

    except:
        messagebox.showerror(
            "Error",
            "No registered users found"
        )


# File write Sign Up function
def sign_up():

    user = new_username.get()
    pwd = new_password.get()

    if user=="" or pwd=="":

        messagebox.showwarning(
            "Missing Data",
            "Enter all fields"
        )
        return

    with open("test.txt","a") as file:
        file.write(f"{user},{pwd}\n")

    messagebox.showinfo(
        "Success",
        "Account created"
    )

    sign_in_window()


# Clear current window
def clear_window():

    for widget in root.winfo_children():
        widget.destroy()


# sign in window
def sign_in_window():

    clear_window()

    tk.Label(
        root,
        text="Student Portal",
        font=("Arial",18,"bold"),
        fg="blue"
    ).pack(pady=10)

    tk.Label(
        root,
        text="Username"
    ).pack()

    global username_entry
    username_entry=tk.Entry(root,width=25)
    username_entry.pack(pady=5)

    tk.Label(
        root,
        text="Password"
    ).pack()

    global password_entry
    password_entry=tk.Entry(root,show="*",width=25)
    password_entry.pack(pady=5)

    tk.Button(
        root,
        text="Sign In",
        width=15,
        command=sign_in
    ).pack(pady=10)

    tk.Button(
        root,
        text="Create Account",
        command=sign_up_window
    ).pack()


# sign up window
def sign_up_window():

    clear_window()

    tk.Label(
        root,
        text="New Registration",
        font=("Arial",18,"bold"),
        fg="green"
    ).pack(pady=10)

    tk.Label(root,text="New Username").pack()

    global new_username
    new_username=tk.Entry(root)
    new_username.pack()

    tk.Label(root,text="New Password").pack()

    global new_password
    new_password=tk.Entry(root,show="*")
    new_password.pack()

    tk.Button(
        root,
        text="Register",
        command=sign_up
    ).pack(pady=10)

    tk.Button(
        root,
        text="Back",
        command=sign_in_window
    ).pack()


# main menu window
def main_menu(name):

    clear_window()

    tk.Label(
        root,
        text="Dashboard",
        font=("Arial",20,"bold"),
        fg="purple"
    ).pack(pady=10)

    tk.Label(
        root,
        text=f"Hello, {name}"
    ).pack(pady=10)

    tk.Button(
        root,
        text="Profile"
    ).pack(pady=5)

    tk.Button(
        root,
        text="Settings"
    ).pack(pady=5)

    tk.Button(
        root,
        text="Logout",
        bg="red",
        fg="white",
        command=sign_in_window
    ).pack(pady=10)



# root window
root=tk.Tk()

root.title("Student Portal")
root.geometry("350x300")

sign_in_window()

root.mainloop()