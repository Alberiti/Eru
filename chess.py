from tkinter import *
from tkinter import messagebox as mb
from math import *
from tkinter import filedialog as fd
started = False
primenit = True
chelovek = 0


startinger = False
pausing = False
# кнопки паузы и начала не нажаты

colorpawn = "white"
colorblack = "black"
colorwhite = "white"
peshkacolor = True

# Изаначально установили, что цвет пешки белый, цвет чёрный чёрный, цвет белых белый, а пешка у белых

xpeshka = 160
ypeshka = 480

xwhite = 320
ywhite = 320

xblack = 80
yblack = 240

# задаём координаты пешки и королей

pauer = 51  # номер клетки в которой пешка
blkinguer = 26  # номер клетки в которой чёрный король
wtkinguer = 37  # номер клетки в которой белый король

#size = (512, 512)
#img = Image.open('mem.jpeg')
#img.thumbnail(size)
#img.save("mem1.png")
# from tkinter import Tk, Menu
alf = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}
computer = False
people = False
a = True
movecolorwhite = True
aop = False
p = False
kw = False
kb = False
p1 = True
kw1 = True
kb1 = True
vibp = False
vibkw = False
vibkb = False
vibor = False
f = open('text.txt', 'w')

memas = False

trebunal = False
kto = True

# клетки которые блокирует пешка, что бы не производить лишний рассчётов каждый раз
noleft = pauer - 9
noright = pauer - 7
color_white_board = "#E9FB00"
color_black_board = "#A64B00"

oq = 0  # инициализация переменной

pawsqare = 1
kingwhsquare = 2
kingblsquare = 3

colorkingwhite = "white"
colorkingblack = "black"

x: int = 390  # Координаты для отрисовки пешки
y: int = 55  # Координаты для отрисовки пешки
root = Tk()  # Говорим , что будем создавать главное окно
root.title('Проведи пешку')  # название
root.geometry('1000x680')  # размер окна
root.resizable(False, False)  # запрет увелечения окна
root["bg"] = "white"  # Цвет фона
# abc = PhotoImage(file="mem.png")
canvas = Canvas(root, width=1160, height=760, bg="white")
canvas.pack()
# variant1 = PhotoImage(file="whitepawn.png")
# variant2 = PhotoImage(file="blackpawn.png")
# variant3 = PhotoImage(file="whitecentr.png")
label_x = 100
label_y1 = 30
label_y2 = 600
label_compukter = Label(root, text="Компьютер", bg="white", font="Arial 28")
label_compukter.place(x=label_x, y=label_y1)

label_people = Label(root, text="Человек", bg="white", font="Arial 28")
label_people.place(x=label_x, y=label_y2)
# canvas.btn = Button(text="Меню", background="#F00").place(x=0, y=100, width=70)  # создание кнопки меню

def vihod():
    root.destroy()

def nachali():
    global startinger, butn1

    if not startinger:
        startinger = True
        butn1['text'] = 'Стоп'
    else:
        startinger = False
        butn1['text'] = 'Старт'


def paused():
    global pausing, butn2
    if not pausing:
        pausing = True
        butn2['text'] = 'Продолжить'
    else:
        pausing = False
        butn2['text'] = 'Пауза'






def chessboard(col_white_pole, col_black_pole):  # отрисовка шахматной доски
    # col2 = "#A64B00"
    # col1 = "#E9FB00"  # светлый
    yboard = 40
    ii = 1
    while ii <= 4:
        i1 = 1
        op = "white"
        xboard = 360
        while i1 <= 8:
            if (i1 % 2) == 0:
                op = col_black_pole
            else:
                op = col_white_pole
            canvas.create_rectangle(xboard, yboard, xboard + 80, yboard + 80, fill=op, outline="black")
            xboard += 80
            i1 = i1 + 1
        xboard = 360
        yboard += 80
        i2 = 1
        while i2 <= 8:
            canvas.create_rectangle(xboard, yboard, xboard + 80, yboard + 80, fill=op, outline="black")
            xboard += 80
            i2 = i2 + 1
            if (i2 % 2) == 1:
                op = col_black_pole
            else:
                op = col_white_pole
        yboard += 80
        ii += 1
    ii = 1
    xx = 390
    while ii <= 8:
        Label(root, text=alf.get(ii)).place(x=xx, y=10)
        xx += + 80
        ii += 1
    yy = 630
    while ii > 1:
        ii -= 1
        Label(root, text=str(9 - ii)).place(x=330, y=yy)
        yy -= 80


chessboard(color_white_board, color_black_board)#(360, 40, )

