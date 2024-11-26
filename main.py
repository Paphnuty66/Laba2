from tkinter import *
from datetime import datetime
from tkinter.messagebox import showinfo
temp = 0
after_id = " "
hours=0
minut=0
current_mode = "sec"
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

def starttm():
    global after_id, hours, minut
    lbl.config(text="Время пошло!")
    btn3.place_forget()
    btn4.place_forget()
    btn5.place_forget()
    btn6.place_forget()
    btn7.place_forget()
    if hours == 0 and minut == 0:
        lbl.config(text="Таймер завершен!")
        lbl1.config(text="00:00")
        btn8.place_forget()
        timer()
        return

    if minut == 0:
        if hours > 0:
            hours -= 1
            minut = 59
    else:
        minut -= 1

    if hours < 10 and minut < 10:
        h1 = f"0{hours}:0{minut}"
    elif hours < 10 and minut >= 10:
        h1 = f"0{hours}:{minut}"
    elif hours >= 10 and minut < 10:
        h1 = f"{hours}:0{minut}"
    else:
        h1 = f"{hours}:{minut}"
    lbl1.config(text=h1)
    after_id = window.after(1000, starttm)
    lbl.config(text="Чтобы остановить нажмите Stop")
    btn8.place(relx=.5, rely=.5, anchor="c")

def stoptm():
    lbl.config(text="Хотите сбросить таймер?")
    btn8.place_forget()
    btn9.place(relx=.5, rely=.5, anchor="c")
    window.after_cancel(after_id)

def resettm():
    lbl.config(text="Для начала нажми на кнопку Start")
    global hours, minut
    hours = 0
    minut = 0
    btn9.place_forget()
    timer()

def timer():
    btn.place_forget()
    btn1.place_forget()
    btn2.place_forget()
    lbl.config(text="Введите время для таймера")
    lbl1.config(text="00:00")
    btn3.place(relx=.3, rely=.35, anchor="c")
    btn4.place(relx=.4, rely=.35, anchor="c")
    btn5.place(relx=.6, rely=.35, anchor="c")
    btn6.place(relx=.7, rely=.35, anchor="c")
    btn7.place(relx=.5, rely=.5, anchor="c")

def plush():
    global hours, minut
    if hours<59:
        hours += 1
    else:
        showinfo("Предупреждение!", "Мой таймер не рассчитан на такие цифры!")

    if hours < 10 and minut < 10:
        h1 = "0" + str(hours)+":0"+str(minut)
        lbl1.config(text=h1)
    elif hours < 10 and minut >= 10:
        h1 = "0" + str(hours)+":"+str(minut)
        lbl1.config(text=h1)
    elif hours >= 10 and minut < 10:
        h1 = str(hours) + ":0" + str(minut)
        lbl1.config(text=h1)
    else:
        h1 = str(hours) + ":" + str(minut)
        lbl1.config(text=h1)

def minush():
    global hours, minut
    if hours > 0:
        hours -= 1
        if hours < 10 and minut < 10:
            h1 = "0" + str(hours) + ":0" + str(minut)
            lbl1.config(text=h1)
        elif hours < 10 and minut >= 10:
            h1 = "0" + str(hours) + ":" + str(minut)
            lbl1.config(text=h1)
        elif hours >= 10 and minut < 10:
            h1 = str(hours) + ":0" + str(minut)
            lbl1.config(text=h1)
        else:
            h1 = str(hours) + ":" + str(minut)
            lbl1.config(text=h1)

def plusm():
    global hours, minut
    if minut<59:
        minut += 1
    else:
        showinfo("Предупреждение!", "Мой таймер не рассчитан на такие цифры!")


    if hours < 10 and minut < 10:
        h1 = "0" + str(hours)+":0"+str(minut)
        lbl1.config(text=h1)
    elif hours < 10 and minut >= 10:
        h1 = "0" + str(hours)+":"+str(minut)
        lbl1.config(text=h1)
    elif hours >= 10 and minut < 10:
        h1 = str(hours) + ":0" + str(minut)
        lbl1.config(text=h1)
    else:
        h1 = str(hours) + ":" + str(minut)
        lbl1.config(text=h1)

