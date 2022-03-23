from genericpath import isdir
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from os import listdir
from os.path import isfile, join
import os

SELECT_PROTOCOL_TEXT = 'Select a Protocol'
SELECT_DOMAIN_TEXT = 'Select a Domain'
SELECT_ANALYSE_TEXT = 'Select an Analyse'
ADD_PARTICIPANT_ERROR_MESSAGE = 'Please select both party and preference then click "Add Participant"'
ADD_PARTICIPANT_BUTTON_TEXT = 'Add Participant'
DELETE_PARTICIPANT_BUTTON_TEXT = 'Delete Participant'
SELECT_PARTY_TEXT = 'Select a Party'
SELECT_PREFERENCE_PROFILE = 'Select a Preference Profile'


class Session:
    def __init__(self, window):
        self.window = window
        self.create_session_gui()

    def create_session_gui(self):
        self.frame_session = tk.Frame(self.window)
        self.frame_session.grid(
            row=0, column=0, columnspan=10, padx=40, pady=10)

        self.create_protocol_menu()
        self.create_domain_menu()
        self.create_analyse_menu()

        # In order to make space
        tk.Label(self.frame_session, text='').grid(row=3, column=1)

        # In order to show the rest content
        tk.Label(self.frame_session, text=' Participant ').grid(
            row=4, column=1)

        # In order to separate content
        ttk.Separator(self.frame_session, orient='horizontal').grid(
            row=5, column=0, columnspan=10, sticky='we')

        self.create_select_party()
        # self.create_select_preference()

        # Button in order to add participant

        self.btn_add_participant = ttk.Button(
            self.frame_session, text=ADD_PARTICIPANT_BUTTON_TEXT, command=self.add_participant)
        self.btn_add_participant.grid(
            row=8, column=0, columnspan=3, sticky='we', padx=2)

        # List box that show the negotiation participants
        self.listbox_party_and_preference = tk.Listbox(self.frame_session)
        self.listbox_party_and_preference.grid(
            row=9, column=0, columnspan=5, sticky='we', pady=2)

        # Delete Button in order to delete the participant
        btn_delete_participant = ttk.Button(self.frame_session, text=DELETE_PARTICIPANT_BUTTON_TEXT,
                                            command=self.delete_participant)
        btn_delete_participant.grid(
            row=10, column=0, columnspan=5, sticky='we')

        # In order to make space
        tk.Label(self.frame_session, text='', pady=5).grid(row=11, column=1)

        # Show Information to user
        tk.Label(self.frame_session, text=' Session Setting ',
                 pady=5).grid(row=12, column=1)

        # In order to separate content
        ttk.Separator(self.frame_session, orient='horizontal').grid(
            row=13, column=0, columnspan=10, sticky='we')

        self.create_deadline_menu()

        ttk.Button(self.frame_session, text=' Start ', padding=5, command=self.start_negotiation_session).grid(
            row=15, column=0, columnspan=5, sticky='we', pady=15)

    def delete_participant(self):
        self.listbox_party_and_preference.delete(tk.ANCHOR)
        self.btn_add_participant.config(state='enable')

    # Option menu in order to select the protocol
    def create_protocol_menu(self):
        tk.Label(self.frame_session, text='Protocol ').grid(row=0, column=0)
        self.protocol_list = ["Protocol 1", "Protocol 2",
                              "Protocol 3", "Protocol 4"]
        self.var_protocol_name = tk.StringVar()
        self.var_protocol_name.set(SELECT_PROTOCOL_TEXT)
        self.optionMenu_protocol = tk.OptionMenu(
            self.frame_session, self.var_protocol_name, *self.protocol_list)
        self.optionMenu_protocol.config(width=25)
        self.optionMenu_protocol.grid(
            row=0, column=1, columnspan=2, sticky='we')

    # Option menu in order to select the domain
    def create_domain_menu(self):
        tk.Label(self.frame_session, text='Domain ').grid(row=1, column=0)
        self.domain_lists = [name for name in os.listdir(".\Domains")]
        self.var_domain_name = tk.StringVar()
        self.var_domain_name.set(SELECT_DOMAIN_TEXT)
        self.optionMenu_domain = tk.OptionMenu(
            self.frame_session, self.var_domain_name, *self.domain_lists, command=self.create_select_preference)
        self.optionMenu_domain.config(width=25)
        self.optionMenu_domain.grid(row=1, column=1, columnspan=2, sticky='we')

    # Option menu in order to select the analyse file
    def create_analyse_menu(self):
        tk.Label(self.frame_session, text='Analyse file ').grid(
            row=2, column=0)
        self.analyse_list = ["analyse 1", "analyse 2",
                             "analyse 3", "analyse 4"]
        self.var_analyse_name = tk.StringVar()
        self.var_analyse_name.set(SELECT_ANALYSE_TEXT)
        self.optionMenu_analyse = tk.OptionMenu(
            self.frame_session, self.var_analyse_name, *self.analyse_list)
        self.optionMenu_analyse.config(width=25)
        self.optionMenu_analyse.grid(
            row=2, column=1, columnspan=2, sticky='we')

    # Option menu in order to select the party
    def create_select_party(self):
        tk.Label(self.frame_session, text=' Party Name ', padx=15).grid(
            row=6, column=0)
        party_path = '.\Agents'
        self.party_list = [f for f in listdir(
            party_path) if isfile(join(party_path, f))]
        self.var_party_name = tk.StringVar()
        self.var_party_name.set(SELECT_PARTY_TEXT)
        self.optionMenu_party = tk.OptionMenu(
            self.frame_session, self.var_party_name, *self.party_list)
        self.optionMenu_party.config(width=25)
        self.optionMenu_party.grid(row=6, column=1, columnspan=2, sticky='we')

    # Option menu in order to select the preference profile
    def create_select_preference(self, selected_domain):
        tk.Label(self.frame_session, text='Preference Profile').grid(
            row=7, column=0)
        path = '.\Domains'+'\\'+selected_domain
        if isdir(path):
            self.preference_profile_list = [name for name in os.listdir(path)]
            self.var_preference_profile_name = tk.StringVar()
            self.var_preference_profile_name.set(SELECT_PREFERENCE_PROFILE)
            self.optionMenu_preference_profile = tk.OptionMenu(
                self.frame_session, self.var_preference_profile_name, *self.preference_profile_list)
            self.optionMenu_preference_profile.config(width=25)
            self.optionMenu_preference_profile.grid(
                row=7, column=1, columnspan=2, sticky='we')

    # Show Deadline time
    def create_deadline_menu(self):
        tk.Label(self.frame_session, text=' Deadline ',
                 pady=5).grid(row=14, column=0)
        self.var_deadline = tk.StringVar()
        self.spinbox_deadline = tk.Spinbox(
            self.frame_session, from_=1, to=3600, textvariable=self.var_deadline)
        self.spinbox_deadline.delete(0, 'end')
        self.spinbox_deadline.insert(0, 60)
        self.spinbox_deadline.grid(row=14, column=1)

    # This method add participants if there is no error
    def add_participant(self):
        if self.listbox_party_and_preference.size() >= 1:
            self.btn_add_participant.config(state='disable')
        number_of_items = self.listbox_party_and_preference.size()
        if self.var_party_name.get() == SELECT_PARTY_TEXT or self.var_preference_profile_name.get() == SELECT_PREFERENCE_PROFILE:
            return messagebox.showerror(
                title='Error!', message=ADD_PARTICIPANT_ERROR_MESSAGE)
        self.listbox_party_and_preference.insert(
            number_of_items+1, f"{self.var_party_name.get()} -> {self.var_domain_name.get()}/{self.var_preference_profile_name.get()}")

    def start_negotiation_session(self):
        message = 'Please select'
        if self.var_protocol_name.get() == SELECT_PROTOCOL_TEXT:
            message += ' Protocol,'
        if self.var_domain_name.get() == SELECT_DOMAIN_TEXT:
            message += ' domain,'
        if self.var_analyse_name.get() == SELECT_ANALYSE_TEXT:
            message += ' Analyse,'
        if self.listbox_party_and_preference.size() < 2:
            message += ' participatnts,'

        if message != 'Please select':
            return messagebox.showerror(
                title='Error!', message=message)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('New Seesion')
    # root.geometry('400x400')
    Session(root)
    root.mainloop()
