import tkinter as tk
import CreateObjectByPath
from configurations import *
from controller import Controller

class GUIsegments:

    def __init__(self, window, segments_path: str):
        self.window = window
        self.controller = Controller()
        package_name = segments_path.split("./")[1]
        self.create_sessionGUI(segments_path, package_name)


    def create_sessionGUI(self, segments_path, package_name):
        if package_name == SESSION_GUI_PACKAGE_NAME:
            segments_names = self.controller.fetch_session_gui_segments()
        elif package_name == TOURNAMENT_GUI_PACKAGE_NAME:
            segments_names = self.controller.fetch_tournament_gui_segments()
        else:
            raise ValueError('There is no package_name')
        widgets = []
        frames = []
        var_dict = {}
        segments = []
        for segments_name in segments_names:
            var_dict[segments_name] = tuple(tk.StringVar() for x in range(10))

        for segments_name in segments_names:
            frame = tk.Frame(master=self.window)
            frames.append(frame)
            obj = CreateObjectByPath.get_object(segments_path, segments_name, frame, var_dict)
            segments.append(obj)
            widgets_row = obj.get_widget()
            widgets.append(widgets_row)

        all_widgets_in_Gui = {}
        i = 0
        for widgets_row in widgets:
            frames[i].pack(side='top')
            all_row_widgets = []
            for widget_col in widgets_row:
                widget_col.pack(side='left', padx=5, pady=5)
                all_row_widgets.append(widget_col)
            all_widgets_in_Gui[i] = all_row_widgets
            i += 1

        for obj in segments:
            obj.set_gui_widgets(all_widgets_in_Gui)
