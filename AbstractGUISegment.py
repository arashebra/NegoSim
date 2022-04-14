from abc import ABC, abstractmethod
from tkinter import Frame


class SegmentInterface(ABC):

    def __init__(self, frame: Frame, var_dict: dict):
        self.__frame = frame
        self.__var_dict = var_dict
        self.__gui_widgets_dict = {}

    def set_gui_widgets(self, gui_widgets_dict: dict):
        '''
        this method maintains all existing widgets in the Gui
        :param gui_widgets_dict:
        '''
        self.__gui_widgets_dict = gui_widgets_dict

    def get_gui_widgets(self):
        '''
        this method returns all existing widgets in the Gui
        :return: all existing widgets in the Gui
        '''
        return self.__gui_widgets_dict

    def get_frame(self):
        return self.__frame

    def get_var_dict(self):
        return self.__var_dict

    @abstractmethod
    def get_widget(self) -> tuple:
        '''
        :param var_dict:
        :param frame:
        :return: tuple ([widget1, widget2, ...], row)
        '''
        raise NotImplementedError

    @abstractmethod
    def get_name(self):
        raise NotImplementedError