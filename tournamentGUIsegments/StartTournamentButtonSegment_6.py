from GUI.AbstractGUISegment import AbstractGUISegment
from tkinter import messagebox
from tkinter.ttk import Button
from GUI.visualization.Charts import Charts
from core.BilateralTournament import BilateralTournament
import tkinter as tk

NOTSELECTIONMESSAGE = 'Please select '


class StartTournamentButtonSegment_6(AbstractGUISegment):

    def get_widget(self) -> tuple:
        self.__first_clicked = False
        frame = self.get_frame()
        # self.my_dict = self.get_var_dict()
        btn_start = Button(master=frame, text='Start Tournament', width=50, padding=5, command=self.start_tournament)
        return btn_start,

    def get_name(self):
        return 'StartTournamentButtonSegment_6.py'

    def start_tournament(self):

        message = NOTSELECTIONMESSAGE

        row_widgets = self.get_gui_widgets()

        optionMenu_protocol_var = self.get_special_segment_special_StringVar(0, 0)
        selected_protocol = optionMenu_protocol_var.get()
        if selected_protocol == 'Select a protocol':
            message += 'Protocol, '

        selected_analysis_string_var = self.get_special_segment_special_StringVar(1, 0)
        selected_analysis = selected_analysis_string_var.get()
        if selected_analysis == 'Select an analysis':
            message += 'Analysis, '

        selected_tournament_analysis_string_var = self.get_special_segment_special_StringVar(2, 0)
        selected_tournament_analysis = selected_tournament_analysis_string_var.get()
        if selected_tournament_analysis == 'Select a Tournament Analysis':
            message += 'Tournament Analysis, '

        listbox_domain = row_widgets[3][1]  # widget in row=3 and col=1
        domain_indexes = listbox_domain.curselection()
        selected_domains = []
        if len(domain_indexes) > 0:
            for index in domain_indexes:
                selected_domains.append(listbox_domain.get(index))
        else:
            message += 'Domain(s), '

        agent1_names = []
        listbox_agent1 = row_widgets[4][1]  # widget in row=3 and col=1
        agent1_indexes = listbox_agent1.curselection()
        if len(agent1_indexes) > 0:
            for agent1_index in agent1_indexes:
                agent1_name = listbox_agent1.get(agent1_index)
                agent1_names.append(agent1_name)
        else:
            message += 'Agent(s), '

        opponent_names = []
        listbox_opponent = row_widgets[4][4]  # widget in row=3 and col=1
        opponent_indexes = listbox_opponent.curselection()
        if len(opponent_indexes) > 0:
            for opponent_index in opponent_indexes:
                opponent_name = listbox_opponent.get(opponent_index)
                opponent_names.append(opponent_name)
        else:
            message += 'opponent(s)'

        deadline_var_tuple = self.get_var_dict()['DeadlineSegment_5.py']
        deadline_var = deadline_var_tuple[0]
        deadline = deadline_var.get()

        if message != NOTSELECTIONMESSAGE:
            return messagebox.showerror('Error', message)

        self.bilateral_tournament = BilateralTournament(protocol_name=selected_protocol,
                                                        analysis_man_name=selected_analysis,
                                                        Tournament_analysis_name=selected_tournament_analysis,
                                                        deadline=deadline,
                                                        agent_names=agent1_names,
                                                        opponent_names=opponent_names,
                                                        domain_names=selected_domains)

        self.bilateral_tournament.start_tournament()

        h_frame1 = self.get_special_horizontal_frame(1)
        if not self.__first_clicked:
            self.create_tournament_visualization_window1(h_frame1)
        else:
            h_frame_alternative1 = tk.Frame(master=self.get_root())
            self.replace_frame(1, h_frame_alternative1)
            self.create_tournament_visualization_window1(h_frame_alternative1)

        h_frame2 = self.get_special_horizontal_frame(2)
        if not self.__first_clicked:
            self.create_tournament_visualization_window2(h_frame2)
        else:
            h_frame_alternative1 = tk.Frame(master=self.get_root())
            self.replace_frame(2, h_frame_alternative1)
            self.create_tournament_visualization_window2(h_frame_alternative1)

        self.__first_clicked = True

    def create_tournament_visualization_window1(self, h_frame1):
        chart = Charts()
        tournament_analysis_man = self.bilateral_tournament.get_tournament_analysis_man()
        my_data = tournament_analysis_man.get_tournament_analysis_data()
        agents_names = [key.split('_')[1] for key, value in my_data.items() if key.split('_')[0] == 'party1']
        agents_utilities = [value for key, value in my_data.items() if key.split('_')[0] == 'party1']
        data = {'Agents': agents_names,
                'Utility': agents_utilities
                }
        chart.bar_chart(data=data, frame=h_frame1, col1_name='Agents', col2_name='Utility')

    def create_tournament_visualization_window2(self, h_frame1):
        chart = Charts()
        tournament_analysis_man = self.bilateral_tournament.get_tournament_analysis_man()
        my_data = tournament_analysis_man.get_tournament_analysis_data()
        agents_names = [key.split('_')[0] for key, value in my_data.items() if key.split('_')[1] == 'SocialWelfare']
        agents_utilities = [value for key, value in my_data.items() if key.split('_')[1] == 'SocialWelfare']
        data = {'Agents': agents_names,
                'SocialWelfare': agents_utilities
                }
        chart.bar_chart(data=data, frame=h_frame1, col1_name='Agents', col2_name='SocialWelfare')
