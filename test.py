# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title('PanedWindow Demo')
# root.geometry('300x200')

# # change style to classic (Windows only)
# # to show the sash and handle
# style = ttk.Style()
# style.theme_use('classic')

# # paned window
# pw = ttk.PanedWindow(orient=tk.HORIZONTAL)

# # Left listbox
# # left_list = tk.Listbox(root)
# # left_list.pack(side=tk.LEFT)
# mn = ttk.Notebook(root)
# frame1 = tk.Frame(root)
# frame2 = tk.Frame(root)
# mn.add(frame1, text='tab1')
# mn.add(frame2, text='tab2')
# pw.add(mn)

# # Right listbox
# right_list = tk.Listbox(root)
# right_list.pack(side=tk.LEFT)
# pw.add(right_list)

# # place the panedwindow on the root window
# pw.pack(fill=tk.BOTH, expand=True)

# root.mainloop()

# **************************************************************************

# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog


# class Tab:
#     def __init__(self, notebook: ttk.Notebook):
#         self.filename = None
#         self.notebook = notebook

#         self.text_widget = tk.Text(self.notebook)
#         self.text_widget.bind("<Control-o>", self.open)
#         self.text_widget.bind("<Control-s>", self.save)
#         self.text_widget.bind("<Control-Shift-S>", self.saveas)
#         self.notebook.add(self.text_widget, text="The tab name")

#     def open(self, _=None):
#         filename = filedialog.askopenfilename()
#         if filename != "":
#             with open(filename, "r") as file:
#                 data = file.read()
#             self.text_widget.delete("0.0", "end")
#             self.text_widget.insert("end", data)
#             self.filename = filename
#         return "break"

#     def save(self, _=None):
#         if self.filename is None:
#             self.saveas()
#         else:
#             self._save()
#         return "break"

#     def saveas(self, _=None):
#         filename = filedialog.asksaveasfilename()
#         if filename == "":
#             return "break"
#         self.filename = filename
#         self._save()

#     def _save(self):
#         assert self.filename is not None, "self.filename shouldn't be None"
#         data = self.text_widget.get("0.0", "end")
#         with open(self.filename, "w") as file:
#             file.write(data)


# class App:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.new_tab_button = tk.Button(
#             self.root, text="New tab", command=self.add_new_tab)
#         self.new_tab_button.pack()
#         self.open_button = tk.Button(
#             self.root, text="Open file", command=self.open_file)
#         self.open_button.pack()
#         self.save_button = tk.Button(
#             self.root, text="Save file", command=self.save_file)
#         self.save_button.pack()
#         self.notebook = ttk.Notebook(self.root)
#         self.notebook.pack()
#         self.tabs = []

#     def add_new_tab(self):
#         tab = Tab(self.notebook)
#         self.tabs.append(tab)

#     def get_current_tab(self):
#         # This code gets the currently selected tab
#         idx = self.notebook.index(self.notebook.select())
#         tab = self.tabs[idx]
#         return tab

#     def open_file(self):
#         tab = self.get_current_tab()
#         tab.open()  # Call `open` on the tab

#     def save_file(self):
#         tab = self.get_current_tab()
#         tab.save()  # Call `save` on the tab

#     def mainloop(self):
#         self.root.mainloop()


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


# ***************************************************************************
# from time import time
# from tkinter import Tk, Menu, Text
# from tkinter.ttk import Notebook
# from tkinter.filedialog import askopenfile


# text_list = []


# def add_tab(parent, contents, name):
#     text = Text()
#     text_list.append(text)
#     text = text_list[len(text_list) - 1]

#     parent.add(text, text=name)
#     text.insert('end', contents)


# def open_file():
#     file = askopenfile(filetypes=[('Text file', '*.txt')])

#     if file:
#         add_tab(notebook, file.read(), file.name.split('/')[-1])


# root = Tk()

# menu_bar = Menu(root)

# file_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label='File', menu=file_menu)
# file_menu.add_command(label='Open', command=open_file)

# root.config(menu=menu_bar)

# notebook = Notebook(width=700, height=500)
# notebook.pack()

