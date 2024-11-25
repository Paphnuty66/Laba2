from tkinter import *
from datetime import datetime

temp = 0
after_id = " "

def tick():
    global temp, after_id
    after_id = window.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    lbl1.configure(text=str(f_temp))
    temp += 1

def start():
    lbl.config(text="Время пошло")
    btn.place_forget()
    btn1.place(relx=.5, rely=.5, anchor="c")
    tick()

def stop():
    lbl.config(text="Хотите сбросить Секундомер?")
    btn1.place_forget()
    btn2.place(relx=.5, rely=.5, anchor="c")
    window.after_cancel(after_id)

def reset():
    lbl.config(text="Для начала нажми на кнопку Start")
    global temp
    temp = 0
    btn2.place_forget()
    btn.place(relx=.5, rely=.5, anchor="c")
    lbl1.config(text="00:00")

def timer():
    btn.place_forget()
    btn1.place_forget()
    btn2.place_forget()
    lbl.config(text="Введите время для таймера")
    lbl1.config(text="00:00")


window = Tk()
window['bg'] = '#8B7355'
window.title("Секундомер")
window.geometry("400x400")
lbl = Label(window, text="Для начала нажми на кнопку Start", font=("Elephant", 16))
lbl.pack()
lbl1 = Label(window, text="00:00", font=("Elephant", 40))
lbl1.pack()
btn = Button(window, text="Start!", font=("Elephant", 20), background="#DC143C", command=start, activebackground="White")
btn.place(relx=.5, rely=.5, anchor="c")
btn1 = Button(window, text="Stop!", font=("Elephant", 20), background="#DC143C", command=stop, activebackground="White")
btn2 = Button(window, text="Reset?", font=("Elephant", 20), background="#DC143C", command=reset, activebackground="White")
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label="Таймер",command=timer)
menu.add_cascade(label="Сменить режим", menu=new_item)
window.config(menu=menu)
window.mainloop()