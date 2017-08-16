from tkinter import *

#Размер кно
WIDTH = 500
HEIGHT = 500

#Радиус мячей
BALL_MY_RADIUS = 30
BALL_KILL_RADIUS = 10

#Скорость мячей
BALL_SPEED = 5
BALL_MY_X_SPEED = 0
BALL_MY_Y_SPEED = 0
BALL_KILL_X_SPEED = 0
BALL_KILL_Y_SPEED = 0

def spawn_ball():
    global BALL_X_SPEED
    # Выставляем мяч по центру
    c.coords(BALL_MY, WIDTH/4-BALL_MY_RADIUS/2,
             HEIGHT/4-BALL_MY_RADIUS/4,
             WIDTH/4+BALL_MY_RADIUS/4,
             HEIGHT/4+BALL_MY_RADIUS/4)


#Установка окна
root = Tk()
root.title("Death Ball")

#Установка экшн-окна
c = Canvas(root, width = WIDTH, height =HEIGHT)
c.pack()

#Линия по центру
LINE = c.create_line(HEIGHT, HEIGHT/2, 0, HEIGHT/2, fill="green")

#Мой мяч
BALL_MY= c.create_oval(WIDTH/2-BALL_MY_RADIUS/2,
                     HEIGHT/1.5-BALL_MY_RADIUS/2,
                     WIDTH/2+BALL_MY_RADIUS/2,
                     HEIGHT/1.5+BALL_MY_RADIUS/2, fill="blue")

def main():
    move_my_ball()
    root.after(100,main)

def move_my_ball():
    c.move(BALL_MY, BALL_MY_X_SPEED, BALL_MY_Y_SPEED)

    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL_MY)
    #ball_center = (ball_top + ball_bot) / 2

    if ball_right + BALL_MY_X_SPEED < WIDTH and ball_left + BALL_MY_X_SPEED > 0:
        c.move(BALL_MY, BALL_MY_X_SPEED, BALL_MY_Y_SPEED)
    else:
        if ball_right > WIDTH / 2:
            c.move(BALL_MY, WIDTH - ball_right, BALL_MY_Y_SPEED)
        else:
            c.move(BALL_MY, -ball_left , BALL_MY_Y_SPEED)

    if ball_bot + BALL_MY_Y_SPEED < HEIGHT and ball_top + BALL_MY_Y_SPEED > LINE:
        c.move(BALL_MY, BALL_MY_X_SPEED, BALL_MY_Y_SPEED)
    else:
        if ball_bot > HEIGHT/2:
            c.move(BALL_MY, BALL_MY_X_SPEED, HEIGHT - ball_bot)
        else:
            c.move(BALL_MY, BALL_MY_X_SPEED, LINE -ball_top)


c.focus_set()

#Реакция на нажатие клавиши
def move(event):
    global BALL_MY_X_SPEED, BALL_MY_Y_SPEED
    if event.keysym == "Up":
        BALL_MY_Y_SPEED = -BALL_SPEED
    elif event.keysym == "Down":
        BALL_MY_Y_SPEED = BALL_SPEED
    elif event.keysym == "Left":
        BALL_MY_X_SPEED = -BALL_SPEED
    elif event.keysym == "Right":
        BALL_MY_X_SPEED = BALL_SPEED
c.bind("<KeyPress>", move)



# Реакция на отпускание клавиши
def stop_ball(event):
    global BALL_MY_X_SPEED, BALL_MY_Y_SPEED
    if event.keysym in ("Up", "Down"):
        BALL_MY_Y_SPEED = 0
    elif event.keysym in ("Left", "Right"):
        BALL_MY_X_SPEED = 0
c.bind("<KeyRelease>", stop_ball)



main()
root.mainloop()