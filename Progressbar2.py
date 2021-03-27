import tkinter as kt
from tkinter import ttk
root = ttk()

def progress(currentValue,master):
    maxValue=100
    progressbar=ttk.Progressbar(master,orient="horizontal",length=300,mode="determinate")
    progressbar.pack(side=ttk.TOP)
    currentValue=0
    progressbar["value"]=currentValue
    progressbar["maximum"]=maxValue
    progressbar.place(x=25, y=35, width=200)
    progressbar.place(width=300, height=200)
    divisions=10
    for i in range(divisions):
        currentValue=currentValue+10
        progressbar.after(500, progress(currentValue))
        progressbar.update() # Force an update of the GUI
        
root.mainloop()