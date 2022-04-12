import tkinter as tk
from configurations import *
import CreateObjectByPath
from controller import Controller


class Tournament:
    def __init__(self, window):
        self.window = window
        self.controller = Controller()
        self.create_tournament()

    def create_tournament(self):
        widget_names = self.controller.fetch_tournament_gui_segments()
        widgets = []
        frames = []
        var_dict = {}
        segments = []
        for widget_name in widget_names:
            var_dict[widget_name] = tuple(tk.StringVar() for x in range(10))

        for widget_name in widget_names:
            frame = tk.Frame(master=self.window)
            frames.append(frame)
            obj = CreateObjectByPath.get_object(TOURNAMENT_GUI_SEGMENT_PATH, widget_name, frame, var_dict)
            segments.append(obj)
            widgets_row = obj.get_widget()
            widgets.append(widgets_row)

        all_widgets_in_Gui = {}
        i = 0
        for widgets_row in widgets:
            frames[i].pack(side='top')
            all_row_widgets = []
            for widget_col in widgets_row:
                widget_col.pack(side='left', padx=5, pady=10)
                all_row_widgets.append(widget_col)
            all_widgets_in_Gui[i] = all_row_widgets
            i += 1

        for obj in segments:
            obj.set_gui_widgets(all_widgets_in_Gui)


    # def create_tournament(self):
    #     tournament_frame = tk.Frame(self.window)
    #     tournament_frame.grid(row=0, column=0, columnspan=10)
    #
    #     tk.Label(tournament_frame, text='Protocol ').grid(row=0, column=0)
    #
    #     protocol_list = ["Protocol 1", "Protocol 2",
    #                      "Protocol 3", "Protocol 4"]
    #     protocol_name = tk.StringVar()
    #     protocol_name.set("Select a Protocol")
    #     optionMenu_protocol = tk.OptionMenu(
    #         tournament_frame, protocol_name, *protocol_list)
    #     optionMenu_protocol.grid(
    #         row=0, column=1, columnspan=2, sticky='we')
    #
    #     tk.Label(tournament_frame, text='Domain ').grid(row=1, column=0)
    #
    #     domain_list = ["Domain 1", "Domain 2",
    #                    "Domain 3", "Domain 4"]
    #     domain_name = tk.StringVar()
    #     domain_name.set("Select a Domain")
    #     optionMenu_domain = tk.OptionMenu(
    #         tournament_frame, domain_name, *domain_list)
    #     optionMenu_domain.grid(row=1, column=1, columnspan=2, sticky='we')
    #
    #     ttk.Separator(tournament_frame, orient='horizontal').grid(
    #         row=2, column=0, columnspan=10, sticky='we')
    #
    #     tk.Label(tournament_frame, text=' Participant ').grid(
    #         row=3, column=1)
    #
    #     ttk.Separator(tournament_frame, orient='horizontal').grid(
    #         row=4, column=0, columnspan=10, sticky='we')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('New Tournament')
    # root.geometry('400x400')
    Tournament(root)
    root.mainloop()
