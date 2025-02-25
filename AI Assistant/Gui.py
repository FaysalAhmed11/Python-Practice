from tkinter import*
from PIL import Image, ImageTk
import action_operator
import speech_to_text

root = Tk()
root.title("Faysal's AI Assistant")
root.geometry("700x750")
root.resizable(False, False)
root.config(bg="#800000")


#ask function
def ask():
    send = entry1.get()
    bot = action_operator.action_fun(send)
    text.insert(END, "Me --> "+send+"\n")
    if bot != None:
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
          root.destroy()  
    
    
#send function
def send():
    ask_val= speech_to_text.speech_to_text_fun()
    bot_val = action_operator.action_fun(ask_val)
    text.insert(END, "Me --> "+ask_val+"\n") 
    if bot_val != None:
       text.insert(END, "Bot <-- "+ str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()


#Delete Function
def del_fun():
    text.delete("1.0", "end")

#Creating the frame
frame = LabelFrame(root, padx = 100, pady = 7, borderwidth= 3, relief= "raised")
frame.config(bg="#800000")
frame.grid(row = 0, column = 1, padx = 50, pady = 10)

#Text Label
text_label = Label(frame, text = "Faysal's AI", font =("Times New Roman", 14, "bold"), bg="#356696")
text_label.grid(row=0, column=0, padx = 20, pady = 10)

#adding image
image = ImageTk.PhotoImage(Image.open("Virtual Assistant.jpg"))
image_label = Label(frame, image=image)
image_label.grid(row = 1, column = 0, pady = 20)

#Text_Widget_Area
text_widget = Text(root, font=('Arial 10 bold'), bg='#0000FF')
text_widget.grid(row=2, column=0)
text_widget.place(x = 150, y = 425, width= 425, height=100)

#Entry of the Widget
entry = Entry(root, justify=CENTER)
entry.place(x = 150, y = 550, width= 425, height=50)

#Button1
Button1 = Button(root, text="ASK", bg="#356690", padx=40, pady=16, borderwidth=3, command=ask)
Button1.place(x=150, y=650)

#Button2
Button2 = Button(root, text="Send", bg="#356690", padx=40, pady=16, borderwidth=3, command=send)
Button2.place(x=440, y=650)

#Button3
Button3 = Button(root, text="Delete", bg="#356690", padx=40, pady=16, borderwidth=3, command=del_fun)
Button3.place(x=290, y=650)

root.mainloop()