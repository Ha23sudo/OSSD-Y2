import tkinter as tk
# File read Sign In function

def sign_in():
    pass    
    
    
    
# File write Sign Up function

def sign_up():
    pass
    
    
    

#sign in window

def sign_in_window():
    tk.Label(root,text="enter your username").pack(pady=10)
    username=tk.Entry(root)
    username.pack(pady=10)
    tk.Label(root,text="enter your password").pack()
    password=tk.Entry(root,show="*")
    password.pack(pady=10)
    submit=tk.Button(root,text="sign-in",command=sign_in)
    submit.pack(pady=10)
    sign=tk.Button(root,text="sign-up",command=sign_up_window)
    sign.pack(pady=10)


#sign up window

def sign_up_window():
    tk.Label(root,text="enter your username").pack(pady=10)
    usernames=tk.Entry(root)
    usernames.pack(pady=10)
    tk.Label(root,text="enter your password").pack()
    passwords=tk.Entry(root,show="*")
    passwords.pack(pady=10)
    tk.Label(root,text="enter your email").pack()
    email=tk.Entry(root)
    email.pack(pady=10)
    done=tk.Button(root,text="sign-up",command=sign_up)
    done.pack(pady=10)
    signin=tk.Button(root,text="Sign-in",command=sign_in_window)
    signin.pack(pady=10)
# main menu window

def main_menu():
    tk.Label(root,text=f"welcome {username.get()}").pack(pady=10)
    tk.Button(root,text="btn 1").pack(pady=10)
    tk.Button(root,text="btn 2").pack(pady=10)
    tk.Button(root,text="btn 3").pack(pady=10)
    logout=tk.Button(root,text="logout",command=sign_in_window)
    logout.pack(pady=10)

# root window
root = tk.Tk()
root.title("Application")
root.geometry("300x200")
root.minsize(200,200)
root.maxsize(600,600)
root.configure(bg="black")
sign_in_window()

root.mainloop()



            


