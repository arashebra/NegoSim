from abc import ABC
from AbstractGUISegment import SegmentInterface
import tkinter as tk

class S3ParticipantLabel(SegmentInterface, ABC):

    def get_widget(self):
        lable = tk.Label(master=self.get_frame(), text='Participant')
        return lable,

    def get_name(self):
        return 'S3ParticipantLabel.py'