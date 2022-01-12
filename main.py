import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BREAK = 5
rep = 0
actual_time_passing = None


# ---------------------------- TIMER RESET ------------------------------- #
def resetting():
    global rep
    rep = 0
    window.after_cancel(actual_time_passing)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.configure(text='Timer')
    check_label.config("")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    rep += 1
    work = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    if (rep % 2) != 0:
        count_down(work)
        timer_label.configure(text='Work')
    elif rep % 8 == 0:
        count_down(long_break)
        timer_label.configure(text='Break')
    else:
        count_down(short_break)
        timer_label.configure(text='Break')
    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}")
    if count > 0:
        global actual_time_passing
        actual_time_passing = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()
        mark = ''
        work_sessions = math.floor(rep / 2)
        for _ in range(work_sessions):
            mark += "✔"
            check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Time Manager")
window.config(padx=120, pady=60, bg=GREEN)

canvas = Canvas(width=210, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=GREEN, fg=RED)
timer_label.grid(column=1, row=0)

check_label = Label(font=(FONT_NAME, 50, "bold"), bg=GREEN, fg=RED)
check_label.grid(column=1, row=3)

start_button = Button(width=7, height=3, text="Start", bd=0, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(width=7, height=3, text="Reset", bd=0, highlightthickness=0, command=resetting)
reset_button.grid(column=2, row=2)

window.mainloop()
