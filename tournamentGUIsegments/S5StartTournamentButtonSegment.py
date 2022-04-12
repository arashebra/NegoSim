from core.AbstractGUISegment import SegmentInterface
from tkinter import Frame, messagebox
from tkinter.ttk import Button
import CreateObjectByPath
from configurations import *


class S5StartTournamentButtonSegment(SegmentInterface):

    def get_widget(self):
        frame = self.get_frame()
        self.my_dict = self.get_var_dict()
        btn_start = Button(master=frame, text='Start Tournament', width=50, padding=5, command=self.start_tournament)
        return btn_start,

    def get_name(self):
        return 'S5StartTournamentButtonSegment'

    def start_tournament(self):
        row_widgets = self.get_gui_widgets()

        optionMenu_protocol_var_tuple = self.my_dict['S0ProtocolSegment.py']
        selected_protocol = optionMenu_protocol_var_tuple[0].get()
        if selected_protocol == 'Select a protocol':
            return messagebox.showerror('Error', 'Please select Protocol')

        optionMenu_analysis_var_tuple = self.my_dict['S1AnalysisSegment.py']
        selected_analysis = optionMenu_analysis_var_tuple[0].get()
        if selected_analysis == 'Select an analysis':
            return messagebox.showerror('Error', 'Please select Analysis!')

        listbox_domain = row_widgets[2][1] # widget in row=2 and col=1
        domain_indexes = listbox_domain.curselection()
        if len(domain_indexes) > 0:
            selected_domains = []
            for index in domain_indexes:
                selected_domains.append(listbox_domain.get(index))
        else:
            return messagebox.showerror('Error', 'Please select domain(s)!')

        listbox_agent1 = row_widgets[3][1] # widget in row=3 and col=1
        agent1_index = listbox_agent1.curselection()
        if len(agent1_index) > 0:
            agent1_name = listbox_agent1.get(agent1_index)
        else:
            return messagebox.showerror('Error', 'Please select an Agent!')

        opponent_names = []
        listbox_opponent = row_widgets[3][3]  # widget in row=3 and col=1
        opponent_indexes = listbox_opponent.curselection()
        if len(opponent_indexes) > 0:
            for opponent_index in opponent_indexes:
                opponent_name = listbox_opponent.get(opponent_index)
                opponent_names.append(opponent_name)
        else:
            return messagebox.showerror('Error', 'Please select opponent(s)!')

        print(selected_protocol,' - ', selected_analysis, ' - ')
        print(selected_domains)
        print(agent1_name)
        print(opponent_names)