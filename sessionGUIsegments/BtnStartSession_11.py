from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk
from core.BilateralSession import BilateralSession
from core.BidSpace import BidSpace
from GUI.visualization.Charts import Charts
from controller import Controller

PARTY_PREFERENCE_SEPERATOR = ' -> '


class BtnStartSession_11(AbstractGUISegment):

    def get_widget(self) -> tuple:
        self.first_clicked = False
        btn_start = tk.Button(master=self.get_frame(), text='Start Negotiation',
                              width=42, height=3, command=self.start_negotiation)
        return btn_start,

    def start_negotiation(self):
        protocol_strinVar = self.get_special_segment_special_StringVar(0, 0)
        protocol_name = protocol_strinVar.get()

        domain_strinVar = self.get_special_segment_special_StringVar(1, 0)
        self.domain_name = domain_strinVar.get()

        analysis_stringVar = self.get_special_segment_special_StringVar(2, 0)
        analysis_name = analysis_stringVar.get()

        listbox_party_preference = self.get_special_widget(8, 0)
        party_preference1_txt = self.get_text_from_listbox(listbox_party_preference, 0)
        party1_name, self.party1_preference_name = self.party_preference_text_separator(party_preference1_txt)

        party_preference2_txt = self.get_text_from_listbox(listbox_party_preference, 1)
        party2_name, self.party2_preference_name = self.party_preference_text_separator(party_preference2_txt)

        deadline_var = self.get_special_segment_special_StringVar(10, 0)
        deadline = deadline_var.get()

        self.bilateral_session = BilateralSession(protocol_name=protocol_name,
                                                  analysis_man_name=analysis_name,
                                                  deadline=deadline,
                                                  first_preference_name=self.party1_preference_name,
                                                  second_preference_name=self.party2_preference_name,
                                                  party1_name=party1_name,
                                                  party2_name=party2_name,
                                                  domain_name=self.domain_name)
        self.first_clicked = True

        self.bilateral_session.start_session()
        h_frame1 = self.get_special_horizontal_frame(1)
        if not self.first_clicked:
            self.create_visualization_window(h_frame1)
        else:
            h_frame_alternative1 = tk.Frame(master=self.get_root())
            self.replace_frame(1, h_frame_alternative1)
            self.create_visualization_window(h_frame_alternative1)

    def party_preference_text_separator(self, party_preference_text: str) -> tuple:
        temp = party_preference_text.split(PARTY_PREFERENCE_SEPERATOR)
        return temp[0], temp[1]

    def get_text_from_listbox(self, listbox_party_and_preference, row):
        text = listbox_party_and_preference.get(row)
        return text

    def create_visualization_window(self, frame):

        ctrl = Controller()
        preference1 = ctrl.fetch_preference(self.domain_name, self.party1_preference_name)
        preference2 = ctrl.fetch_preference(self.domain_name, self.party2_preference_name)
        bid_space1 = BidSpace(preference1)
        bid_space2 = BidSpace(preference2)
        data = {self.party1_preference_name: bid_space1.get_all_bids_utility(),
                self.party2_preference_name: bid_space2.get_all_bids_utility()
                }

        chart = Charts()
        chart.scatter_chart(data=data, col_name1=self.party1_preference_name,
                            col_name2=self.party2_preference_name, frame=frame, position='top')

        protocol = self.bilateral_session.get_protocol()
        analysis_man = self.bilateral_session.get_analysis_man()

        all_offers = protocol.get_nego_table().get_offers_on_table()

        party1 = protocol.get_parties()[0]
        party2 = protocol.get_parties()[1]

        nego_state = protocol.get_nego_table().get_state_info().get_negotiation_state()
        s = ''
        if nego_state == 1:
            s += f"Agreement by {party2.get_name() if len(all_offers[party1]) == len(all_offers[party2]) else party1.get_name()}"
        else:
            s += "negotiation ended without agreement"
        tk.Label(master=frame, text=f'Status : {s}').pack(side='top')

        frame_left = tk.Frame(master=frame)
        frame_mid = tk.Frame(master=frame)
        frame_right = tk.Frame(master=frame)
        frame_left.pack(side='left', fill='both')
        frame_mid.pack(side='left')
        frame_right.pack(side='left', fill='both')

        tk.Label(master=frame_left, text=f'{party1.get_name()}').pack(side='top')
        tk.Label(master=frame_mid, text='  Vs  ').pack(side='top')
        tk.Label(master=frame_right, text=f'{party2.get_name()}').pack(side='top')

        analysis_data = analysis_man.get_analysis_data()

        scr1_horizontal = tk.Scrollbar(master=frame_left, orient=tk.HORIZONTAL)
        scr1_horizontal.pack(side='bottom', fill='x')
        listbox_party1_bids = tk.Listbox(master=frame_left, width=50)
        listbox_party1_bids.pack(side='left', fill='both')
        listbox_party1_bids.config(xscrollcommand=scr1_horizontal.set)
        scr1_horizontal.config(command=listbox_party1_bids.xview)
        scr1_vertical = tk.Scrollbar(master=frame_left)
        scr1_vertical.pack(side='right', fill='y')
        listbox_party1_bids.config(yscrollcommand=scr1_vertical.set)
        scr1_vertical.config(command=listbox_party1_bids.yview)
        listbox_party1_bids.insert(tk.END, *all_offers[party1])
        listbox_party1_bids.insert(tk.END, analysis_data)

        scr2_horizontal = tk.Scrollbar(master=frame_right, orient=tk.HORIZONTAL)
        scr2_horizontal.pack(side='bottom', fill='x')
        listbox_party2_bids = tk.Listbox(master=frame_right, width=50)
        listbox_party2_bids.pack(side='left', fill='both')
        listbox_party2_bids.config(xscrollcommand=scr2_horizontal.set)
        scr2_horizontal.config(command=listbox_party2_bids.xview)
        scr2_vertical = tk.Scrollbar(master=frame_right)
        scr2_vertical.pack(side='right', fill='y')
        listbox_party2_bids.config(yscrollcommand=scr2_vertical.set)
        scr2_vertical.config(command=listbox_party2_bids.yview)
        listbox_party2_bids.insert(tk.END, *all_offers[party2])
        listbox_party2_bids.insert(tk.END, analysis_data)

    def get_name(self):
        return 'BtnStartSession_11.py'
