import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Frame


class Charts:

    def scatter_chart(self, data, col_name1: str, col_name2: str, frame: Frame, position: str):
        df = pd.DataFrame(data, columns=[col_name1, col_name2])
        figure = plt.Figure(figsize=(5, 4), dpi=100)
        ax = figure.add_subplot(111)
        ax.scatter(df[col_name1], df[col_name2], color='r')
        scatter_plt = FigureCanvasTkAgg(figure, frame)
        scatter_plt.get_tk_widget().pack(side=position, fill='both')
        ax.legend(['Bids'])
        ax.set_xlabel(col_name1)
        ax.set_ylabel(col_name2)
        ax.set_title(f'{col_name1} Vs. {col_name2}')