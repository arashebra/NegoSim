from abc import ABC
from AbstractGUISegment import SegmentInterface
import tkinter as tk
from controller import Controller


class S6PreferenceSegment(SegmentInterface, ABC):
    optionMenu_preference = None

    def get_widget(self):

        my_dict = self.get_var_dict()
        domain_var_tuple = my_dict['S1DomainSegment.py']
        domain_name = domain_var_tuple[0].get()
        ctrl = Controller()
        optionMenu_preference = None
        if domain_name != 'Select a Domain':
            preference_list = ctrl.fetch_preferences_of_domain(domain=domain_name)
        else:
            preference_list = ['Select a Preference']
        my_dict = self.get_var_dict()
        my_dict[self.get_name()][0].set('Select a Preference')
        optionMenu_preference = tk.OptionMenu(self.get_frame(), my_dict[self.get_name()][0], *preference_list)
        optionMenu_preference.configure(width=25, state='disable')
        lable = tk.Label(master=self.get_frame(), text='Preference Profile')
        if optionMenu_preference == None:
            return lable,
        else:
            return lable, optionMenu_preference

    def get_name(self):
        return 'S6PreferenceSegment.py'

