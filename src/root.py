import tkinter as tk
from .frame.frame import Frame


class Root:
    def __init__(self, title: str, frame: Frame = None):
        self.Window = tk.Tk()
        self.update_title(title)
        if frame is None:
            self.Frame = Frame('Base')
        else:
            if isinstance(frame, Frame):
                self.Frame = frame
            else:
                raise TypeError("Frame attribute entered not a Frame class.")

    def __repr__(self):
        return f"RootApplication({self.Title})"

    def __str__(self):
        return str(self.__repr__())

    def update_title(self, title: str):
        self.__dict__['Title'] = title
        self.Window.title(title)

    def run(self):
        self.Window.mainloop()


class Login:
    user: str
    psword: str

    def __init__(self):
        self.Window = tk.Tk()
        self.Window.title("Login")

        self.user_var = tk.StringVar()
        self.ps_var = tk.StringVar()

        self.user_label = tk.Label(self.Window, text="Username").grid(column=0, row=0)
        self.user_variable = tk.Entry(self.Window, textvariable=self.user_var, width=30).grid(column=1, row=0)
        self.pass_label = tk.Label(self.Window, text="Password").grid(column=0, row=1)
        self.pass_variable = tk.Entry(self.Window, textvariable=self.ps_var, width=30).grid(column=1, row=1)
        self.submit_btn = tk.Button(self.Window, command=self.populate_password, text="Login", height=2, width=20).grid(column=3)

    def __repr__(self):
        return "LoginWindow()"

    def get(self):
        return self.user, self.psword

    def populate_password(self):
        self.user = self.user_var.get()
        self.psword = self.ps_var.get()
