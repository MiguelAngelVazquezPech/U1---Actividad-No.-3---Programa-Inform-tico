import tkinter as tk
from tkinter import Message, ttk
from tkinter import messagebox as MessageBox
#-----------------------------------------------------------------------------------------------
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Barra de progreso en Tk")
        self.progressbar = ttk.Progressbar(self , length=100, mode = "indeterminate")
        self.progressbar.place(x=25, y=35, width=200)
        self.place(width=300, height=200)
        main_window.geometry("250x100")
        self.progressbar.start(10)
        MessageBox.showinfo("¡EXITO!","Ejecucion Exitosa")
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()