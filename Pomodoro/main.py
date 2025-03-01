import tkinter as tk
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224
REPS = 0
IS_RUNNING = False
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global IS_RUNNING
    IS_RUNNING = False

    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global IS_RUNNING
    global REPS

    if REPS % 2 == 0:
        title_label.config(text="Work", fg=GREEN)
        to_work_time = WORK_MIN
    elif REPS % 7 == 0:
        title_label.config(text="Break", fg=RED)
        to_work_time = LONG_BREAK_MIN
    else:
        title_label.config(text="Break", fg=PINK)
        to_work_time = SHORT_BREAK_MIN
    
    print(to_work_time)

    if not IS_RUNNING:
        count_down(to_work_time)
        IS_RUNNING = True


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global REPS
    global timer

    count_minutes = str(count // 60)
    count_seconds = str(count % 60)
    
    if len(count_minutes) == 1:
        count_minutes = "0" + count_minutes
    if len(count_seconds) == 1:
        count_seconds = "0" + count_seconds
    
    count_text = f"{count_minutes}:{count_seconds}"

    canvas.itemconfig(timer_text, text=count_text)
    if count > 0:
       timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        check_marks.config(text="✓"*int((REPS+2)//2))
        REPS += 1
        reset_timer()
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file = "tomato.png")
canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=tomato_img)
timer_text = canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2+20, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



title_label = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

end_button = tk.Button(text="End", highlightthickness=0, command=reset_timer)
end_button.grid(row=2, column=2)

check_marks = tk.Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
