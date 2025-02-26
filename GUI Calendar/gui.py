from tkinter import *
import calendar

def calendar_see():
    window = Tk()
    window.config(background="light pink")
    window.title("The Calendar")
    window.geometry("550x575")
    get_year = int(year_entry.get())
    window_content = calendar.calendar(get_year)
    year_cal = Label(window, text=window_content, font=("Arial", 11, "bold"))
    year_cal.grid(row=5, column=1, padx=20)
    window.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.config(background="green")
    root.title("The Python Calendar")
    root.geometry("300x200")
    
    name = Label(root, text="Calendar", bg="light yellow", font=("Arial",14,"bold"))
    name.grid(row=1, column=1)
    
    year = Label(root, text="Enter the year", bg="light blue", font=("Arial",13,"bold"))
    year.grid(row=2, column=1)
    
    year_entry = Entry(root, font=("Arial", 13, "bold"))
    year_entry.grid(row=3, column=1)
    
    show_button = Button(root, text="Show me the Calendar!!", fg="dark red", bg="orange", font=("Times new roman", 13, "bold"), command=calendar_see)
    show_button.grid(row=4,column=1)

    
    
    
    root.mainloop()
    
    
    