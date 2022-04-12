from abc import ABC
from core.AbstractGUISegment import SegmentInterface
from tkinter import Label, OptionMenu


class S1AnalysisSegment(SegmentInterface, ABC):

    def get_widget(self):
        frame = self.get_frame()
        my_dict = self.get_var_dict()
        protocol_list = ["Analysis 1", "Analysis 2", "Analysis 3", "Analysis 4"]
        my_dict[self.get_name()][0].set('Select an analysis')
        optionMenu_Analysis = OptionMenu(frame, my_dict[self.get_name()][0], *protocol_list)

        lable = Label(master=frame, text='Analysis ')

        return lable, optionMenu_Analysis

    def get_name(self):
        return 'S1AnalysisSegment.py'