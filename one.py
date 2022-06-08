

import pygame
import random
import keyboard
one = 44
limit_y = one * 9
FPS = 60
W = 1400  # ширина экрана
H = 800  # высота экрана
WHITE = (176, 196, 222)
BLUE = (0, 70, 225)
DA = False
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
pygame.display.set_caption(" Tennis")
people = False
machine = False
pause = False
def paused():
    global start, inings, ining_people, ining_machine, wait_hit
    start = True
    wait_hit = False
    inings = False
    ining_machine = False
    ining_people = True
one = 44
def new_ining():
    global j, x_player, y_player, x_ball, y_ball, x_machine, y_machine, ining_machine, ining_people, jj
    if j == 3:
        j = 0
    jj = 0
    if j > 0:
        ining_machine = True
        jj = 0
        x_player = 18.5 * one + 200
        y_player = 16 * one
        x_machine = one * 17 - 200
        y_machine = one * 4
        x_ball = x_machine
        y_ball = y_machine
    else:
        ining_people = True
        x_player = 11.5 * one
        y_player = 16 * one
        x_machine = one * 25 - 200
        y_machine = one * 4
        x_ball = x_player
        y_ball = y_player
argument_cor_machine = ((one * 11.5, 5 * one), (24.5 * one, 5 * one), (29.5 * one, 16 * one), (6.5 * one, 16 * one))
Color_cort = (94, 100, 122)
Color_pole = (90, 154, 196)
Yellow = (255, 255, 0)
BLACK = (30, 30, 30)
# переменные для начала
button_start = False
button_pause = False
button_EXIT = False
controller = True
sc.fill(BLACK)
height = 150
x = W // 2
y = H // 2
r = 10
hit = 0
ining_people = False
ining_machine = False
game: bool = False
clava = True
while controller:
    pygame.display.update()
    sc.fill(BLACK)
    font = pygame.font.SysFont('arial', 50)
    text = font.render("""Для выбора управления нажмите Enter / Start  """, True, Yellow)
    sc.blit(text, [300, 350])
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            EXIT()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_KP_ENTER:
                controller = False
            if i.key == pygame.K_RETURN:
                controller = False
            if i.key == pygame.K_SPACE:
                controller = False
            clava = True
    pygame.joystick.init()
    if pygame.joystick.get_count() > 1:
        font = pygame.font.SysFont('arial', 50)
        text = font.render("Подключено слишком много джостиков, оставьте один и перезапустите приложение  ", True,
                           Yellow)
        pygame.display.update()
        sc.blit(text, [300, 350])
    elif pygame.joystick.get_count() == 1:  # если подключён один джостик
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        button = joystick.get_button(7)
        if button == 1:
            controller = False
            clava = False
    clock.tick(FPS)
