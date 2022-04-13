from abc import ABC
from core.AbstractGUISegment import SegmentInterface
from tkinter import Listbox, END, Label
from controller import Controller


class S2DomainSegment(SegmentInterface, ABC):

    def get_widget(self):
        ctrl = Controller()
        frame = self.get_frame()
        listbox_domain = Listbox(master=frame, width=50, selectmode="multiple", exportselection=0)
        list_domain = ctrl.fetch_domains()
        listbox_domain.insert(END, *list_domain)

        lebel_Vs = Label(master=frame, text='Domains ')

        return lebel_Vs, listbox_domain

    def get_name(self):
        return 'S2DomainSegment.py'
