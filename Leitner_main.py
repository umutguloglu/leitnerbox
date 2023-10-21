import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json 

import array as arr
import random

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
                now_1.set(general_dict['Groups'][0]['Number of Words'] +1)
                general_dict['Groups'][0]['Number of Words'] = int(now_1.get())
                json.dump(general_dict,f,indent=4)

            messagebox.showinfo('Succesful!','The word is added to the dictionary successfully.',parent=self)
            self.destroy()
         
def addWordWindow():
    add_word_window()

def editWordWindow():
    pass

def startShowWindow():
    global current_index
    global selected_words
    global length
    global selected_group

    outputtxt['state'] = 'disabled'
    show_def_button['state'] = 'enabled'
    current_index = 0
    if show_1.get()==True:
        disable_checks()
        length = int(now_1.get())
        screen_words = general_dict['Groups'][0]["Words"]    
        selected_group = 1
    elif show_2.get()==True:
        disable_checks()
        length = int(now_2.get())
        screen_words = general_dict['Groups'][1]["Words"]    
        selected_group = 2
    elif show_3.get()==True:
        disable_checks()
        length = int(now_3.get())
        screen_words = general_dict['Groups'][2]["Words"]    
        selected_group = 3 
    elif show_4.get()==True:
        disable_checks()
        length = int(now_4.get())
        screen_words = general_dict['Groups'][3]["Words"]    
        selected_group = 4 
    elif show_5.get()==True:
        disable_checks()
        length = int(now_5.get())
        screen_words = general_dict['Groups'][4]["Words"]    
        selected_group = 5 
    elif show_6.get()==True:
        disable_checks()
        length = int(now_6.get())
        screen_words = general_dict['Groups'][5]["Words"]    
        selected_group = 6 
    elif show_7.get()==True:
        disable_checks()
        length = int(now_7.get())
        screen_words = general_dict['Groups'][6]["Words"]    
        selected_group = 7 
    else:
        messagebox.showerror('Error!','Please select a group.')
        return -1
    if length>0:
        selected_words = random.sample(screen_words,length)
        screen_play()
    elif length==0:
        messagebox.showerror('Error!','There is not any object in that group.')
        enable_checks()
    else:
        messagebox.showerror('Error!','There is something wrong about the length. Call Umut.')
        enable_checks()

def screen_play():
    outputtxt.delete('1.0', tk.END)
    outputtxt['state'] = 'disabled'
    global current_index
    selected_name= selected_words[current_index]['Name']
    selected_pos = selected_words[current_index]['Pos'] 
    selected_ex  = selected_words[current_index]["Example"]
    if selected_ex == "":
        txt_file = f'{selected_pos} -- {selected_name} \n'
    else:
        txt_file = f'{selected_pos} -- {selected_name} \nEXAMPLE: {selected_ex}'
    inputtxt.delete('1.0', tk.END)
    inputtxt.insert('1.0', txt_file)


def screen_answer():
    show_def_button['state'] = 'disabled'
    correct_def_button['state'] = 'normal'
    false_def_button['state'] = 'normal'
    outputtxt['state'] = 'normal'
    global current_index
    selected_def = selected_words[current_index]["Definition"]
    outputtxt.delete('1.0', tk.END)
    outputtxt.insert('1.0', selected_def)
    
    pass

def correct_answer():
    global current_index
    global selected_group

    show_def_button['state'] = 'normal'
    correct_def_button['state'] = 'disabled'
    false_def_button['state'] = 'disabled'
    '''
    general_dict['Groups'][selected_group-1]['Number of Words'] = general_dict['Groups'][selected_group-1]['Number of Words'] - 1
    general_dict['Groups'][selected_group]['Number of Words'] = general_dict['Groups'][selected_group]['Number of Words'] + 1
    '''
    general_dict['Groups'][selected_group-1]['Words'].remove(selected_words[current_index])
    general_dict['Groups'][selected_group]['Words'].append(selected_words[current_index])

    with open("Words.json", "w") as f:
        renew_now(selected_group,-1)
        renew_now(selected_group+1,1)
        json.dump(general_dict,f,indent=4)

    current_index = current_index + 1
    if current_index < length:
        screen_play()
    else:
        messagebox.showinfo('Completed', f'Group {selected_group} is completed.')
        show_def_button['state'] = 'disabled'
        enable_checks()
        outputtxt.delete('1.0', tk.END)
        inputtxt.delete('1.0', tk.END)
        outputtxt['state'] = 'disabled'
    pass

