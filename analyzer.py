import tkinter as tk
from df_handler import Df_handler

root = tk.Tk()
df_handler = Df_handler()

canvas = tk.Canvas(root, width=500, height=500, bg='lightsteelblue')
canvas.pack()



browseButton_Excel = tk.Button(text='Import Excel File', command=lambda: df_handler.getExcel(), bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
canvas.create_window(250, 250, window=browseButton_Excel)





root.mainloop()


'''

import pandas as pd

excel_file = r'Database/salaries.xls'

salaries = pd.read_excel(excel_file)
sorted_by_salary = salaries.sort_values(['סיכום ברוטו'], ascending=False)
print(sorted_by_salary['סיכום ברוטו'].head(5))
print(salaries.head(1))
'''