# пешка
def otrisovkapeshki(colorpawn, xx, yy):
    global xpawn, ypawn, head, ringup, tors, ringdn
    xpawn = x + xx
    ypawn = y + 5 + yy
    head = canvas.create_oval(xpawn - 5, ypawn - 15, xpawn + 20, ypawn + 10, fill=colorpawn, width=0)
    ringup = canvas.create_oval(xpawn - 10, ypawn + 5, xpawn + 25, ypawn + 15, fill=colorpawn, width=0)
    tors = canvas.create_arc(xpawn - 5, ypawn, xpawn + 21, ypawn + 94, outline=colorpawn, start=0, extent=180,
                             fill=colorpawn, width=0)
    ringdn = canvas.create_oval(xpawn - 20, ypawn + 44, xpawn + 36, ypawn + 54, fill=colorpawn, width=0)

def pedestroyy():
    global xpawn, ypawn, head, ringup, tors, ringdn
    canvas.delete(head)
    canvas.delete(tors)
    canvas.delete(ringup)
    canvas.delete(ringdn)



otrisovkapeshki(colorpawn, xpeshka, ypeshka)

# король белый

# col = "red"
def deletewh():
    global head1, head2, detail1white, detail2white, detail3white, detail4white
    canvas.delete(head1)
    canvas.delete(head2)
    canvas.delete(detail1white)
    canvas.delete(detail2white)
    canvas.delete(detail3white)
    canvas.delete(detail4white)

def otrisovkawhite(colorkingwhite, xx, yy):
    global head1, head2, detail1white, detail2white, detail3white, detail4white
    xking = x + xx
    yking = y + 5 + yy
    head1 = canvas.create_rectangle(xking + 5, yking - 15, xking + 15, yking + 5, outline=colorkingwhite,
                                    fill=colorkingwhite)
    head2 = canvas.create_rectangle(xking - 10, yking - 8, xking + 30, yking, outline=colorkingwhite, fill=colorkingwhite)
    arguments1 = [xking + 5, yking + 5, xking - 5, yking + 15, xking + 25, yking + 15, xking + 15, yking + 5]
    detail1white = canvas.create_polygon(arguments1, outline=colorkingwhite,
                                         fill=colorkingwhite, width=2)
    detail2white = canvas.create_oval(xking - 15, yking + 10, xking + 35, yking + 25, outline=colorkingwhite,
                                      fill=colorkingwhite, width=1)
    arguments2 = [xking + 5, yking + 20, xking - 15, yking + 45, xking + 35, yking + 45, xking + 20, yking + 25]
    detail3white = canvas.create_polygon(arguments2, outline=colorkingwhite,
                                         fill=colorkingwhite, width=2)
    detail4white = canvas.create_oval(xking - 25, yking + 40, xking + 45, yking + 55, outline=colorkingwhite,
                                      fill=colorkingwhite, width=1)


otrisovkawhite("white", xwhite, ywhite)

# чёрный король
def otrisovkablack(colorkingblack, xx, yy):
    global head1black,head2black, detail1black, detail2black, detail3black, detail4black

    xkingblack = x + xx
    ykingblack = y + 5 + yy
    head1black = canvas.create_rectangle(xkingblack + 5, ykingblack - 15, xkingblack + 15, ykingblack + 5,
                                         outline=colorkingblack,
                                         fill=colorkingblack)
    head2black = canvas.create_rectangle(xkingblack - 10, ykingblack - 8, xkingblack + 30, ykingblack,
                                         outline=colorkingblack,
                                         fill=colorkingblack)
    arguments1 = [xkingblack + 5, ykingblack + 5, xkingblack - 5, ykingblack + 15, xkingblack + 25, ykingblack + 15,
                  xkingblack + 15, ykingblack + 5]
    detail1black = canvas.create_polygon(arguments1, outline=colorkingblack,
                                         fill=colorkingblack, width=2)
    detail2black = canvas.create_oval(xkingblack - 15, ykingblack + 10, xkingblack + 35, ykingblack + 25,
                                      outline=colorkingblack,
                                      fill=colorkingblack, width=1)
    arguments2 = [xkingblack + 5, ykingblack + 20, xkingblack - 15, ykingblack + 45, xkingblack + 35, ykingblack + 45,
                  xkingblack + 20, ykingblack + 25]
    detail3black = canvas.create_polygon(arguments2, outline=colorkingblack, fill=colorkingblack, width=2)
    detail4black = canvas.create_oval(xkingblack - 25, ykingblack + 40, xkingblack + 45, ykingblack + 55,
                                      outline=colorkingblack,
                                      fill=colorkingblack, width=1)


def deletebl():
    global head1, head2, detail1white, detail2white, detail3white, detail4white
    canvas.delete(head1black)
    canvas.delete(head2black)
    canvas.delete(detail1black)
    canvas.delete(detail2black)
    canvas.delete(detail3black)
    canvas.delete(detail4black)


otrisovkablack("black", xblack, yblack)

