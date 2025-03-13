from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Electric Car Controller')
root.geometry("800x600")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

spe_total = StringVar(value='0')
time_total = StringVar(value='0')
start_op = StringVar(value='')

def sub(total):
    try:
        value = int(total.get())
        if value > 0:
            total.set(value - 1)
    except ValueError:
        pass

def add(total):
    try:
        value = int(total.get())
        total.set(value + 1)
    except ValueError:
        pass

def start():
    pass   
    ''' SHEELLLL, the button to start the car calls this function, time_total 
is the total time the user inputs (no units, interpret as you will), spe_total is the same but for speed, and start_op is the 
option the user selects via the radio buttons at the bottom. It contains a string that
will read either speed or time (exactly as I have shown). When no button has been selected yet it reads ''. 
'''

def reset():
   spe_total.set('0')
   time_total.set('0')

def layout(parent, title, total):
    ttk.Label(parent, text=title, anchor='center').grid(column=2, row=0, sticky='nsew', padx=5, pady=5)
    ttk.Button(parent, text='Decrease', command=lambda: sub(total)).grid(column=0, row=1, sticky='nsew', padx=5, pady=5)
    ttk.Button(parent, text='Increase', command=lambda: add(total)).grid(column=4, row=1, sticky='nsew', padx=5, pady=5)
    ttk.Label(parent, textvariable=total, anchor='center').grid(column=2, row=2, sticky='nsew', padx=5, pady=5)
    
def config(parent, col_num, row_num, col_weight, row_weight):
    for i in range(col_num):
        parent.columnconfigure(i, weight=col_weight)
    for i in range(row_num):
        parent.rowconfigure(i, weight=row_weight)

content = ttk.Frame(root)
content.grid(column=0, row=0, sticky='nsew')
content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=1)

mainframe = ttk.Frame(content, borderwidth=5, relief='ridge')
mainframe.grid(column=0, row=0, sticky='nsew')
mainframe.grid_propagate(False)

config(mainframe, 1, 4, 1, 1)

title_frame = ttk.Frame(mainframe, borderwidth=5)
topframe = ttk.Frame(mainframe, borderwidth=5, relief='ridge')
bottomframe = ttk.Frame(mainframe, borderwidth=5, relief='ridge')
begin = ttk.Frame(mainframe, borderwidth=5)

title_frame.grid(column=0, row=0, sticky='nsew', padx=5, pady=5)
topframe.grid(column=0, row=1, sticky='nsew', padx=5, pady=5)
bottomframe.grid(column=0, row=2, sticky='nsew', padx=5, pady=5)
begin.grid(column=0, row=3, sticky='nsew', padx=5, pady=5)

config(topframe, 5, 3, 1, 1)
config(bottomframe, 5, 3, 1, 1)
config(title_frame, 5, 1, 1, 1)
config(begin, 3, 1, 1, 1)


title = ttk.Label(title_frame, text="Lucy's Electric Car Controller", anchor='center').grid(column=2, row=0, sticky='nsew')
res = ttk.Button(topframe, text='Reset Values', command=reset)
res.grid(column=0, row=0, sticky='nsew', padx=20, pady=20)
s_spe = Scale(topframe, borderwidth=10, resolution=5, variable=spe_total, showvalue=0, from_ = 0, to = 30, orient = HORIZONTAL)
s_spe.grid(column=1, row=1, columnspan=3, sticky='nsew', padx=5, pady=5)
s_time = Scale(bottomframe, borderwidth=10, variable=time_total, resolution=5, showvalue=0, from_ = 0, to = 30, orient = HORIZONTAL)
s_time.grid(column=1, row=1, columnspan=3, sticky='nsew', padx=5, pady=5)
start_button = ttk.Button(begin, text='Start Car', command=start)
start_button.grid(column=0, row=0, sticky='nsew', padx=10, pady=1)
speed_button = ttk.Radiobutton(begin, text="Speed", variable=start_op, value='speed')
distance_button = ttk.Radiobutton(begin, text="Time", variable=start_op, value='time')
speed_button.grid(column=1, row=0, sticky='nsew', padx=5, pady=1)
distance_button.grid(column=2, row=0, sticky='nsew', padx=5, pady=1)


layout(topframe, 'Speed', spe_total)
layout(bottomframe, 'Time', time_total)

root.mainloop()
