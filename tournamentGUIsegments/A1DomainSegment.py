from abc import ABC
from core.SegmentInterface import SegmentInterface
from tkinter import Frame, StringVar, Listbox, END, Label


class A1DomainSegment(SegmentInterface, ABC):

    def get_widget(self):
        frame = self.get_frame()
        listbox_domain = Listbox(master=frame, width=50, selectmode="multiple", exportselection=0)
        list_domain = ['domain 1', 'domain 2', 'domain 3', 'domain 4']
        listbox_domain.insert(END, *list_domain)

        lebel_Vs = Label(master=frame, text='Domains ')

        return lebel_Vs, listbox_domain

    def get_name(self):
        return 'A1DomainSegment.py'
