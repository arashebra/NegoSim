from GUI.AbstractGUISegment import AbstractGUISegment
from tkinter import messagebox
from tkinter.ttk import Button
from core.BilateralTournament import BilateralTournament


class StartTournamentButtonSegment_5(AbstractGUISegment):

    def get_widget(self):
        frame = self.get_frame()
        self.my_dict = self.get_var_dict()
        btn_start = Button(master=frame, text='Start Tournament', width=50, padding=5, command=self.start_tournament)
        return btn_start,

    def get_name(self):
        return 'StartTournamentButtonSegment_5.py'

    def start_tournament(self):
        row_widgets = self.get_gui_widgets()

        optionMenu_protocol_var_tuple = self.my_dict['ProtocolSegment_0.py']
        selected_protocol = optionMenu_protocol_var_tuple[0].get()
        if selected_protocol == 'Select a protocol':
            return messagebox.showerror('Error', 'Please select Protocol')

        optionMenu_analysis_var_tuple = self.my_dict['AnalysisSegment_1.py']
        selected_analysis = optionMenu_analysis_var_tuple[0].get()
        if selected_analysis == 'Select an analysis':
            return messagebox.showerror('Error', 'Please select Analysis!')

        listbox_domain = row_widgets[2][1]  # widget in row=2 and col=1
        domain_indexes = listbox_domain.curselection()
        if len(domain_indexes) > 0:
            selected_domains = []
            for index in domain_indexes:
                selected_domains.append(listbox_domain.get(index))
        else:
            return messagebox.showerror('Error', 'Please select domain(s)!')

        agent1_names = []
        listbox_agent1 = row_widgets[3][1]  # widget in row=3 and col=1
        agent1_indexes = listbox_agent1.curselection()
        if len(agent1_indexes) > 0:
            for agent1_index in agent1_indexes:
                agent1_name = listbox_agent1.get(agent1_index)
                agent1_names.append(agent1_name)
        else:
            return messagebox.showerror('Error', 'Please select an Agent!')

        opponent_names = []
        listbox_opponent = row_widgets[3][4]  # widget in row=3 and col=1
        opponent_indexes = listbox_opponent.curselection()
        if len(opponent_indexes) > 0:
            for opponent_index in opponent_indexes:
                opponent_name = listbox_opponent.get(opponent_index)
                opponent_names.append(opponent_name)
        else:
            return messagebox.showerror('Error', 'Please select opponent(s)!')

        deadline_var_tuple = self.get_var_dict()['DeadlineSegment_4.py']
        deadline_var = deadline_var_tuple[0]
        deadline = deadline_var.get()

        # print('deadline: ', deadline)
        # print('Protocol: ', selected_protocol)
        # print('Analysis: ', selected_analysis)
        # print('Domain(s): ', selected_domains)
        # print('Agent(s) A: ', agent1_names)
        # print('Agent(s) B: ', opponent_names)

        bilateral_tournament = BilateralTournament(protocol_name=selected_protocol,
                                                   analysis_man_name=selected_analysis,
                                                   deadline=deadline,
                                                   party1_names=agent1_names,
                                                   party2_names=opponent_names,
                                                   domain_names=selected_domains)

        bilateral_tournament.start_tournament()