# root.mainloop()

# ***************************************************

# from tkinter import *
# from tkinter import ttk
# # Create an instance of tkinter frame or window
# win = Tk()
# # Set the geometry of tkinter frame
# win.geometry("750x250")
# # Define a new function to open the window


# def open_win():
#     new = Toplevel(win)
#     new.geometry("750x250")
#     new.title("New Window")
#     # Create a Label in New window
#     Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold')).pack(pady=30)


# # Create a label
# Label(win, text="Click the below button to Open a New Window",
#       font=('Helvetica 17 bold')).pack(pady=30)
# # Create a button to open a New Window
# ttk.Button(win, text="Open", command=open_win).pack()
# win.mainloop()

# *******************************************************************************


# from tkinter import *

# top = Tk()

# top.geometry("200x250")

# lbl = Label(top, text="A list of favourite countries...")

# listbox = Listbox(top)

# listbox.insert(1, "India")

# listbox.insert(2, "USA")

# listbox.insert(3, "Japan")

# listbox.insert(4, "Austrelia")

# # this button will delete the selected item from the list

# btn = Button(top, text="delete",
#              command=lambda listbox=listbox: listbox.delete(ANCHOR))

# lbl.pack()


# listbox.pack()

# btn.pack()
# top.mainloop()


#  *************************************************************************


# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()

# canvas1 = tk.Canvas(root, width=300, height=300)
# canvas1.pack()


# def ExitApplication():
#     MsgBox = tk.messagebox.askquestion(
#         'Exit Application', 'Are you sure you want to exit the application', icon='warning')
#     if MsgBox == 'yes':
#         root.destroy()
#     else:
#         tk.messagebox.showinfo(
#             'Return', 'You will now return to the application screen')


# button1 = tk.Button(root, text='Exit Application',
#                     command=ExitApplication, bg='brown', fg='white')
# canvas1.create_window(150, 150, window=button1)

# root.mainloop()


# ****************************************************************************************

# from os import listdir
# from os.path import isfile, join
# mypath = '.\Agents'
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(onlyfiles)

# ****************************************************************************************
# import os
# from os import listdir
# from os.path import isfile, join

# path = '.\Domains'
# preference_paths = []
# domain_lists = (name for name in os.listdir(path))
# for dir in domain_lists:
#     newpath = path+'\\'+dir
#     for f in listdir(newpath):
#         if isfile(join(newpath, f)):
#             preference_paths.append(newpath+'\\' + f)
#     newpath = ''

# print(preference_paths)


# **********************************************************************************
# import os
# print([name for name in os.listdir(".\Domains")])

# **********************************************************************************
# import os
# from os import listdir
# from os.path import isfile, join
# path = '.\Domains'
# preference_paths = []
# domain_dirs = (name for name in os.listdir(path))
# for dir in domain_dirs:
#     newpath = path+'\\'+dir
#     for f in listdir(newpath):
#         if isfile(join(newpath, f)):
#             preference_paths.append(newpath+'\\' + f)
#     newpath = ''

# **********************************************************************************

# from tkinter import *


# def func(value):
#     print(value)


# root = Tk()
# options = ["1", "2", "3"]
# var = StringVar()
# drop = OptionMenu(root, var, *options, command=func)
# drop.place(x=10, y=10)

# root.mainloop()

#  *********************************************************************************


import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("320x80")
        self.title('Tkinter OptionMenu Widget')

        # initialize data
        self.languages = ('Python', 'JavaScript', 'Java',
                          'Swift', 'GoLang', 'C#', 'C++', 'Scala')

        # set up variable
        self.option_var = tk.StringVar(self)

        # create widget
        self.create_wigets()

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(self,  text='Select your most favorite language:')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # option menu
        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.languages[0],
            *self.languages,
            command=self.option_changed)

        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

        # output label
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=1, sticky=tk.W, **paddings)

    def option_changed(self, *args):
        self.output_label['text'] = f'You selected: {self.option_var.get()}'


if __name__ == "__main__":
    app = App()
    app.mainloop()
