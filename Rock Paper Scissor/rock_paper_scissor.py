# Import Required Library
from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Create Object
window = Tk()
window.title("Rock Paper Scissor")
window.configure(background="black")

image_rock1 = ImageTk.PhotoImage(Image.open("rock 1.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("paper 1.png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissor 1.png"))
image_rock2 = ImageTk.PhotoImage(Image.open("rock 2.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("paper 2.png"))
image_scissor2 = ImageTk.PhotoImage(Image.open("scissor 2.png"))

label_computer = Label(window, image= image_scissor2)
label_computer.grid(row=1, column=0)
label_player = Label(window, image=image_scissor1)
label_player.grid(row=1, column=4)

computer_score = Label(window, text=0, font=('arial', 60, "bold"), fg="red")
computer_score.grid(row=1, column=1)
player_score = Label(window, text =0, font=("arial",60, "bold"), fg="red")
player_score.grid(row=1, column=3)

computer_indicator = Label(window, font=('times new roman',40,'bold'),text="COMPUTER", bg="orange", fg="blue")
player_indicator = Label(window, font=("times new roman",40,"bold"), text="PLAYER", bg="orange", fg="blue")
player_indicator.grid(row=0,column=3)
computer_indicator.grid(row=0, column=1)

def msg_update(msg):
    final_message['text'] = msg
    
def com_update():
    final = int(computer_score['text'])
    final += 1
    computer_score["text"] = str(final)
    
def pla_update():
    final = int(player_score['text'])
    final += 1
    player_score["text"] = str(final)
    
def winner_check(computer, player):
    if player == computer:
        msg_update("It's a tie !")
    elif computer == "rock":
        if player == "paper":
            msg_update("Computer Wins !")
            com_update()
            
        else:
            msg_update("Player Wins !")
            pla_update()
    elif computer == "paper":
        if player == "scissor":
            msg_update("Computer Wins !")
            com_update()
        else:
            msg_update("Player Wins !")
            pla_update()
            
    elif computer == "scissor":
        if player == "rock":
            msg_update("Computer Wins !")
            com_update()
            
        else:
            msg_update("Player Wins !")
            pla_update()
    else:
        pass

to_select = ["rock", "scissor", "paper"]

def choice_update(msg):
    com_choice = to_select[randint(0,2)]
    if com_choice == "rock":
        label_computer.configure(image=image_rock2)
    elif com_choice == "paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)
    if msg =="rock":
        label_player.configure(image=image_rock1)
    elif msg == "paper":
        label_player.configure(image= image_paper1)
    else:
        label_player.configure(image=image_scissor1)
        
    winner_check(msg, com_choice)



final_message = Label(window, font=('Times new roman', 40, "bold"), bg="blue",fg="white")
final_message.grid(row=3, column=2)

button_rock = Button(window, width=16, height=3, text="ROCK", font=("arial", 20, "bold"),bg="red", fg="yellow",command=lambda:choice_update("rock")).grid(row=2, column=1)
button_paper = Button(window, width=16, height=3, text="PAPER", font=("arial", 20, "bold"),bg="red", fg="yellow",command=lambda:choice_update("paper")).grid(row=2, column=2)
button_scissor = Button(window, width=16, height=3, text="SCISSOR", font=("arial", 20, "bold"),bg="red", fg="yellow",command=lambda:choice_update("scissor")).grid(row=2, column=3)

# Execute
window.mainloop()