def minusm():
    global hours, minut
    if minut > 0:
        minut -= 1
        if hours < 10 and minut < 10:
            h1 = "0" + str(hours) + ":0" + str(minut)
            lbl1.config(text=h1)
        elif hours < 10 and minut >= 10:
            h1 = "0" + str(hours) + ":" + str(minut)
            lbl1.config(text=h1)
        elif hours >= 10 and minut < 10:
            h1 = str(hours) + ":0" + str(minut)
            lbl1.config(text=h1)
        else:
            h1 = str(hours) + ":" + str(minut)
            lbl1.config(text=h1)

def Sec():
    global current_mode, hours, minut
    hours=0
    minut=0
    if current_mode != "sec":
        current_mode = "sec"
        btn3.place_forget()
        btn4.place_forget()
        btn5.place_forget()
        btn6.place_forget()
        btn7.place_forget()
        btn8.place_forget()
        btn9.place_forget()
        lbl.config(text="Для начала нажми на кнопку Start")
        lbl1.config(text="00:00")
        btn.place(relx=.5, rely=.5, anchor="c")

def Timer():

    global current_mode, temp
    temp = 0
    if current_mode != "timer":
        current_mode = "timer"
        btn.place_forget()
        btn1.place_forget()
        btn2.place_forget()
        lbl.config(text="Введите время для таймера")
        lbl1.config(text="00:00")
        btn3.place(relx=.3, rely=.35, anchor="c")
        btn4.place(relx=.4, rely=.35, anchor="c")
        btn5.place(relx=.6, rely=.35, anchor="c")
        btn6.place(relx=.7, rely=.35, anchor="c")
        btn7.place(relx=.5, rely=.5, anchor="c")



window = Tk()
window['bg'] = '#F0FFFF'
window.title("Секундомер")
window.geometry("400x400")
showinfo(title="Белов Павел ИДБ-23-14", message="Вариант 13 Программа <<Таймер-секундомер>>")
lbl = Label(window, text="Для начала нажми на кнопку Start", font=("Elephant", 16))
lbl.pack()
lbl1 = Label(window, text="00:00", font=("Elephant", 40))
lbl1.pack()
btn = Button(window, text="Start!", font=("Elephant", 20), background="#66CDAA", command=start, activebackground="White")
btn.place(relx=.5, rely=.5, anchor="c")

btn1 = Button(window, text="Stop!", font=("Elephant", 20), background="#66CDAA", command=stop, activebackground="White")
btn2 = Button(window, text="Reset?", font=("Elephant", 20), background="#66CDAA", command=reset, activebackground="White")

btn3 = Button(window, text="+", font=("Elephant", 15), background="#66CDAA", command=plush, activebackground="White")
btn4 = Button(window, text="-", font=("Elephant", 15), background="#66CDAA", command=minush, activebackground="White")
btn5 = Button(window, text="+", font=("Elephant", 15), background="#66CDAA", command=plusm, activebackground="White")
btn6 = Button(window, text="-", font=("Elephant", 15), background="#66CDAA", command=minusm, activebackground="White")
btn7 = Button(window, text="Start!", font=("Elephant", 15), background="#66CDAA", command=starttm, activebackground="White")
btn8 = Button(window, text="Stop!", font=("Elephant", 15), background="#66CDAA", command=stoptm, activebackground="White")
btn9 = Button(window, text="Reset!", font=("Elephant", 15), background="#66CDAA", command=resettm, activebackground="White")
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label="Таймер", command=timer)
new_item.add_command(label="Секундомер", command=Sec)
menu.add_cascade(label="Сменить режим", menu=new_item)
window.config(menu=menu)
window.mainloop()