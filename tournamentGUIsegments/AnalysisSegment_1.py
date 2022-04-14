from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
from tkinter import Label, OptionMenu
from controller import Controller


class AnalysisSegment_1(AbstractGUISegment, ABC):

    def get_widget(self):
        ctrl = Controller()
        frame = self.get_frame()
        my_dict = self.get_var_dict()
        analysis_list = ctrl.fetch_analysis_men()
        my_dict[self.get_name()][0].set('Select an analysis')
        optionMenu_Analysis = OptionMenu(frame, my_dict[self.get_name()][0], *analysis_list)

        lable = Label(master=frame, text='Analysis ')

        return lable, optionMenu_Analysis

    def get_name(self):
        return 'AnalysisSegment_1.py'