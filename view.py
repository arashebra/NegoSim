from configurations import *
import controller
import tkinter as tk
from tkinter import ttk
import session
import tournament


class View:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.init_GUI()

    def init_GUI(self):
        self.create_top_menu()
        self.create_main_window()

    def create_top_menu(self):
        self.menu_bar = tk.Menu(self.parent)
        self.create_start_menu()
        self.create_file_menu()
        self.create_help_menu()

    def create_start_menu(self):
        self.start_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.start_menu.add_command(
            label='Negotiation', command=self.session_window)
        self.start_menu.add_command(
            label='Tornument', command=self.tornument_window)
        self.menu_bar.add_cascade(label='Start', menu=self.start_menu)
        self.parent.config(menu=self.menu_bar)

    def create_file_menu(self):
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(
            label='Add Domain', command=self.add_domain_file)
        self.file_menu.add_command(
            label='Add Elisitation Strategy', command=self.add_elicitation_strategy_file)
        self.file_menu.add_command(
            label='Add User Model', command=self.add_user_model_file)
        self.file_menu.add_command(
            label='Add Bidding Strategy', command=self.add_bidding_strategy_file)
        self.file_menu.add_command(
            label='Add Opponent Model', command=self.add_opponent_model_file)
        self.file_menu.add_command(
            label='Add Acceptance Strategy', command=self.add_acceptance_strategy_file)
        self.file_menu.add_command(
            label='Create Domain Set', command=self.create_domain_set)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.parent.config(menu=self.menu_bar)

    def add_domain_file(self):
        pass

    def add_elicitation_strategy_file(self):
        pass

    def add_user_model_file(self):
        pass

    def add_bidding_strategy_file(self):
        pass

    def add_opponent_model_file(self):
        pass

    def add_acceptance_strategy_file(self):
        pass

    def create_domain_set(self):
        pass

    def session_window(self):
        self.open_session_window()

    def open_session_window(self):
        window_session = tk.Toplevel(self.parent)
        # window_session.geometry("400x400")
        window_session.title("New Session")
        session.Session(window_session)

    def tornument_window(self):
        self.open_tornument_window()

    def open_tornument_window(self):
        tornument_window = tk.Toplevel(self.parent)
        tornument_window.geometry("400x400")
        tornument_window.title("New Tornument")
        tournament.Tournament(tornument_window)

    def create_help_menu(self):
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Help', menu=self.help_menu)
        self.parent.config(menu=self.menu_bar)

    def create_main_window(self):
        notebook_component = ttk.Notebook(self.parent, height=400)
        notebook_component.grid(row=0, column=0)

        frame_domain_set = ttk.Frame(notebook_component)
        frame_domain = ttk.Frame(notebook_component)
        frame_euboa = ttk.Frame(notebook_component)
        frame_protocol = ttk.Frame(notebook_component)
        frame_analyses = ttk.Frame(notebook_component)

        notebook_component.add(frame_domain_set, text=' Domain Set ')
        notebook_component.add(frame_domain, text=' Domain ')
        notebook_component.add(frame_euboa, text=' EUBOA Component')
        notebook_component.add(frame_protocol, text=' Protocols ')
        notebook_component.add(frame_analyses, text=' Analyses ')


if __name__ == '__main__':
    root = tk.Tk()
    # root.geometry(f'{WIDTH_GUI}x{HEIGHT_GUI}')
    root.title(PROGRAM_NAME)
    View(root, controller.Controller())
    root.mainloop()
