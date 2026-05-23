import tkinter as tk
from tkinter import messagebox

CREDENTIALS_FILE = "credentials.txt"


class SignApp:
    def __init__(self, root):
        self.root = root
        root.title("Sign In")
        root.geometry("320x240")

        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack(expand=True, fill="both")

        tk.Label(frame, text="Username").pack(anchor="w")
        self.username = tk.Entry(frame)
        self.username.pack(fill="x")

        tk.Label(frame, text="Password").pack(anchor="w", pady=(8, 0))
        self.password = tk.Entry(frame, show="*")
        self.password.pack(fill="x")

        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Sign In", width=12, command=self.check_credentials).grid(row=0, column=0, padx=6)
        tk.Button(btn_frame, text="Sign Up", width=12, command=self.save_credentials).grid(row=0, column=1, padx=6)

        self.message_label = tk.Label(frame, text="")
        self.message_label.pack(pady=6)

    def save_credentials(self):
        u = self.username.get().strip()
        p = self.password.get().strip()
        if not u or not p:
            messagebox.showwarning("Input required", "Please enter both username and password.")
            return
        try:
            with open(CREDENTIALS_FILE, "a") as f:
                f.write(f"{u}:{p}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save credentials: {e}")
            return
        self.message_label.config(text="Sign up successful", fg="green")
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)

    def check_credentials(self):
        u = self.username.get().strip()
        p = self.password.get().strip()
        if not u or not p:
            messagebox.showwarning("Input required", "Please enter both username and password.")
            return
        try:
            with open(CREDENTIALS_FILE, "r") as f:
                credentials = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            credentials = []

        if f"{u}:{p}" in credentials:
            self.message_label.config(text="Login Successful", fg="green")
        else:
            self.message_label.config(text="Login Failed", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = SignApp(root)
    root.mainloop()
