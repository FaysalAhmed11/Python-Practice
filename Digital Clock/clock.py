from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title("Python Clock")

def current_time():
    display_time = time.strftime("%I:%M:%S %p")
    digital_clock.config(text=display_time)
    digital_clock.after(200, current_time)


digital_clock = Label(root, font=('Times New Roman', 120), bg='green', fg='red')
digital_clock.pack()

current_time()

root.mainloop()