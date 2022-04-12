from abc import ABC
from core.SegmentInterface import SegmentInterface
from tkinter import Frame, StringVar, Listbox, END, Label, OptionMenu


class A4AnalysisSegment(SegmentInterface, ABC):

    def get_widget(self, frame: Frame, var_dict: dict):
        protocol_list = ["Analysis 1", "Analysis 2", "Analysis 3", "Analysis 4"]
        var_dict[self.get_name()].set("Select a Analysis")
        optionMenu_Analysis = OptionMenu(frame, var_dict[self.get_name()], *protocol_list)

        lable = Label(master=frame, text='Analysis ')

        return lable, optionMenu_Analysis

    def get_name(self):
        return 'A4AnalysisSegment.py'