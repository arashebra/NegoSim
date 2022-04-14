from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk

INITIAL_DEADLINE_TIME = 60
MAX_DEADLINE_TIME = 3600000


class DeadLineSegment_10(AbstractGUISegment):

    def get_widget(self) -> tuple:
        my_dict = self.get_var_dict()
        lable = tk.Label(master=self.get_frame(), text='Deadline')
        spinbox_deadline = tk.Spinbox(self.get_frame(), from_=1, to=MAX_DEADLINE_TIME,
                                      textvariable=my_dict[self.get_name()][0])
        spinbox_deadline.delete(0, 'end')
        spinbox_deadline.insert(0, INITIAL_DEADLINE_TIME)
        return lable, spinbox_deadline

    def get_name(self):
        return 'DeadLineSegment_10.py'
