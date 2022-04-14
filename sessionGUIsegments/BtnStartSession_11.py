from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk

class BtnStartSession_11(AbstractGUISegment):

    def get_widget(self) -> tuple:
        btn_start = tk.Button(master=self.get_frame(), text='Start Negotiation',
                              width=42, height=3, command=self.start_negotiation)
        return btn_start,

    def start_negotiation(self):
        protocol_strinVar = self.get_special_segment_special_StringVar(0, 0)
        protocol_name = protocol_strinVar.get()

        domain_strinVar = self.get_special_segment_special_StringVar(1, 0)
        domain_name = domain_strinVar.get()

        analysis_stringVar = self.get_special_segment_special_StringVar(2, 0)
        analysis_name = analysis_stringVar.get()

        listbox_party_preference = self.get_special_widget(8, 0)
        party_preference1 = self.get_text_from_listbox(listbox_party_preference, 0)
        party_preference2 = self.get_text_from_listbox(listbox_party_preference, 1)

        deadline_var = self.get_special_segment_special_StringVar(10, 0)
        deadline = deadline_var.get()

        print(protocol_name)
        print(domain_name)
        print(analysis_name)
        print(party_preference1, ' - ', party_preference2)
        print(deadline)

    def get_text_from_listbox(self, listbox_party_and_preference, row):
        text = listbox_party_and_preference.get(row)
        return text


    def get_name(self):
        return 'BtnStartSession_11.py'