from abc import ABC
from core.SegmentInterface import SegmentInterface
from tkinter import Frame, Label, Spinbox


MIN_MAX_PARTICIPANTS = 2
INITIAL_DEADLINE_TIME = 60
MAX_DEADLINE_TIME = 3600000


class A3DeadlineSegment(SegmentInterface, ABC):

    def get_widget(self, frame: Frame, var_dict: dict):
        lebel1 = Label(frame, text=' Deadline ')
        spinbox_deadline = Spinbox(frame, from_=1, to=MAX_DEADLINE_TIME, textvariable=var_dict[self.get_name()])
        spinbox_deadline.delete(0, 'end')
        spinbox_deadline.insert(0, INITIAL_DEADLINE_TIME)
        return lebel1, spinbox_deadline

    def get_name(self):
        return 'A3DeadlineSegment.py'