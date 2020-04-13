from tkinter import filedialog
import pandas as pd

import matplotlib.pyplot as plt

class Df_handler:
    def __init__(self):
        self.df = None

    def getExcel(self):
        import_file_path = filedialog.askopenfilename()
        self.df = pd.read_excel(import_file_path)
        print(self.df)

    def printPlot(self):
        plt.plot(self.df['סיכום ברוטו'],self.df['מס הכנסה'])
        plt.xlable('סיכום ברוטו')
        plt.ylable('מס הכנסה')
        plt.title('יחס שכר\מס')
        plt.legend()
        print(self.df)
