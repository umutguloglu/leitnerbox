import tkinter as tk
from tkinter import ttk
import json 

# Initial Geometry Arrangements
window = tk.Tk()
my_width = window.winfo_screenwidth()
my_height= window.winfo_screenheight()
window_width = 1080
window_height= 650
left_sp = int((my_width - window_width)/2)
top_sp=int((my_height-window_height)/2)
window.geometry(f'{window_width}x{window_height}+{left_sp}+{top_sp}')
window.title('Leitner Box')
window.minsize(200,100)
window.bind('<Escape>', lambda event: window.quit())

# Creating Frames
label1 = ttk.Label(window, text = 'A', font= 'Calibri 24 bold')
#label1.pack()

# Configuring Columns
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 5)
window.columnconfigure(2, weight = 1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=15)



label2 = ttk.Label(window, text = 'A', font= 'Calibri 24 bold' , background= 'red')
label3 = ttk.Label(window, text = 'A', font= 'Calibri 24 bold' , background= 'blue')
label4 = ttk.Label(window, text = 'A', font= 'Calibri 24 bold' , background= 'green')

label1.grid( row=0, column=1)
label2.grid( row=1, column=0, sticky='nsew')
label3.grid( row=1, column=1, sticky='nsew')
label4.grid( row=1, column=2, sticky='nsew')

# Loading Config File
with open('Words.json','r') as f:
    general_dict = json.load(f)

print(general_dict['Dates'][55])


'''
        ttk.Label(aw_pos_frame , text='Type of the Word:').pack(side='left',expand=True)
        pos_list = ('Noun (n)', 'Adjective (Adj)', 'Verb (V)', 'Adverb (Adv)', 'Preposition (Prep)', 'Conjunction (Conj)')
        pos_combobox = ttk.Combobox(aw_pos_frame, name='choose', textvariable=aw_pos)
        pos_combobox['values'] = pos_list
        pos_combobox.pack(side='left',expand=True)
        aw_pos_frame.pack(fill='x')
'''





window.mainloop()

