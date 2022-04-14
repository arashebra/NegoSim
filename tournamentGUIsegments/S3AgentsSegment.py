from abc import ABC
from AbstractGUISegment import SegmentInterface
from tkinter import Frame, Listbox, END, Label
from controller import Controller


class S3AgentsSegment(SegmentInterface, ABC):

    def get_widget(self):
        ctrl = Controller()

        frame = self.get_frame()

        frame_left = Frame(master=frame)
        frame_left.pack(side='left')

        frame_right = Frame(master=frame)
        frame_right.pack(side='left')

        lebel1 = Label(master=frame_left, text='Agent ')

        listbox_agents1 = Listbox(master=frame_left, width=25, selectmode="multiple", exportselection=0)
        list_agents1 = ctrl.fetch_agents()
        listbox_agents1.insert(END, *list_agents1)

        lebel_Vs = Label(master=frame_left, text='Vs  Opponents ')

        listbox_agents2 = Listbox(master=frame_right, width=25, selectmode="multiple", exportselection=0)
        list_agents2 = ctrl.fetch_agents()
        listbox_agents2.insert(END, *list_agents2)

        return lebel1, listbox_agents1, lebel_Vs, listbox_agents2

    def get_name(self):
        return 'S3AgentsSegment.py'
