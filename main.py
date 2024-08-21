from tkinter import *
import pygame


b_count = 0
timer = None
FONT_NAME = 'Courier'
RED = '#FF6D60'
YELLOW = '#F7D060'
CREAM = '#F3E99F'
GREEN = '#98D8AA'
pygame.mixer.init()


def play():
    pygame.mixer.music.load('alarm.wav')
    pygame.mixer.music.play(loops=0)


def start_countdown():
    count_down()


def reset_count():
    global b_count, timer

    screen.after_cancel(timer)
    b_count = 0
    lb_timer.config(text='Timer')
    lb_check.config(text='')
    canvas.itemconfig(text_canvas, text='00:00')


def count_down(minutes=20, sec=0):
    global b_count, timer

    canvas.itemconfig(text_canvas, text=f'{minutes:02d}:{sec:02d}')
    lb_timer.config(text='Work', fg=GREEN)

    if sec == 0:
        sec = 60
        minutes -= 1

    if minutes >= 0:
        timer = screen.after(1000, count_down, minutes, sec - 1)
    else:
        b_count += 1
        lb_check.config(text='✔' * b_count)

        if b_count > 3:
            reset_count()
            # play()
            break_time(minutes=20, sec=0)
        else:
            # play()
            break_time()


def break_time(minutes=5, sec=0):
    global b_count, timer

    canvas.itemconfig(text_canvas, text=f'{minutes:02d}:{sec:02d}')
    lb_timer.config(text='Break', fg=YELLOW)

    if sec == 0:
        sec = 59
        minutes -= 1

    if minutes >= 0:
        timer = screen.after(1000, break_time, minutes, sec - 1)
    else:
        # play()
        count_down()


# Screen
screen = Tk()
screen.config(padx=100, pady=50, bg=CREAM)
screen.title('Pomodoro Countdown')

# BG image for canvas
bg_image = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=CREAM, highlightthickness=0)
canvas.create_image(100, 112, image=bg_image)
text_canvas = canvas.create_text(102, 135, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Timer Label
lb_timer = Label(text='Timer', fg=GREEN, bg=CREAM, font=(FONT_NAME, 35, 'bold'))
lb_timer.grid(column=1, row=0)

# Start button
btn_start = Button(text='Start', bg=YELLOW, width=7, command=start_countdown)
btn_start.grid(column=0, row=2)

# Reset button
btn_restart = Button(text='Restart', bg=YELLOW, width=7, command=reset_count)
btn_restart.grid(column=2, row=2)

# Check mark label
lb_check = Label(text='', bg=CREAM, fg=GREEN)
lb_check.grid(column=1, row=3)

screen.mainloop()