def false_answer():
    global current_index
    global selected_group

    show_def_button['state'] = 'normal'
    correct_def_button['state'] = 'disabled'
    false_def_button['state'] = 'disabled'
    '''
    general_dict['Groups'][selected_group-1]['Number of Words'] = general_dict['Groups'][selected_group-1]['Number of Words'] - 1
    general_dict['Groups'][0]['Number of Words'] = general_dict['Groups'][0]['Number of Words'] + 1
    '''
    general_dict['Groups'][selected_group-1]['Words'].remove(selected_words[current_index])
    general_dict['Groups'][0]['Words'].append(selected_words[current_index])

    with open("Words.json", "w") as f:
        renew_now(selected_group,-1)
        renew_now(1,1)
        json.dump(general_dict,f,indent=4)






    current_index = current_index + 1
    if current_index < length:
        screen_play()
    else:
        messagebox.showinfo('Completed', f'Group {selected_group} is completed.')
        show_def_button['state'] = 'disabled'
        enable_checks()
        outputtxt.delete('1.0', tk.END)
        inputtxt.delete('1.0', tk.END)
        outputtxt['state'] = 'disabled'
    pass

def disable_checks():
    check_1['state'] = 'disabled'
    check_2['state'] = 'disabled'
    check_3['state'] = 'disabled'
    check_4['state'] = 'disabled'
    check_5['state'] = 'disabled'
    check_6['state'] = 'disabled'
    check_7['state'] = 'disabled'

def enable_checks():
    check_1['state'] = 'enable'
    check_2['state'] = 'enable'
    check_3['state'] = 'enable'
    check_4['state'] = 'enable'
    check_5['state'] = 'enable'
    check_6['state'] = 'enable'
    check_7['state'] = 'enable'

def renew_now(selected_group,change):
    if selected_group == 1:
        now_1.set(general_dict['Groups'][selected_group - 1]['Number of Words'] + change)
        general_dict['Groups'][selected_group - 1]['Number of Words'] = int(now_1.get())
    elif selected_group == 2:
        now_2.set(general_dict['Groups'][selected_group - 1]['Number of Words'] + change)
        general_dict['Groups'][selected_group - 1]['Number of Words'] = int(now_2.get())
    elif selected_group == 3:
        now_3.set(general_dict['Groups'][selected_group - 1]['Number of Words'] + change)
        general_dict['Groups'][selected_group - 1]['Number of Words'] = int(now_3.get())
    elif selected_group == 4:
        now_4.set(general_dict['Groups'][selected_group - 1]['Number of Words'] + change)
        general_dict['Groups'][selected_group - 1]['Number of Words'] = int(now_4.get())
    elif selected_group == 5:
        now_5.set(general_dict['Groups'][selected_group - 1]['Number of Words'] + change)
        general_dict['Groups'][selected_group - 1]['Number of Words'] = int(now_5.get())
    elif selected_group == 6:
        now_6.set(general_dict['Groups'][selected_group - 1]['Number of Words'] + change)
        general_dict['Groups'][selected_group - 1]['Number of Words'] = int(now_6.get())
    elif selected_group == 7:
        now_7.set(general_dict['Groups'][selected_group - 1]['Number of Words'] + change)
        general_dict['Groups'][selected_group - 1]['Number of Words'] = int(now_7.get())
    return
    '''
    elif selected_group == 8:
        now_8.set(general_dict['Groups'][selected_group - 1]['Number of Words'] + change)
        general_dict['Groups'][selected_group - 1]['Number of Words'] = int(now_8.get())
    '''    





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
window.bind('<Escape>', lambda event: window.quit())  # Change it

