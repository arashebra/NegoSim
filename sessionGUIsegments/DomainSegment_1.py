from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk
from controller import Controller


class DomainSegment_1(AbstractGUISegment, ABC):

    def get_widget(self):
        ctrl = Controller()
        domain_list = ctrl.fetch_domains()
        self.my_dict = self.get_var_dict()
        self.my_dict[self.get_name()][0].set('Select a Domain')
        optionMenu_domain = tk.OptionMenu(self.get_frame(), self.my_dict[self.get_name()][0], *domain_list, command=self.create_select_preference)
        optionMenu_domain.configure(width=25)
        lable = tk.Label(master=self.get_frame(), text='Domain                 ')

        return lable, optionMenu_domain

    def create_select_preference(self, selected_domain):
        # print(self.my_dict['ProtocolSegment_0.py'][0].get())
        # print(self.my_dict[self.get_name()][0].get())
        # print(selected_domain)

        ctrl = Controller()
        preference_list = ctrl.fetch_preferences_of_domain(selected_domain)
        my_dict = self.get_var_dict()
        # new_frame = tk.Frame(self.get_root())
        new_frame = tk.Frame(self.get_special_frame(6))
        # self.replace_frame(index=6, frame=new_frame)
        self.add_new_frame(index=6, frame=new_frame)
        self.add_new_frame(6, new_frame)
        self.my_dict['PreferenceSegment_6.py'][0].set('Select a Preference')
        optionMenu_preference = tk.OptionMenu(new_frame, my_dict['PreferenceSegment_6.py'][0], *preference_list)
        optionMenu_preference.configure(width=25)
        label = tk.Label(master=self.get_all_frames()[6], text='Preference profile')
        self.add_new_gui_widget(6, label)
        self.add_new_gui_widget(6, optionMenu_preference)
        label.pack(side='left')
        optionMenu_preference.pack(side='left')


    def get_name(self):
        return 'DomainSegment_1.py'