press_start = True
while 1:
def upr():
    global joystick_count, joystick, axis_y, axis_x, y, x, x_player, y_player, wait_hit, hit, inings, y_ball, x_ball, start, x_machine, y_machine, ining_people, ining_machine, press_start, y_min, move_ball_y, move_ball_x, game, temp_y, height, pause, bounce, DA, j, machine_point, You_point, w_key, d_key, s_key, a_key, space_key, temp_res
    for iter in pygame.event.get():
        if iter.type == pygame.QUIT:
            exit()
        elif iter.type == pygame.KEYDOWN:
            if iter.key == pygame.K_w:
                w_key = -5
            if iter.key == pygame.K_s:
                s_key = 5
            if iter.key == pygame.K_d:
                d_key = 5
            if iter.key == pygame.K_a:
                a_key = -5
            if iter.key == pygame.K_SPACE:
                space_key = True
        elif iter.type == pygame.KEYUP:
            if iter.key == pygame.K_w:
                w_key = 0
            if iter.key == pygame.K_s:
                s_key = 0
            if iter.key == pygame.K_d:
                d_key = 0
            if iter.key == pygame.K_a:
                a_key = 0
            if iter.key == pygame.K_SPACE:
                space_key = False
    joystick_count = pygame.joystick.get_count()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    axis_y = joystick.get_axis(1)
    axis_x = joystick.get_axis(0)
    if joystick.get_button(7) == 0:
        press_start = False
    if joystick.get_button(7) == 1 and not press_start:
        print("URA")
        press_start = True
        if start:
            start = False
        else:
            start = True
            x_player = 18.5 * one + 200
            y_player = 16 * one
            x_machine = one * 17 - 200
            y_machine = one * 4
            x_ball = x_player
            y_ball = y_player
            temp_y = 0
            ining_people = True
            ining_machine = False
            move_ball_y = 0
            move_ball_x = 0
            You_point = 0
            machine_point = 0
    if ining_people and DA:
        buttonss = joystick.get_button(1)
        if buttonss == 1:
            inings = True
            ining_people = False
            y_ball -= 11
            y_min = y_ball - 100
            DA = False
            j += 1
        if j % 2 == 1:
            pass
        if axis_y > 0.001:
            y_player += int(5 * axis_y)
        if axis_y < -0.001 and axis_y != 0 and y_player > one * 16:
            y_player -= int(5 * abs(axis_y))
        if axis_x > 0.001:
            x_player += int(5 * axis_x)
        if axis_x < -0.001 and axis_x != 0:
            x_player -= int(5 * abs(axis_x))
        return
    if wait_hit:
        buttonss = joystick.get_button(1)
        height -= 5
        print(height)
        if height < 0:
            paused()
        temp_y = 50 + temp_y // 5
        y_ball += temp_y // 10
        print(y_ball, ' asd', y_player)
        if buttonss ==0:
            if axis_y > 0.001:
                y_player += int(5 * axis_y)
            if axis_y < -0.001 and axis_y != 0:
                y_player -= int(5 * abs(axis_y))
        if abs(y_player - y_ball) <= 10 and buttonss == 1:
            #c = random.randint(-1, 1)
            #print(c)
            if axis_y > 0.001:
                move_ball_y = int(5 * axis_y)
            if axis_y < -0.001 and axis_y != 0:
                move_ball_y = -int(5 * abs(axis_y))
            if axis_x > 0.001:
                move_ball_x = int(5 * axis_x)
            if axis_x < -0.001 and axis_x != 0:
                move_ball_x = -int(5 * abs(axis_x))
            wait_hit = False
            game = True
            bounce = False
            hit = move_ball_y / 2
    else:
        if axis_y > 0.001:
            y_player += int(5 * axis_y)
        if axis_y < -0.001 and axis_y != 0 and y_player > one * 9:
            y_player -= int(5 * abs(axis_y))
        if axis_x > 0.001:
            x_player += int(5 * axis_x)
        if axis_x < -0.001 and axis_x != 0:
            x_player -= int(5 * abs(axis_x))
        if joystick.get_button(1) == 1:
            if abs(y_player - y_ball) < 20 and abs(x_player - x_ball) < 20:
                bounce = True
                move_ball_x = a_key + d_key
                move_ball_y = -5
                height = 200
                temp_res = y_ball
    break
def pole():
    pygame.draw.line(sc, (255, 255, 255), (one * 11.5, 4.915 * one), (6.5 * one, 16.12 * one), 10)
    pygame.draw.line(sc, (255, 255, 255), (one * 24.5, 4.915 * one), (29.5 * one, 16.12 * one), 10)
    pygame.draw.line(sc, (255, 255, 255), (one * 6.5 + 5 - 5, 16 * one), (29.5 * one - 5, 16 * one), 10)
    pygame.draw.line(sc, (255, 255, 255), (one * 11.55, 5 * one), (24.5 * one, 5 * one), 10)
    pygame.draw.line(sc, (255, 255, 255), (one * 13.2, 5 * one), (9.2 * one, 16 * one), 10)
    pygame.draw.line(sc, (255, 255, 255), (one * 22.5, 5 * one), (26.5 * one, 16 * one), 10)
    pygame.draw.line(sc, (255, 255, 255), (one * 12.65, 6.5 * one), (23 * one, 6.5 * one), 10)
    pygame.draw.line(sc, (255, 255, 255), (one * 10.8, 11.8 * one), (25 * one, 11.8 * one), 10)
    pygame.draw.line(sc, (255, 255, 255), (one * 18, 6.5 * one), (17.5 * one, 11.8 * one), 10)
    pygame.draw.line(sc, (255, 255, 255), (one * 18, 6.5 * one), (17.5 * one, 11.8 * one), 10)
    pygame.draw.line(sc, (1, 1, 1), (one * 8.42, 9 * one), (27.92 * one, 9 * one), 5)
    pygame.draw.line(sc, (255, 255, 255), (one * 8.42, 7 * one), (27.92 * one, 7 * one), 5)
    pygame.draw.line(sc, (1, 1, 1), (one * 8.5, 7 * one), (8.5 * one, 9 * one), 10)
    pygame.draw.line(sc, (1, 155, 255), (one * 10.5, 7 * one), (10.5 * one, 9 * one), 10)
    pygame.draw.line(sc, (1, 155, 255), (one * 25.8, 7 * one), (25.8 * one, 9 * one), 10)
    pygame.draw.line(sc, (1, 1, 1), (one * 27.8, 7 * one), (27.8 * one, 9 * one), 10)
    pygame.draw.circle(sc, Yellow, (int(x_ball), int(y_ball)), r)
    pygame.draw.ellipse(sc, PINK, (x_player, y_player, one * 0.425, 0.85 * one), 5)
    pygame.draw.ellipse(sc, PINK, (x_machine, y_machine, one * 0.425, 0.85 * one), 5)