# Loading Config File
with open('Words.json','r') as f:
    general_dict = json.load(f)

# Check whether the number of words match with the real ones
for x in range(7):
    if(len(general_dict['Groups'][x]['Words']) != general_dict['Groups'][x]['Number of Words']):
        print(len(general_dict['Groups'][x]['Words']) != general_dict['Groups'][x]['Number of Words'])
        messagebox.showerror('Possible Fundemental Error!','Consult Umut')
        print(len(general_dict['Groups'][x]['Words']))
        print(general_dict['Groups'][x]['Number of Words'])
        general_dict['Groups'][x]['Number of Words'] = len(general_dict['Groups'][x]['Words'])
        print(x)

# Check the Current Day and Group
current_day = general_dict['Track']['Day']
current_group = general_dict['Dates'][(current_day-1)%64]
current_index = 0

# Creating Frames
top_frame   = ttk.Frame(window)
bottom_frame= ttk.Frame(window)
left_frame  = ttk.Frame(bottom_frame)
main_frame  = ttk.Frame(bottom_frame)
right_frame = ttk.Frame(bottom_frame)
no_words_frame = tk.Frame(left_frame)
no_words_label_frame = tk.Frame(no_words_frame)
no_words_number_frame = tk.Frame(no_words_frame)


# Defining Variables
aw_pos  = tk.StringVar()
aw_name = tk.StringVar()
aw_def  = tk.StringVar()
#aw_ex   = tk.StringVar()

now_1 = tk.StringVar(master = no_words_number_frame, value=general_dict['Groups'][0]['Number of Words'])
now_2 = tk.StringVar(master = no_words_number_frame, value=general_dict['Groups'][1]['Number of Words'])
now_3 = tk.StringVar(master = no_words_number_frame, value=general_dict['Groups'][2]['Number of Words'])
now_4 = tk.StringVar(master = no_words_number_frame, value=general_dict['Groups'][3]['Number of Words'])
now_5 = tk.StringVar(master = no_words_number_frame, value=general_dict['Groups'][4]['Number of Words'])
now_6 = tk.StringVar(master = no_words_number_frame, value=general_dict['Groups'][5]['Number of Words'])
now_7 = tk.StringVar(master = no_words_number_frame, value=general_dict['Groups'][6]['Number of Words'])

label3 = ttk.Label(main_frame, text = 'A', font= 'Calibri 24 bold')
label4 = ttk.Label(right_frame, text = 'General Info', font= 'Calibri 24 bold' , background= 'green')
 
# Top Frame
ttk.Label(top_frame, text = 'Online Leitner Box', font= 'Calibri 24 bold', background='orange').pack(side= 'top')
top_frame.pack()

# Left Frame
label2 = ttk.Label(left_frame, text = 'General Info', font= 'Calibri 24 bold' , background= 'red')
no_words_headline = ttk.Label(no_words_frame, text = 'Number of Words In Each Group', font= 'Calibri 12 italic' , background= 'orange')

label2.pack(side='top',fill = 'both')
no_words_headline.pack()
ttk.Label(no_words_label_frame, text = 'Group 1: ', font= 'Calibri 12').pack()
ttk.Label(no_words_label_frame, text = 'Group 2: ', font= 'Calibri 12').pack()
ttk.Label(no_words_label_frame, text = 'Group 3: ', font= 'Calibri 12').pack()
ttk.Label(no_words_label_frame, text = 'Group 4: ', font= 'Calibri 12').pack()
ttk.Label(no_words_label_frame, text = 'Group 5: ', font= 'Calibri 12').pack()
ttk.Label(no_words_label_frame, text = 'Group 6: ', font= 'Calibri 12').pack()
ttk.Label(no_words_label_frame, text = 'Group 7: ', font= 'Calibri 12').pack()

