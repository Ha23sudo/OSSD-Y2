import tkinter as tk
root=tk.Tk()
def sign_in():
    global username,password
    user=username.get()
    pas=password.get()
    with open("file.txt","r")as f:
        for line in f:
            data=line.strip().split(":")
            if data[0]==user and data[1]==pas:
                main_menu(user)
            else:
                messegebox.showwarning("! Invalid username & Password ")

def sign_up():
    global usernames,passwords,emails
    u=usernames.get()
    p=passwords.get()
    e=emails.get()
    if u=="" or p=="":
        messegebox.showwarning("enter a valid username and password")
    else:
        with open("file.txt","a")as f:
            f.write(f"{u}:{p}:{e}\n")
            sign_in_window()
   


def sign_up_window():
    global usernames,passwords,emails
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root,text="enter your email").pack()
    emails=tk.Entry(root)
    emails.pack()
    tk.Label(root,text="enter your username").pack()
    usernames=tk.Entry(root)
    usernames.pack()
    tk.Label(root,text="enter your password").pack()
    passwords=tk.Entry(root)
    passwords.pack()
    signup=tk.Button(root,text="sign_up",command=sign_up)
    signup.pack()
    signin=tk.Button(root,text="Login",command=sign_in_window)
    signin.pack()

def sign_in_window():
    for widget in root.winfo_children():
        widget.destroy()
    global username,password
    tk.Label(root,text="enter your username ").pack()
    username=tk.Entry(root)
    username.pack()
    tk.Label(root,text="enter your password").pack()
    password=tk.Entry(root)
    password.pack()
    log=tk.Button(root,text="sign_in",command=sign_in)
    log.pack()
    up=tk.Button(root,text="sign_up",command=sign_up_window)
    up.pack()

def main_menu(name):
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root,text=f"welcome user {name}").pack()
    btn1=tk.Button(root,text="btn 1")
    btn1.pack()
    btn2=tk.Button(root,text="btn 2")
    btn2.pack()
    btn3=tk.Button(root,text="btn 3")
    btn3.pack()
    logout=tk.Button(root,text="log-out",command=sign_in_window)
    logout.pack()


root.geometry("400x400")
root.maxsize(600,600)
sign_in_window()
root.mainloop()







