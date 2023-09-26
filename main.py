from tkinter import *
import pandas
import random
li = {}
current_dic = {}
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/Russian English - Sheet1.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("data/Russian English - Sheet1.csv")
    li = og_data.to_dict(orient="records")
else:
    li = data.to_dict(orient="records")
def new_card():
    global current_dic
    global timer
    root.after_cancel(timer)
    canvas.itemconfig(front_img, image=card_front_img)
    current_dic = random.choice(li)
    canvas.itemconfig(title,text= "Russian", fill="black")
    canvas.itemconfig(word,text= current_dic["Russian"], fill="black")
    timer = root.after(4000, func=reverse)


def reverse():
    canvas.itemconfig(front_img, image=card_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_dic["English"], fill="white")


def save():
    li.remove(current_dic)
    datas = pandas.DataFrame(li)
    datas.to_csv("data/words_to_learn.csv")
    new_card()


root = Tk()
root.title("Flashcard")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
timer = root.after(4000,func=reverse)
canvas = Canvas(width=800, height=526)
front_img = canvas.create_image(400, 263, image= card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0,columnspan=2)
correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, border=0, command=save)
correct_button.grid(row=1,column=1)
incorrect_img = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect_img, highlightthickness=0, border=0, command=new_card)
incorrect_button.grid(row=1,column=0)
new_card()
root.mainloop()