def kingblacker(aa, b):
    canvas.move(head1black, aa, b)
    canvas.move(head2black, aa, b)
    canvas.move(detail1black, aa, b)
    canvas.move(detail2black, aa, b)
    canvas.move(detail3black, aa, b)
    canvas.move(detail4black, aa, b)
    canvas.itemconfig(head1black, fill="black")


def pawner(raza):
    canvas.move(head, 0, raza)
    canvas.move(ringup, 0, raza)
    canvas.move(tors, 0, raza)
    canvas.move(ringdn, 0, raza)
    canvas.itemconfig(head, fill="white")


def kingwhiter(aa, b):
    global wtkinguer
    canvas.move(head1, aa, b)
    canvas.move(head2, aa, b)
    canvas.move(detail1white, aa, b)
    canvas.move(detail2white, aa, b)
    canvas.move(detail3white, aa, b)
    canvas.move(detail4white, aa, b)
    canvas.itemconfig(head1, fill="white")
    wtkinguer = wtkinguer + aa / 80 + b / 10


def resetfig():
    global head1, head, head1black
    canvas.itemconfig(head1, fill="white")
    canvas.itemconfig(head, fill=colorwhite)
    canvas.itemconfig(head1black, fill=colorblack)

def srvnn(blawhi, hi): #второе падающееся это то куда мы хотим сходить
    global trebunal, xod
    if blawhi - 9 == hi:
        trebunal = False
    if blawhi - 8 == hi:
        trebunal = False
    if blawhi - 1 == hi:
        trebunal = False
    if blawhi - 7 == hi:
        trebunal = False
    if blawhi + 9 == hi:
        trebunal = False
    if blawhi + 8 == hi:
        trebunal = False
    if blawhi + 7 == hi:
        trebunal = False
    if blawhi + 1 == hi:
        trebunal = False
    if not xod:
        if pauer == hi:
            trebunal = False
        if pauer -7 == hi:
            trebunal = False
        if pauer - 9 == hi:
            trebunal = False
    if not trebunal:
        resetfig()
        #mb.showinfo("Ошибка", "Это поле под боем противника")



def srvnnant(blawhi, hi):
    global trebunal, abpap, memas, abcdasda
    trebunal = False
    if blawhi - 9 == hi:
        trebunal = True
    if blawhi - 8 == hi:
        trebunal = True
    if blawhi - 1 == hi:
        trebunal = True
    if blawhi - 7 == hi:
        trebunal = True
    if blawhi + 9 == hi:
        trebunal = True
    if blawhi + 8 == hi:
        trebunal = True
    if blawhi + 7 == hi:
        trebunal = True
    if blawhi + 1 == hi:
        trebunal = True
    if hi == wtkinguer or hi == blkinguer or hi == pauer:
        trebunal = False
    if not trebunal:
        resetfig()
        #memas = True
        # abpap = Label(root, image=abc)
        # abpap.place(x=0, y=10)
        # mb.showinfo("Ошибка", "Ход невозможен")
        #abcdasda = Label(root, text=" Настройки")
        #abcdasda.place(x=400,y=100)

xod_sdelan = False
xod = True