ttk.Label(no_words_number_frame, textvariable = now_1, font= 'Calibri 12').pack()
ttk.Label(no_words_number_frame, textvariable = now_2, font= 'Calibri 12').pack()
ttk.Label(no_words_number_frame, textvariable = now_3, font= 'Calibri 12').pack()
ttk.Label(no_words_number_frame, textvariable = now_4, font= 'Calibri 12').pack()
ttk.Label(no_words_number_frame, textvariable = now_5, font= 'Calibri 12').pack()
ttk.Label(no_words_number_frame, textvariable = now_6, font= 'Calibri 12').pack()
ttk.Label(no_words_number_frame, textvariable = now_7, font= 'Calibri 12').pack()

no_words_label_frame.pack(side='left')
no_words_number_frame.pack(expand=True, side='left')

no_words_frame.pack(pady=10)
ttk.Label(left_frame, text = f'Currently, you are in Day: {current_day}').pack()
ttk.Label(left_frame, text = f'Today\'s repeat group: {current_group}').pack()
left_frame.pack(side='left',fill='both')

# Main Frame
button_frame = tk.Frame(main_frame)
start_show_frame = tk.Frame(main_frame)
check_frame = tk.Frame(start_show_frame)

show_frame = tk.Frame(main_frame)

ttk.Button(button_frame, text='Add a new word', command=addWordWindow).pack(side='left')
ttk.Button(button_frame, text='Edit a word', command=editWordWindow).pack(side='left')
button_frame.pack()

show_1 = tk.BooleanVar(value=False)
show_2 = tk.BooleanVar(value=False)
show_3 = tk.BooleanVar(value=False)
show_4 = tk.BooleanVar(value=False)
show_5 = tk.BooleanVar(value=False)
show_6 = tk.BooleanVar(value=False)
show_7 = tk.BooleanVar(value=False)

check_1 = ttk.Checkbutton(check_frame, text = '1', variable=show_1 )
check_1.pack(side='left')
check_2 = ttk.Checkbutton(check_frame, text = '2', variable=show_2 )
check_2.pack(side='left')
check_3= ttk.Checkbutton(check_frame, text = '3', variable=show_3 )
check_3.pack(side='left')
check_4 = ttk.Checkbutton(check_frame, text = '4', variable=show_4 )
check_4.pack(side='left')
check_5 = ttk.Checkbutton(check_frame, text = '5', variable=show_5 )
check_5.pack(side='left')
check_6 = ttk.Checkbutton(check_frame, text = '6', variable=show_6 )
check_6.pack(side='left')
check_7 = ttk.Checkbutton(check_frame, text = '7', variable=show_7 )
check_7.pack(side='left')

start_show_button = ttk.Button(start_show_frame, text='Start Showing the Words', command=startShowWindow)
start_show_button.pack()
check_frame.pack()

start_show_frame.pack()

tk.Label(show_frame,text='The Word').pack()
inputtxt = tk.Text(show_frame, height = 5,
                width = 50,
                bg = "light yellow")
inputtxt.pack()
tk.Label(show_frame,text='Definition').pack(pady=3)
outputtxt = tk.Text(show_frame, height = 5, 
              width = 50, 
              bg = "light cyan")
outputtxt.pack(pady=5)
show_def_button = ttk.Button(show_frame, text='Show The Answer' , command=screen_answer)

show_def_button.pack(pady=5)
correct_false_frame = tk.Frame(show_frame)
correct_def_button = ttk.Button(correct_false_frame, text='Correct Answer' , command=correct_answer)
correct_def_button.pack(side='left')
false_def_button = ttk.Button(correct_false_frame, text='False Answer' , command=false_answer)
false_def_button.pack(side='left')
correct_false_frame.pack()
show_frame.pack(expand=True, fill = 'both', pady=30)
main_frame.pack(side='left',expand=True,fill='both')

show_def_button['state'] = 'disabled'
correct_def_button['state'] = 'disabled'
false_def_button['state'] = 'disabled'

# Right Frame
label4.pack(fill = 'both')
#right_frame.pack(side='left',fill='both')

bottom_frame.pack(expand=True,fill='both', pady=30)


print(general_dict['Dates'][55])






window.mainloop()

