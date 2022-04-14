import tkinter as tk
from configurations import *
from GUIsegments import GUIsegments


class SessionGUI(GUIsegments):
    def __init__(self, window):
        GUIsegments(window=window, segments_path=SESSION_GUI_SEGMENT_PATH)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('New Tournament')
    # root.geometry('400x400')
    SessionGUI(root)
    root.mainloop()
