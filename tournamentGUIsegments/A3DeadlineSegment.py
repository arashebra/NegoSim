from abc import ABC
from core.SegmentInterface import SegmentInterface
from tkinter import Label, Spinbox, IntVar
from tkinter import ttk


MIN_MAX_PARTICIPANTS = 2
INITIAL_DEADLINE_TIME = 60
MAX_DEADLINE_TIME = 3600000


class A3DeadlineSegment(SegmentInterface, ABC):

    def get_widget(self):
        frame = self.get_frame()
        my_dict = self.get_var_dict()
        lebel1 = Label(frame, text=' Deadline ')
        spinbox_deadline = Spinbox(frame, from_=1, to=MAX_DEADLINE_TIME, textvariable=my_dict[self.get_name()][0])
        spinbox_deadline.delete(0, 'end')
        spinbox_deadline.insert(0, INITIAL_DEADLINE_TIME)

        var_time_type = IntVar()
        time_type = ttk.OptionMenu(frame, var_time_type, 's', *['s', 'ms'])
        time_type.config(width=3)

        return lebel1, spinbox_deadline, time_type

    def get_name(self):
        return 'A3DeadlineSegment.py'