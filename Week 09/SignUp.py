import tkinter as tk
from tkinter import messagebox

# ---------------- SAVE USER ----------------
def save_test():
    user = signup_username.get()
    email = signup_email.get()
    password = signup_password.get()

    if user == "" or email == "" or password == "":
        messagebox.showerror("Error", "Fill all fields")
        return

    with open("test.txt", "a") as f:
        f.write(f"{user},{password}\n")

    messagebox.showinfo("Success", "Signup Successful")

    signin_window()


# ---------------- CHECK LOGIN ----------------
def check_test():
    user = login_username.get()
    password = login_password.get()

    try:
        with open("test.txt", "r") as f:

            for line in f:
                u, p = line.strip().split(",")

                if user == u and password == p:
                    home_window(user)
                    return

        messagebox.showerror("Error", "Invalid Username or Password")

    except FileNotFoundError:
        messagebox.showerror("Error", "No account found")


# ---------------- LOGIN WINDOW ----------------
def signin_window():

    clear_window()

    tk.Label(root,
             text="Login",
             font=("Arial",25,"bold")).pack(pady=10)

    tk.Label(root,text="Username").pack()

    global login_username
    login_username = tk.Entry(root)
    login_username.pack()

    tk.Label(root,text="Password").pack()

    global login_password
    login_password = tk.Entry(root,show="*")
    login_password.pack()

    tk.Button(root,
              text="Login",
              command=check_test).pack(pady=8)

    tk.Button(root,
              text="Go To Signup",
              command=signup_window).pack()


# ---------------- SIGNUP WINDOW ----------------
def signup_window():

    clear_window()

    tk.Label(root,
             text="Signup",
             font=("Arial",25,"bold")).pack(pady=10)

    tk.Label(root,text="Username").pack()

    global signup_username
    signup_username=tk.Entry(root)
    signup_username.pack()

    tk.Label(root,text="Email").pack()

    global signup_email
    signup_email=tk.Entry(root)
    signup_email.pack()

    tk.Label(root,text="Password").pack()

    global signup_password
    signup_password=tk.Entry(root,show="*")
    signup_password.pack()

    tk.Button(root,
              text="Signup",
              command=save_test).pack(pady=8)

    tk.Button(root,
              text="Back to Login",
              command=signin_window).pack()


# ---------------- HOME PAGE ----------------
def home_window(name):

    clear_window()

    tk.Label(root,
             text=f"Welcome {name}",
             font=("Arial",22,"bold")).pack(pady=20)

    tk.Button(root,text="Option 1").pack(pady=5)

    tk.Button(root,text="Option 2").pack(pady=5)

    tk.Button(root,
              text="Logout",
              command=signin_window).pack(pady=10)


# ---------------- CLEAR WINDOW ----------------
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# ---------------- MAIN ----------------
root=tk.Tk()

root.title("Login System")

root.geometry("350x400")

signin_window()

root.mainloop()