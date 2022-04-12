from core.SegmentInterface import SegmentInterface
from tkinter import Frame
from tkinter.ttk import Button
import CreateObjectByPath
from configurations import *


class A5StartTournamentButtonSegment(SegmentInterface):

    def get_widget(self):
        frame = self.get_frame()
        self.my_dict = self.get_var_dict()
        btn_start = Button(master=frame, text='Start Tournament', width=50, padding=5, command=self.test)
        return btn_start,

    def get_name(self):
        return 'A5StartTournamentButtonSegment'

    def test(self):
        print('obj')
        # print(self.var_dict['A4AnalysisSegment.py'].get())

