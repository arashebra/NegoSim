from abc import ABC, abstractmethod
from tkinter import Frame, StringVar


class SegmentInterface(ABC):

    @abstractmethod
    def get_widget(self, frame: Frame, *string_var: StringVar) -> tuple:
        '''
        :param frame:
        :param string_var:
        :return: tuple ([widget1, widget2, ...], row)
        '''
        raise NotImplementedError
