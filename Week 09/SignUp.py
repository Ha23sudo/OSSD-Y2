import tkinter as tk

def save_credentials():
    with open("credentials.txt", "a") as f:
        f.write(f"{username.get()}:{password.get()}\n")
 
    
def check_credentials():
    pass
    
    
def  signin_window():
    tk.Label(root, text="Login").pack()
    username=tk.Entry(root)
    username.pack()
    password=tk.Entry(root, show="*")
    password.pack()
    tk.Button(root, text="Sign In", command=check_credentials).pack()   
    tk.Button(root, text="Sign Up", command=save_credentials).pack()
    
root=tk.Tk()
root.title("Sign In")
root.geometry("300x300")
root.minsize(200,200)
root.minsize(600,600)
root.mainloop()