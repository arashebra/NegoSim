from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk

PARTY_PREFERENCE_SEPERATOR = ' -> '

class BtnAddParty_7(AbstractGUISegment):

    def get_widget(self) -> tuple:
        btn_add_participant = tk.Button(master=self.get_frame(), text='Add Participant',
                                        width=42, command=self.add_participant)
        return btn_add_participant,

    def add_participant(self):

        party_string_var = self.get_special_segment_special_StringVar(5, 0)
        party_name = party_string_var.get()

        preference_string_var = self.get_special_segment_special_StringVar(6, 0)
        preference_name = preference_string_var.get()

        listbox_party_and_preference = self.get_special_widget(8, 0)

        listbox_party_and_preference.insert(tk.END, party_name+PARTY_PREFERENCE_SEPERATOR+preference_name)




    def get_name(self):
        return 'BtnAddParty_7.py'