def bot():
    global varchel, kto, xod_sdelan, verx, gor, blkinguer, trebunal, pauer, wtkinguer, t1, t2
    verx = 0
    gor = 0
    xx = 80
    x_x = -80
    yy = 80
    y_y = -80
    if blkinguer % 8 == 0:
        xx = 0
    if blkinguer % 8 == 1:
        x_x = 0
    if blkinguer < 8:
        yy = 0
    if blkinguer > 56:
        y_y = 0

    if xod:
        if xod_sdelan:
            if pauer // 8 < blkinguer //8:
                verx = y_y
            if pauer % 8 < blkinguer % 8:
                gor = x_x
            else:
                gor = xx
            if pauer % 8 == blkinguer % 8:
                verx = y_y
                gor = 0
                if blkinguer <= 8:
                    verx = 0
                    gor = xx
                    if blkinguer % 8 == 1:
                        gor = xx
                    else:
                        gor = x_x



            if (pauer % 8 == blkinguer % 8) and ((pauer - blkinguer) > 8):
                gor = 0
                verx = yy

            if gor == 80:
                t1 = 1
            if gor == -80:
                t1 = -1
            if gor == 80:
                t2 = 8
            if verx == -80:
                t2 = -8


            t3 = t1 + t2 + blkinguer
            trebunal = True
            srvnn(wtkinguer, t3)
            if not trebunal:


            # t3 = t1 + t2 + blkinguer
            # trebunal = True
            # srvnn(wtkinguer, t3)
            # if not trebunal:
            #     if t1 == 1:
            #         trebunal = True
            #         srvnn(wtkinguer, t3 - 1)
            #         if trebunal:
            #             gor = 0
            #             t1 = 0
            #         else:
            #             trebunal = True
            #             srvnn(wtkinguer, t3 - 2)
            #             if trebunal:
            #                 gor = -80
            #                 t1 = -1
            #             else:
            #                 # проверка на икс закончилась теперь проверка у
            #                 if t2 == -8:
            #                     trebunal = True
            #                     srvnn(wtkinguer,t3 + 8)
            #                     if trebunal:
            #                         verx = -80
            #
            #     else:
            #         if t1 == 0:
            #             trebunal = True
            #             srvnn(wtkinguer, t3 + 1)
            #             if trebunal:
            #                 gor = 80
            #                 t1 = 1
            #             else:
            #                 trebunal = True
            #                 srvnn(wtkinguer, t3 - 1)
            #                 if trebunal:
            #                     gor = -80
            #                     t1 = -1
            #                 else:
            #                     # Проверка на икс закончилась , теперь точно проверяем на y
            #                     if t2 == -8:
            #                         trebunal = True
            #                         srvnn(wtkinguer, t3 + 8)
            #                         if trebunal:
            #                             verx = -80
            #         else:
            #             # тут мы точно проверяем на то, что т1 была равна нулю
            #             trebunal = True
            #             srvnn(wtkinguer, t3 + 1)
            #             if trebunal:
            #                 gor = 0
            #                 t1 = 0
            #             else:
            #                 trebunal = True
            #                 srvnn(wtkinguer, t3 + 2)
            #                 if trebunal:
            #                     t1 = 1
            #                     gor = 80
            #                 else:
            #                     # точно дело не в х
            #                     if t2 == -8:
            #                         trebunal = True
            #                         srvnn(wtkinguer, t3 + 8)
            #                         if trebunal:
            #                             verx = -80







                #     t3 = t1 + t2
                #     srvnn(wtkinguer, t3)
                # Label(root, text="lasdiasfdoasldifoasofdioasfdoasfodfasodfiasodfiasogd").place(x=50, y=250)
                # t3 = t2+t1
                # srvnn(wtkinguer, t2)
                # trebunal = True





                pass
            if gor == 80:
                blkinguer += 1
            if gor == -80:
                blkinguer -= 1
            if verx == 80:
                blkinguer += 8
            if verx == -80:
                blkinguer -= 8

            kingblacker(gor, verx)
    else:
        pass # белый бот

    xod_sdelan = False

