import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json 

# ------------------------------- Defined Functions and Classes for CallBacks ----------------------------------

class add_word_window(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Add a New Word')
        self.geometry(f'{add_word_width}x{add_word_height}+{add_word_left_sp}+{add_word_top_sp}')
        self.attributes('-topmost', True)
        
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 5)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)
        self.rowconfigure(3,weight=1)
        self.rowconfigure(4,weight=1)
        self.rowconfigure(5,weight=1)

        aw_pos_frame= tk.Frame(self)
        aw_name_frame = tk.Frame(self)
        aw_def_frame= tk.Frame(self)
        aw_ex_frame= tk.Frame(self)

        # General Part
        #tk.Label(self, text='Please fill the required parts and click \'Add\'', font='Calibri 15 italic').pack(pady=7)
        tk.Label(self, text='Please fill the required parts and click \'Add\'', font='Calibri 15 italic').grid( row=0, column=0,columnspan=2)
       
        # POS part
        ttk.Label(self , text='Type of the Word:').grid( row=1, column=0)
        pos_list = ('Noun (n)', 'Adjective (Adj)', 'Verb (V)', 'Adverb (Adv)', 'Preposition (Prep)', 'Conjunction (Conj)')
        pos_combobox = ttk.Combobox(self, name='choose', textvariable=aw_pos)
        pos_combobox['values'] = pos_list
        pos_combobox.grid(row=1,column=1)

        # Name part
        ttk.Label(self , text='Name of the Word:').grid(row=2,column=0)
        name_entry = ttk.Entry(self, textvariable=aw_name).grid(row=2,column=1)

        # Definition part
        ttk.Label(self , text='Definition of the Word:').grid(row=3,column=0)
        def_entry = ttk.Entry(self, textvariable=aw_def).grid(row=3,column=1,sticky='nwes')

        # Example part
        global aw_ex
        ttk.Label(self , text='Example in a sentence (Optional)').grid(row=4,column=0)
        aw_ex = tk.Text(self, width=32, height=8)
        aw_ex.grid(row=4,column=1)

        # OK Button
        ttk.Button(self, text='Add this word to the dictionary.' , command=self.addWord).grid(row=5,column=0,columnspan=2)

    def addWord(self):
        new_name = aw_name.get().capitalize()
        new_pos = aw_pos.get().capitalize()
        new_def = aw_def.get().capitalize()
        new_ex = aw_ex.get("1.0",'end-1c').capitalize()
        halt = False
        if new_name=="":
            messagebox.showerror('Error!','Please fill the name of the word.',parent=self)
            halt=True
        elif new_pos=="":
            messagebox.showerror('Error!','Please fill the type of the word.',parent=self)
            halt=True
        elif new_def=="":
            messagebox.showerror('Error!','Please fill the definition of the word.',parent=self)
            halt=True
        else:
            for x in range(7):        
                for eachword in general_dict['Groups'][x]["Words"]: #Controls whether the same word exists.
                    if eachword['Name']==new_name :
                        messagebox.showerror('Error!','This word already exists in the dictionary.',parent=self)
                        halt = True
                if halt==True:
                    break
        if halt == False:
            desc=dict()
            desc['Name'] = new_name
            desc['Pos'] = new_pos
            desc["Definition"]=new_def
            desc["Example"]=new_ex

            with open("Words.json", "w") as f:
                general_dict['Groups'][0]["Words"].append(desc)
                json.dump(general_dict,f,indent=4)

            messagebox.showinfo('Succesful!','The word is added to the dictionary successfully.',parent=self)
            self.destroy()
         
def addWordWindow():
    add_word_window()


# ------------------------------------------------ END ----------------------------------------------------------

# Initial Geometry Arrangements
window = tk.Tk()
my_width = window.winfo_screenwidth()
my_height= window.winfo_screenheight()
window_width = 1080
window_height= 550
add_word_width = 500
add_word_height = 300
left_sp = int((my_width - window_width)/2)
top_sp=int((my_height-window_height)/2)
add_word_left_sp = int((my_width - add_word_width)/2)
add_word_top_sp=int((my_height-add_word_height)/2)
window.geometry(f'{window_width}x{window_height}+{left_sp}+{top_sp}')
window.title('Leitner Box')
window.minsize(200,100)
window.bind('<Escape>', lambda event: window.quit())

# Defining Variables
aw_pos  = tk.StringVar()
aw_name = tk.StringVar()
aw_def  = tk.StringVar()
#aw_ex   = tk.StringVar()

# Loading Config File
with open('Words.json','r') as f:
    general_dict = json.load(f)

# Creating Frames
top_frame   = ttk.Frame(window)
bottom_frame= ttk.Frame(window)
left_frame  = ttk.Frame(bottom_frame)
main_frame  = ttk.Frame(bottom_frame)
right_frame = ttk.Frame(bottom_frame)

label1 = ttk.Label(top_frame, text = 'A', font= 'Calibri 24 bold', background='orange')
label2 = ttk.Label(left_frame, text = 'General Info', font= 'Calibri 24 bold' , background= 'red')
label3 = ttk.Label(main_frame, text = 'A', font= 'Calibri 24 bold')
label4 = ttk.Label(right_frame, text = 'A', font= 'Calibri 24 bold' , background= 'green')
add_word_button = ttk.Button(main_frame, text='Add a new word', command=addWordWindow)

# Top Frame
label1.pack(side= 'top')
top_frame.pack()

# Left Frame
label2.pack(side='top',fill = 'both')
left_frame.pack(side='left',fill='both')

# Main Frame
add_word_button.pack(side='top')
label3.pack(expand=True, fill = 'both')

main_frame.pack(side='left',expand=True,fill='both')

# Right Frame
label4.pack(expand=True, fill = 'both')
right_frame.pack(side='left',fill='both')

bottom_frame.pack(expand=True,fill='both')


print(general_dict['Dates'][55])






window.mainloop()

