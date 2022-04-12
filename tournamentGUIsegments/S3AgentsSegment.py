from abc import ABC
from core.AbstractGUISegment import SegmentInterface
from tkinter import Frame, StringVar, Listbox, END, Label


class S3AgentsSegment(SegmentInterface, ABC):

    def get_widget(self):
        frame = self.get_frame()

        frame_left = Frame(master=frame)
        frame_left.pack(side='left')

        frame_right = Frame(master=frame)
        frame_right.pack(side='left')

        lebel1 = Label(master=frame_left, text='Agent ')

        listbox_agents1 = Listbox(master=frame_left, width=25, exportselection=0)
        list_agents1 = ['agent 1', 'agent 2', 'agent 3', 'agent 4']
        listbox_agents1.insert(END, *list_agents1)

        lebel_Vs = Label(master=frame_left, text='Vs  Opponents ')

        listbox_agents2 = Listbox(master=frame_right, width=25, selectmode="multiple", exportselection=0)
        list_agents2 = ['agent 1', 'agent 2', 'agent 3', 'agent 4']
        listbox_agents2.insert(END, *list_agents2)

        return lebel1, listbox_agents1, lebel_Vs, listbox_agents2

    def get_name(self):
        return 'S3AgentsSegment.py'