def main(event):
    global ypawn, p1, p, kw, kw1, kb, kb1, ykingblack, yking, xkingblack, xking, vibkb, vibkw, vibp, vibor, pauer, oq,\
        trebunal, memas, abpap, abdef, lepka2, lepka3, lepka1, Lepeshka, lep1, lep2, lep3, Lepblack, Lepwhite, xod, xod_sdelan
    if memas:
        abpap.destroy()
        memas = False
    #if aoooo:
        #abc['text'] = 'Выбрано '+ aaabc
        #itemconfig(abc(text='Выбрано '+ aaabc))
    xx = event.x
    yy = event.y
    #Label(root, text=xx).place(x=50, y=250)
    #oq = (xx - 360) // 80 + (yy - 40) // 80 * 8 + 1
    if started:
        move = False
        oq = (xx - 400) // 50 + (yy - 200) // 50 * 8 + 1
        if (xx >= 400) and (yy >=200) and (xx <= 800) and (yy <= 600):

            cu = oq % 8
            if cu == 0:
                cu = 8



            ck = ceil(oq / 8)


            if lep1 and oq !=lepka2 and oq != lepka3:
                lk = ceil(lepka1 / 8)

                if oq <= 8 or lk < 1:
                    lk = 1
                lep1 = False
                lu = lepka1 % 8
                if lu == 0:
                    lu = 8
                canvas.itemconfig(Lepeshka, fill="pink")
                canvas.move(Lepeshka, (cu - lu) * 50, (ck - lk) * 50)
                Label(root, text=cu).place(x=50, y=50)
                Label(root, text=lu).place(x=50, y=100)
                Label(root, text=ck).place(x=50, y=150)
                Label(root, text=lk).place(x=50, y=200)
                Label(root, text=oq).place(x=50, y=250)
                lepka1 = oq
                move = True
            if lep2 and oq !=lepka1 and oq != lepka3:
                lk = ceil(lepka2 / 8)

                if oq <= 8 or lk < 1:
                    lk = 1
                lep2 = False
                lu = lepka2 % 8
                if lu == 0:
                    lu = 8
                canvas.itemconfig(Lepblack, fill="black")
                canvas.move(Lepblack, (cu - lu) * 50, (ck - lk) * 50)
                lepka2 = oq
                move = True
            if lep3 and oq !=lepka2 and oq != lepka1:
                lk = ceil(lepka3 / 8)

                if oq <= 8 or lk < 1:
                    lk = 1
                lu = lepka3 % 8
                if lu == 0:
                    lu = 8
                lep3 = False
                canvas.itemconfig(Lepwhite, fill="white")
                canvas.move(Lepwhite, (cu - lu) * 50, (ck - lk) * 50)
                lepka3 = oq
                move = True
            if (oq == lepka1) and not lep1 and not lep2 and not lep3 and not move:
                canvas.itemconfig(Lepeshka, fill="red")
                lep1 = True
            if (oq == lepka2) and not lep1 and not lep2 and not lep3 and not move:
                canvas.itemconfig(Lepblack, fill="red")
                lep2 = True
            if (oq == lepka3) and not lep1 and not lep2 and not lep3 and not move:
                canvas.itemconfig(Lepwhite, fill="red")
                lep3 = True

    else:
        oq = (xx - 360) // 80 + (yy - 40) // 80 * 8 + 1
        if xx >= 360 and yy >= 40:
            if vibor:
                if vibp:
                    if pauer > 48:
                        if oq + 16 == pauer:
                            pauer -= 16
                            vibp = False
                            canvas.itemconfig(head, fill=colorpawn)
                            pawner(-160)
                            xod = True
                            xod_sdelan = True

                    if oq + 8 == pauer:
                        pauer -= 8
                        vibp = False
                        canvas.itemconfig(head, fill=colorpawn)
                        pawner(-80)
                        xod = True
                        xod_sdelan = True
                if vibkw:
                    trebunal = True
                    srvnnant(wtkinguer, oq)
                    vibkw = False
                    if trebunal:
                        srvnn(blkinguer, oq)
                    if trebunal:
                        kingwhiter((oq % 8 - wtkinguer % 8) * 80, (oq // 8 - wtkinguer // 8) * 80)
                        trebunal = False
                        xod = True
                        xod_sdelan = True

                if vibkb:
                    vibkb = False
                    if oq == noleft or oq == noright:
                        mb.showinfo("Ошибка", "Это поле под боем противника")
                    else:
                        srvnnant(blkinguer, oq)
                        vibkw = False
                        if trebunal:
                            srvnn(wtkinguer, oq)
                        if trebunal:
                            kingwhiter((oq % 8 - blkinguer % 8) * 80, (oq // 8 - blkinguer // 8) * 80)
                            trebunal = False
                        else:
                            mb.showinfo("Ошибка", "Это поле под боем противника")
                vibor = False
                xod = True



            else:
                if kto:
                    if oq == pauer:
                        canvas.itemconfig(head, fill="red")
                        vibp = True
                        vibor = True
                    if oq == wtkinguer:
                        canvas.itemconfig(head1, fill="red")
                        vibkw = True
                        vibor = True
                else:
                    if oq == blkinguer:
                        canvas.itemconfig(head1black, fill="red")
                        vibkb = True
                        vibor = True
    if xod_sdelan:
        bot()
    #else:
    #    mb.showinfo("Ошибка", "Не смешно, клетка за пределами доски, ход невозможен")

root.bind('<Button-1>', main)


def start():
    global aop
    aop = True


def root1destr():
    global root1
    root1.destroy()

def root2destr():
    global root2
    root2.destroy()


def info():
    global root1
    root1 = Tk()
    root1.title("Об авторе")
    root1.geometry("300x150+500+300")
    root1.resizable(False, False)
    Label(root1, text="            Создатель приложения Альберт Чагаев ").place(x=0, y=10)
    Label(root1, text="                           Созданно в 2019 году ").place(x=0, y=30)
    Label(root1, text="                                   Версия 1.15").place(x=0, y=50)
    Label(root1, text="                 Почта для связи: albertimf@mail.ru ").place(x=0, y=70)
    Button(root1, text=' Окей', command=root1destr, fg='red',font='arial 14').place(x=85, y=93, width=140, )


# цвет 3 варианта доски, цвет фигуры, расстановка фигур в файле
# файл( сохранить, открыть), настройки , об
def info1():
    global root2
    root2 = Tk()
    root2.title("О программе")
    root2.geometry("455x250+400+300")
    Label(root2, text="     Программа разработанна для улучшения навыков игры в шахматы").place(x=0, y=10)
    Label(root2, text="     Что бы победить нужно провести пешку или не дать провести её компьютеру,").place(x=0, y=50)
    Label(root2, text="в зависимости от того, что вы выбрали в настройках").place(x=0, y=70)
    Label(root2, text=" Для перемещения фигуры нажмати на неё, у неё загорится деталь и вы сможете ходить").place(x=0,
                                                                                                                  y=90)
    Label(root2, text=" Пешка ходит на 1 клетку вперёд, король ходит на одну клетку в любую сторону").place(x=0, y=110)
    Button(root2, text=' Окей', command=root2destr, fg='blue', font='arial 22').place(x=120, y=165, width=200, height=50)

#canvas1 = Canvas(root, width=1160, height=760, bg="white")
#canvas.destroy()
#abcdef = canvas.create_rectangle(0, 0, 1160, 760, fill="white", outline="black")
opwhite = 1
opblack = 2

def cheli():
    global label_y1, label_y2, kto
    label_y1 = 30
    label_y2 = 600
    kto = False

def chel():
    global label_y1, label_y2, kto
    label_y1 = 600
    label_y2 = 30
    kto = True


def nastroikiclear(izmenenie):
    global ki, varwhite, opblack, varblack, opwhite, varvariant, Otmenit, kio, rbutton1, rbutton11, rbutton11, rbutton2,\
        rbutton22, rbutton222, rbutton3,rbutton33, rbutton333, var1, var2, var3, xpeshka, ypeshka, colorwhite,  colorblack,\
        colorpawn, varwhite, xblack, yblack, xwhite, ywhite, Lepeshka, arrlabel1, arrlabel2, started, Lepwhite, \
        Lepblack, lep1, lep2, lep3, primenit, lepka1, lepka2, lepka3, color_white_board, color_black_board, label_x,\
        label_y1, label_y2, label_compukter, label_people, pauer, blkinguer, wtkinguer
    #if lep:
    started = False
    deletebl()
    deletewh()
    pedestroyy()
    canvas.Otmenit.destroy()
    canvas.Primenit.destroy()
    ki_chel.destroy()
    ki_mel.destroy()
    rbutton1.destroy()
    rbutton11.destroy()
    #rbutton111.destroy()
    rbutton2.destroy()
    rbutton22.destroy()
    #rbutton222.destroy()
    rbutton3.destroy()
    rbutton33.destroy()
    rbutton_chelovek.destroy()
    rbutton_compukter.destroy()
    #rbutton333.destroy()
    #var1.destroy()
    #var2.destroy()
    #var3.destroy()
    ki.destroy()
    lambada = 0
    while lambada <8:
        arrlabel1[lambada].destroy()
        arrlabel2[lambada].destroy()
        lambada += 1
    canvas.delete(Lepeshka)
    canvas.delete(Lepwhite)
    canvas.delete(Lepblack)

    if peshkacolor:
        colorpawn = colorwhite
    else:
        colorpawn = colorblack
    if varwhite==0:
        colorpawn = "white"

    #lep1 = 40
    if izmenenie:
        pauer = lepka1
        blkinguer = lepka3
        wtkinguer = lepka2
        xpeshka = ((lepka1-1) % 8) * 80
        ypeshka = ((lepka1-1) // 8) * 80
        xwhite = ((lepka2-1) % 8) * 80
        ywhite = ((lepka2-1) // 8) * 80
        xblack = ((lepka3-1) % 8) * 80
        yblack = ((lepka3-1) // 8) * 80
        chessboard(color_white_board, color_black_board)
        label_compukter.destroy()
        label_people.destroy()
        #label_y1 = 5
        #chel(False)
        label_compukter = Label(root, text="Компьютер", bg="white", font="Arial 28")
        label_compukter.place(x=label_x, y=label_y2)

        label_people = Label(root, text="Человек", bg="white", font="Arial 28")
        label_people.place(x=label_x, y=label_y1)
    else:
        chessboard("#E9FB00", "#A64B00")
        label_compukter = Label(root, text="Компьютер", bg="white", font="Arial 28")
        label_compukter.place(x=label_x, y=label_y1)

        label_people = Label(root, text="Человек", bg="white", font="Arial 28")
        label_people.place(x=label_x, y=label_y2)

    otrisovkapeshki(colorpawn, xpeshka, ypeshka)
    otrisovkawhite(colorwhite, xwhite, ywhite)
    otrisovkablack(colorblack, xblack, yblack)
    #kio.destroy()


otmena_smena = False
def otmena():
    global otmena_smena
    otmena_smena = False
    nastroikiclear(otmena_smena)

primena_smena = False
def primena():
    global primena_smena
    primena_smena = True
    nastroikiclear(primena_smena)



# DarkKhaki, Fuchsia ( фиолетовый ) , Lime, White, Black, Blue,

def col1():
    global color_white_board
    color_white_board = "#E9FB00"

def col2():
    global color_white_board
    color_white_board = "Blue"

def col3():
    global color_white_board
    color_white_board = "Lime"

def col11():
    global color_black_board
    color_black_board = "#A64B00"

def col12():
    global color_black_board
    color_black_board = "Fuchsia"

def col13():
    global color_black_board
    color_black_board = "DarkKhaki"


#
# def smenacolor():
#     global colorpawn, colorblack, colorwhite, colorkingblack, colorkingwhite
#
#
#     if peshkacolor:
#         colorpawn = colorwhite
#     else:
#         colorpawn = colorblack
#     colorkingblack = colorblack
#     colorkingwhite = colorwhite


def parazit1():
    global Lepeshka
    Lepeshka.config = "red"






def starting(): # инициализация настроек
    global ki, varwhite, opblack, varblack, opwhite, varvariant, Otmenit, kio, rbutton1, rbutton11, rbutton111,\
        rbutton2, rbutton22, rbutton222, rbutton3, rbutton33, rbutton333, var1, var2, var3, Lepeshka, arrlabel1,\
        arrlabel2, started, lepka1, lepka2, lepka3, Lepblack, Lepwhite, lep1, lep2, lep3, chelik, rbutton_chelovek, \
        rbutton_compukter, varchel, ki_chel, ki_mel, color_white_board, color_black_board, o1, o2
    if color_white_board == "#E9FB00":
        o1 = 1
    if color_white_board == "Blue":
        o1 = 2
    if color_white_board == "Lime":
        o1 = 3
    if color_black_board == "DarkKhaki":
        o2 = 3
    if color_black_board == "Fuchsia":
        o2 = 2
    if color_black_board == "#A64B00":
        o2 = 1
    chelik = chelovek
    varchel = IntVar()
    varchel.set(0)
    rbutton_chelovek = Radiobutton(root, text='Белые', variable=varchel, value=0, command=chel)
    rbutton_compukter = Radiobutton(root, text='Чёрные', variable=varchel, value=1, command=cheli)
    rbutton_chelovek.place(x=400, y=75)
    rbutton_compukter.place(x=400, y=100)




    started = True
    canvas.create_rectangle(0, 0, 1160, 760, fill="white", outline="black")

    ki = Label(root, text=" Настройки")
    ki.place(x=625, y=50)

    ki_chel = Label(root, text=" Выбор цвета фигур")
    ki_chel.place(x=400, y=50)


    ki_mel = Label(root, text="  ")
    ki_mel.place(x=550, y=50)

    label_compukter.destroy()
    label_people.destroy()
# для белых
    varwhite = IntVar()
    varwhite.set(o1)
    rbutton1 = Radiobutton(root, text='Жёлтый', variable=varwhite, value=1, command=col1)
    rbutton2 = Radiobutton(root, text='Синий', variable=varwhite, value=2, command=col2)
    rbutton3 = Radiobutton(root, text='Лаймовый', variable=varwhite, value=3, command=col3)
    rbutton1.place(x=550, y=75)
    rbutton2.place(x=550, y=100)
    rbutton3.place(x=550, y=125)
# для чёрных
    varblack = IntVar()
    varblack.set(o2)
    rbutton11 = Radiobutton(root, text='Коричневый', variable=varblack, value=1, command=col11)
    rbutton22 = Radiobutton(root, text='Фиолетовый', variable=varblack, value=2, command=col12)
    rbutton33 = Radiobutton(root, text='Хаки', variable=varblack, value=3, command=col13)
    rbutton11.place(x=700, y=75)
    rbutton22.place(x=700, y=100)
    rbutton33.place(x=700, y=125)

    coler2 = color_black_board
    coler1 = color_white_board  # светлый
    yboard = 200
    ii = 1
    while ii <= 4:
        i1 = 1
        op = "white"
        xboard = 400
        while i1 <= 8:
            if (i1 % 2) == 0:
                op = coler2
            else:
                op = coler1
            canvas.create_rectangle(xboard, yboard, xboard + 50, yboard + 50, fill=op, outline="black")
            xboard += 50
            i1 = i1 + 1
        xboard = 400
        yboard += 50
        i2 = 1
        while i2 <= 8:
            canvas.create_rectangle(xboard, yboard, xboard + 50, yboard + 50, fill=op, outline="black")
            xboard += 50
            i2 = i2 + 1
            if (i2 % 2) == 1:
                op = coler2
            else:
                op = coler1
        yboard += 50
        ii += 1
    ii = 1
    xx = 425
    arrlabel1 = []
    while ii <= 8:
        arrlabel1.append(Label(root, text=alf.get(ii), fg="green", bg="white", font="Arial 14"))
        arrlabel1[ii-1].place(x=xx, y=170)
        xx += + 50
        ii += 1
    yy = 570
    arrlabel2 = []
    while ii > 1:
        ii -= 1
        arrlabel2.append(Label(root, text=str(9 - ii), fg="green", bg="white", font="Arial 14"))
        arrlabel2[8-ii].place(x=380, y=yy)
        yy -= 50


    Lepeshka = canvas.create_rectangle(410, 205, 440, 245, fill="pink", outline="black")
    lepka1 = 1
    lep1 = False
    Lepblack =canvas.create_rectangle(460, 205, 490, 245, fill="black", outline="black")
    lepka2 = 2
    lep2 = False
    Lepwhite = canvas.create_rectangle(510, 205, 540, 245, fill="white", outline="black")
    lepka3 = 3
    lep3 = False




# кнопка сохранения
    canvas.Primenit = Button(text="Окей", background="Lime", command=primena)
    canvas.Primenit.place(x=830, y=350, width=140, height=50)



        #canvas.Primenit.destroy()
# кнопка отмены
    canvas.Otmenit = Button(text="Отменить", background="Lime", command=otmena)
    canvas.Otmenit.place(x=830, y=450, width=140, height=50)
    #canvas.Otmenit.destroy()
    #canvas.butn = Button(text="Старт", background="#F00", command=start).place(x=70, y=100, width=70)



butn1 = Button(text="Старт", background="#F00", command=nachali)
butn1.place(x=70, y=100, width=140)
butn2 = Button(text="Пауза", background="#F00", command=paused)
butn2.place(x=70, y=130, width=140)
butn3 = Button(text="Выйти", background="#F00", command=vihod)
butn3.place(x=70, y=160, width=140)


# Надо записывать/сохранять: цвет полей: белое/чёрное, каким цветом человек играет,
# расположение пешки, белого короля и чёрного короля,

def otkrit_fail():
    global a_col, file_name, yu, color_white_board, color_black_board, wtkinguer, blkinguer, pauer, opana, label_compukter, label_people
    file_name = fd.askopenfilename()
    yu = open(file_name)
    a_col = int(yu.readline())
    if a_col == 1:
        color_white_board = "#E9FB00"
    if a_col == 2:
        color_white_board = "Blue"
    if a_col == 3:
        color_white_board = "Lime"
    b_col = int(yu.readline())
    if b_col == 1:
        color_black_board= "DarkKhaki"
    if b_col == 2:
        color_black_board = "Fuchsia"
    if b_col == 3:
        color_black_board = "#A64B00"
    chessboard(color_white_board, color_black_board)
    pauer = int(yu.readline())
    blkinguer = int(yu.readline())
    wtkinguer = int(yu.readline())
    xpeshka = ((pauer - 1) % 8) * 80
    ypeshka = ((pauer - 1) // 8) * 80
    otrisovkapeshki(colorpawn, xpeshka, ypeshka)
    xwhite = ((wtkinguer - 1) % 8) * 80
    ywhite = ((wtkinguer - 1) // 8) * 80
    otrisovkawhite(colorkingwhite, xwhite, ywhite)
    xblack = ((blkinguer - 1) % 8) * 80
    yblack = ((blkinguer - 1) // 8) * 80
    otrisovkablack(colorblack, xblack, yblack)
    opana = int(yu.readline())
    label_compukter.destroy()
    label_people.destroy()
    if opana == 5000:
        chel
    else:
        cheli
    label_compukter = Label(root, text="Компьютер", bg="white", font="Arial 28")
    label_compukter.place(x=label_x, y=label_y2)
    label_people = Label(root, text="Человек", bg="white", font="Arial 28")
    label_people.place(x=label_x, y=label_y1)
    yu.close()


def save_fail():
    global yu , a_col, b_col, pauer, blkinguer, wtkinguer
    file_name = fd.asksaveasfilename(defaultextension=".txt")
    yu = open(file_name, "w")
    b_col = 5
    if color_white_board == "#E9FB00":
        a_col = 1
    if color_white_board == "Blue":
        a_col = 2
    if color_white_board == "Lime":
        a_col = 3
    if color_black_board == "DarkKhaki":
        b_col = 1
    if color_black_board == "Fuchsia":
        b_col = 2
    if color_black_board == "#A64B00":
        b_col = 3
    yu.writelines(str(a_col) + "\n")
    yu.writelines(str(b_col) + '\n')
    yu.writelines(str(pauer) + '\n')
    yu.writelines(str(blkinguer) + '\n')
    yu.writelines(str(wtkinguer) + '\n')
    if label_y2 == 30:
        yu.writelines("12312" + '\n')
    else:
        yu.writelines("5000" + '\n')
    yu.close()


main_menu = Menu()
file_menu = Menu(tearoff=0)
file_av = Menu(tearoff=0)
main_menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=otkrit_fail)
file_menu.add_command(label="Сохранить", command=save_fail)
file_menu.add_command(label="Выход", command=vihod)
main_menu.add_cascade(label="Настройки", command=starting)
main_menu.add_cascade(label="Справка", menu=file_av)
file_av.add_command(label="Об авторе", command=info)
file_av.add_command(label="О программе", command=info1)

root.config(menu=main_menu)

root.mainloop()
