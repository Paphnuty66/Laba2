from tkinter import *
import time
class Timer:
    def _init_(self):
        self._starttimer = None
    def start(self):
        if self._starttimer is not None:
            lbl.config(text="Таймер уже запущен, чтобы начать останови таймер")
        self._starttimer = time.perf_counter()
    def stop(self):
        if self._starttimer is not None:
            lbl.config(text="Таймер не запущен, нажми на Start чтобы он заработал")
        t_time = time.perf_counter()-self._starttimer
        return lbl.config(t_time)




def click():
    p = Timer()
    p.start
    lbl.config(text="Нажата")
    p.stop()





window = Tk()
window['bg'] = '#8B7355'
window.title("Секундомер|Таймер")
window.geometry("400x400")

lbl = Label(window, text="Для начала нажми на кнопку Start", font=("Elephant", 16))
lbl.pack()
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label="Таймер")
menu.add_cascade(label="Сменить режим", menu=new_item)
window.config(menu=menu)
btn = Button(window, text="Start!", font="Elephant", background="#DC143C", command=click)
btn.place(relx=.5, rely=.5, anchor="c")
window.mainloop()