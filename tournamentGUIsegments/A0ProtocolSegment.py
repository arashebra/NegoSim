from abc import ABC
from core.SegmentInterface import SegmentInterface
import tkinter as tk


class A0ProtocolSegment(SegmentInterface, ABC):

    def get_widget(self, frame, var_dict: dict):
        protocol_list = ["Protocol 1", "Protocol 2", "Protocol 3", "Protocol 4"]
        var_dict[self.get_name()].set("Select a Analysis")
        optionMenu_protocol = tk.OptionMenu(frame, var_dict[self.get_name()], *protocol_list)

        lable = tk.Label(master=frame, text='Protocol')

        return lable, optionMenu_protocol

    def get_name(self):
        return 'A0ProtocolSegment.py'