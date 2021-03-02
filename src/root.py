import tkinter as tk
from frame.frame import Frame


class Root:
    def __init__(self, title: str, frame: Frame = None):
        self.Title = title
        self.App = tk.Tk()
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

    def run(self):
        self.App.mainloop()
