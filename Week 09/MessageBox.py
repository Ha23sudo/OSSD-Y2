import tkinter as tk
from tkinter import messagebox


def _with_hidden_root(func, *args, **kwargs):
    """Ensure a Tk root exists for messagebox; create a hidden one if needed.

    This lets the functions be imported and used without creating a visible
    main window at import time.
    """
    root = tk._default_root
    created = False
    if not root:
        root = tk.Tk()
        root.withdraw()
        created = True
    try:
        return func(*args, **kwargs)
    finally:
        if created:
            root.destroy()


def info(title, msg):
    return _with_hidden_root(messagebox.showinfo, title, msg)


def warning(title, msg):
    return _with_hidden_root(messagebox.showwarning, title, msg)


def error(title, msg):
    return _with_hidden_root(messagebox.showerror, title, msg)


def ask_yes_no(title, msg):
    return _with_hidden_root(messagebox.askyesno, title, msg)


def ask_ok_cancel(title, msg):
    return _with_hidden_root(messagebox.askokcancel, title, msg)


def ask_retry_cancel(title, msg):
    return _with_hidden_root(messagebox.askretrycancel, title, msg)


def _launch_demo():
    root = tk.Tk()
    root.title("Message Box Demo")
    root.geometry("320x260")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(expand=True, fill="both")

    tk.Button(frame, text="Info", width=24, command=lambda: info("Info", "This is an info message")).pack(pady=6)
    tk.Button(frame, text="Warning", width=24, command=lambda: warning("Warning", "This is a warning message")).pack(pady=6)
    tk.Button(frame, text="Error", width=24, command=lambda: error("Error", "This is an error message")).pack(pady=6)
    tk.Button(frame, text="Ask Yes/No", width=24, command=lambda: print('Answer:', ask_yes_no("Question", "Do you agree?"))).pack(pady=6)
    tk.Button(frame, text="Ask Ok/Cancel", width=24, command=lambda: print('Answer:', ask_ok_cancel("Confirm", "Proceed?"))).pack(pady=6)
    tk.Button(frame, text="Ask Retry/Cancel", width=24, command=lambda: print('Answer:', ask_retry_cancel("Retry", "Retry operation?"))).pack(pady=6)
    tk.Button(frame, text="Close", width=24, command=root.destroy).pack(pady=6)

    root.mainloop()


if __name__ == "__main__":
    _launch_demo()







