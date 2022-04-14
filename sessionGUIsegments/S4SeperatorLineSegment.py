from abc import ABC
from AbstractGUISegment import SegmentInterface
import tkinter as tk


class S4SeperatorLineSegment(SegmentInterface, ABC):

    def get_widget(self):
        my_seperator = tk.Label(master=self.get_frame(), text='*******************************************')
        return my_seperator,

    def get_name(self):
        return 'S4SeperatorLineSegment.py'