temp_ball = 0
PINK = (190, 50, 100)
level_ball = 150
x_min = 0
y_min = 0
move_ball_x = 0
move_ball_y = 0
wait_hit = False
x_player = 18.5 * one + 200
y_player = 16 * one
x_machine = one * 17 - 200
y_machine = one * 4
x_ball = x_player
y_ball = y_player
You_point = 0
machine_point = 0
ining_people = True
start = True
temp_res = 0
inings = False
j = 1
space_key = 0
a_key = 0
w_key = 0
s_key = 0
d_key = 0
new_ining()
jj = 0
ining_wait = False
while 1:
    sc.fill(WHITE)
    if start:
        if space_key:
            if abs(y_machine - y_ball) < 20 and abs(x_machine - x_ball) < 20:
                bounce = True
                move_ball_x = a_key + d_key
                move_ball_y = 5
                height = 200
                temp_res = y_ball
                game = True
        raz = w_key + s_key
        if raz + y_machine <= 7 * one:
            y_machine += w_key + s_key
        x_machine += a_key + d_key
        text = font.render("    Счёт", True, Yellow)
        sc.blit(text, [100, 250])
        text = font.render("Компьютер "+ str(machine_point), True, Yellow)
        sc.blit(text, [100, 350])
        text = font.render("Вы "+ str(You_point), True, Yellow)
        sc.blit(text, [100, 450])
        if ining_people:
            x_ball = x_player
            y_ball = y_player
            text = font.render("Ваша подача", True, Yellow)
            sc.blit(text, [600, 150])
            ining_machine = False
            DA = True
            people = True
        if ining_machine:
            jj += 1
            if jj == 100 and not game:
                x_ball = x_machine
                y_ball = y_machine - 100
                ining_machine = False
                inings = True
                ining_wait = True
        if inings:
            if ining_wait:
                if space_key:
                    if abs(y_machine - y_ball) < 31 and abs(x_machine - x_ball) < 31:
                        bounce = True
                        move_ball_x = a_key + d_key
                        move_ball_y = 5
                        height = 200
                        temp_res = y_ball
            if y_min < y_ball:
                y_ball -= 10
                if space_key:
                    if abs(y_machine - y_ball) < 20 and abs(x_machine - x_ball) < 20:
                        bounce = True
                        move_ball_x = a_key + d_key
                        move_ball_y = 5
                        height = 200
                        temp_res = y_ball
                        game = True
            else:
                wait_hit = True
                inings = False
                temp_y = 1
                height = 250
                if space_key:
                    if abs(y_machine - y_ball) < 20 and abs(x_machine - x_ball) < 20:
                        bounce = True
                        move_ball_x = a_key + d_key
                        move_ball_y = 5
                        height = 200
                        temp_res = y_ball
                        game = True
        if game:
            y_ball += move_ball_y
            x_ball += move_ball_x
            height -= 2
            if space_key:
                if abs(y_machine - y_ball) < 20 and abs(x_machine - x_ball) < 20:
                    bounce = True
                    move_ball_x = a_key + d_key
                    move_ball_y = 5
                    height = 200
                    temp_res = y_ball
            if height <0 and not bounce:
                bounce = True
                move_ball_x = move_ball_x // 2 + (move_ball_x // 4 * -1)
                move_ball_y = move_ball_y // 2
                height = 100
                temp_res = y_ball
            if height < 0 and bounce:
                game = False
                bounce = False
            if not game:
                if people:
                    people = False
                    if 16 * one > temp_res > 9 * one:
                        machine_point += 1
                    elif 9 * one > temp_res > 5 * one:
                        You_point += 1
                    else:
                        if temp_res > 16 * one:
                            You_point += 1
                        else:
                            machine_point += 1
                j += 1
                new_ining()
    else:
        text = font.render("Игра окончена, нажмите Start, чтобы начать заново", True, Yellow)
        sc.blit(text, [300, 150])
    pole()
    pygame.display.update()
    clock.tick(FPS)

