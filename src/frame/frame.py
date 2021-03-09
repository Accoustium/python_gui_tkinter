import tkinter as tk


class Frame:
    def __init__(self, title: str):
        self.Title = title

    def __repr__(self):
        return f"TabFrame({self.title})"

    def __str__(self):
        return str(self.__repr__())
