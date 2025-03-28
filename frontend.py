from tkinter import *
from tkinter import ttk
import time
import board
import busio
from adafruit_mcp4725 import MCP4725
import RPi.GPIO as GPIO
import backend

root = Tk()
root.title('Electric Car Controller')
root.geometry("800x600")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

spe_total = StringVar(value='0')
time_total = StringVar(value='0')
start_op = StringVar(value='')

i2c, dac = backend.initialize()

def sub(total, min_val, change):
    try:
        value = int(total.get())
        if value > min_val:
            total.set(value - change)
    except ValueError:
        pass

def add(total, max_val, change):
    try:
        value = int(total.get())
        if value < max_val:
            total.set(value + change)
    except ValueError:
        pass

def start():
    start_button.config(state='disabled')
    start_button.config(state='normal')

def reset():
   spe_total.set('0')
   time_total.set('0')

def layout(parent, title, total, unit, min_val, max_val, change):
    ttk.Label(parent, text=title, anchor='center').grid(column=2, row=0, sticky='nsew', padx=5, pady=5)
    ttk.Button(parent, text='Decrease', command=lambda: sub(total, min_val, change)).grid(column=0, row=1, sticky='nsew', padx=5, pady=5)
    ttk.Button(parent, text='Increase', command=lambda: add(total, max_val, change)).grid(column=5, row=1, sticky='nsew', padx=5, pady=5)
    ttk.Label(parent, textvariable=total, anchor='e').grid(column=2, row=2, sticky='nsew', padx=0, pady=5)
    ttk.Label(parent, text=unit, anchor='w').grid(column=3, row=2, sticky='nsew', padx=0, pady=5)    

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

config(topframe, 6, 3, 1, 1)
config(bottomframe, 6, 3, 1, 1)
config(title_frame, 5, 1, 1, 1)
config(begin, 3, 1, 1, 1)

def test():
    start_button.config(state='disabled')
    print('Button disabled')
    time.sleep(5)

def wrapper(dac, i2c, spe_total, time_total):

    start_button.config(state='disabled')

    output_voltage = ((3 - 2.5) * (int(spe_total.get()) / 100)) + 2.5

    backend.volt(dac=dac, i2c=i2c, output_voltage=output_voltage, duration=int(time_total.get()))

    time.sleep(int(time_total.get()))

    dac.raw_value = 0

    start_button.config(state='normal')

title = ttk.Label(title_frame, text="Lucy's Electric Car Controller", anchor='center').grid(column=2, row=0, sticky='nsew')
res = ttk.Button(topframe, text='Close program', command=lambda: backend.reset(dac, i2c))
res.grid(column=0, row=0, sticky='nsew', padx=20, pady=20)
s_spe = Scale(topframe, borderwidth=10, resolution=5, variable=spe_total, showvalue=0, from_ = 0, to = 100, orient = HORIZONTAL)
s_spe.grid(column=1, row=1, columnspan=3, sticky='nsew', padx=5, pady=5)
s_time = Scale(bottomframe, borderwidth=10, variable=time_total, resolution=1, showvalue=0, from_ = 0, to = 15, orient = HORIZONTAL)
s_time.grid(column=1, row=1, columnspan=3, sticky='nsew', padx=5, pady=5)


# start_button = ttk.Button(begin, text='Start Car', command=lambda: backend.volt(dac=dac, i2c=i2c, output_voltage=3, duration=3))
start_button = ttk.Button(begin, text='Start Car', command=lambda: wrapper(dac=dac, i2c=i2c, spe_total=spe_total, time_total=time_total))
start_button.grid(column=0, row=0, sticky='nsew', padx=10, pady=1)
speed_button = ttk.Radiobutton(begin, text="Speed", variable=start_op, value='speed')
distance_button = ttk.Radiobutton(begin, text="Time", variable=start_op, value='time')
#speed_button.grid(column=1, row=0, sticky='nsew', padx=5, pady=1)
#distance_button.grid(column=2, row=0, sticky='nsew', padx=5, pady=1)


layout(topframe, 'Speed', spe_total, '%', 0, 100, 1)
layout(bottomframe, 'Time', time_total, 's', 0, 15, 1)

root.mainloop()
