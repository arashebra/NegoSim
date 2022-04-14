from abc import ABC
from AbstractGUISegment import SegmentInterface
import tkinter as tk
from controller import Controller


class S1DomainSegment(SegmentInterface, ABC):

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
        # print(self.my_dict['S0ProtocolSegment.py'][0].get())
        # print(self.my_dict[self.get_name()][0].get())
        # print(selected_domain)
        # s6 = CreateObjectByPath.get_object(package_name=SESSION_GUI_PACKAGE_NAME, file_name='S6PreferenceSegment.py', self.get_frame(), )
        # S6PreferenceSegment.optionMenu_preference.configure(width=25, state='enable')
        # s6 = S6PreferenceSegment(self.get_frame(), self.get_var_dict())
        ctrl = Controller()
        preference_list = ctrl.fetch_preferences_of_domain(selected_domain)
        my_dict = self.get_var_dict()
        my_dict[self.get_name()][0].set('Select a Preference')
        optionMenu_preference = tk.OptionMenu(self.get_frame(), my_dict[self.get_name()][0], *preference_list)
        optionMenu_preference.configure(width=25)
        lable = tk.Label(master=self.get_frame(), text='Preference profile')

        lable.pack(side='left')
        optionMenu_preference.pack(side='bottom')


    def get_name(self):
        return 'S1DomainSegment.py'
