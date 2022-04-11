from abc import ABC
from core.SegmentInterface import SegmentInterface
import tkinter as tk


class ProtocolSegment(SegmentInterface, ABC):

    def get_widget(self, frame, *var_protocol_name):
        widget_list = []

        protocol_list = ["Protocol 1", "Protocol 2", "Protocol 3", "Protocol 4"]
        var_protocol_name[0].set("Select a Protocol")
        optionMenu_protocol = tk.OptionMenu(frame, var_protocol_name[0], *protocol_list)

        lable = tk.Label(master=frame, text='Protocol')
        widget_list.append(lable)
        widget_list.append(optionMenu_protocol)

        return widget_list, 0
