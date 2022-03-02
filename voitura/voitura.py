from tkinter import *
import sys
from turtle import color
import pygame


def dessine_route_horizontale():
    canvas.create_line(0, 400, 1600, 400, width=5)

    canvas.create_line(0, 450, 1600, 450, width=54)
    canvas.create_line(0, 450, 1600, 450, width=3, dash=(20, 10), fill="white")

    canvas.create_line(0, 500, 1600, 500, width=5)


def dessine_route_vertical():
    canvas.create_line(1100, 0, 1100, 1100, width=5)

    canvas.create_line(1150, 0, 1150, 1150, width=54)
    canvas.create_line(1150, 0, 1150, 1150, width=3, dash=(20, 10), fill="white")

    canvas.create_line(1200, 0, 1200, 1200, width=5)

def dessine_stop(x,y):
    canvas.create_line(x, y, x, y+100, width=8,fill="purple")
    canvas.create_oval(x-30,y-30,x+30,y+30,fill="red")
    Label(canvas, text="STOP", bg="red",fg="white" , font=("Courier", 10) ).place(x=x-15, y=y)

def fait_pouet(event):
    pygame.mixer.Sound.play(klaxon_sound)


def fait_pouet_monte(event):
    pygame.mixer.Sound.play(klaxon_sound)
    canvas.move(voiture_bloque, 0, -10)

def fait_pouet_descend(event):
    pygame.mixer.Sound.play(klaxon_sound)
    canvas.move(voiture_bloque, 0, 10)


def fait_pouet_recule(event):
    pygame.mixer.Sound.play(klaxon_sound)
    canvas.move(voiture_bloque, -10, 0)


def fait_pouet_avance(event):
    pygame.mixer.Sound.play(klaxon_sound)
    canvas.move(voiture_bloque, 10, 0)

def automatique_descend():
    canvas.move(voiture_roule, 0, 2)
    x,y, *_ = canvas.bbox(voiture_roule)
    if y > 1100:
        canvas.coords(voiture_roule, 1150, 20)
    canvas.after(20, automatique_descend)

def roule(event):
    canvas.move(voiture, 10, 0)


def recule(event):
    canvas.move(voiture, -10, 0)


def monte(event):
    canvas.move(voiture, 0, -10)


def descend(event):
    canvas.move(voiture, 0, 10)


def close(event):
    sys.exit()  # if you want to exit the entire thing


root = Tk()

pygame.init()
klaxon_sound = pygame.mixer.Sound("pouet.wav")

frame = Frame(root, width=1600, height=1500)
frame.pack(expand=True, fill=BOTH)

canvas = Canvas(frame, bg="white", width=1600, height=1500)

coordinates = 600, 400, 800, 500

canvas.pack(expand=True, fill=BOTH)
photo = PhotoImage(file="voiture1.png")
photo_bloque = PhotoImage(file="voiture3.png")
photo_roule = PhotoImage(file="voiture5.png")
dessine_route_horizontale()
dessine_route_vertical()
dessine_stop(1000,320)
voiture = canvas.create_image(-10, 440, image=photo)
voiture_bloque = canvas.create_image(430, 440, image=photo_bloque)
voiture_roule = canvas.create_image(1150, 20, image=photo_roule)

mur_jaune = canvas.create_rectangle(coordinates, fill="yellow")
Label(canvas, text="garage", bg="yellow", font=("Courier", 30)).place(x=610, y=410)

frame.focus_set()
frame.bind("<Right>", roule)
frame.bind("<Left>", recule)
frame.bind("<Up>", monte)
frame.bind("<Down>", descend)
frame.bind("<Escape>", close)
frame.bind("k", fait_pouet)

frame.bind("<KP_8>", fait_pouet_monte)
frame.bind("<KP_5>", fait_pouet_descend)
frame.bind("<KP_4>", fait_pouet_recule)
frame.bind("<KP_6>", fait_pouet_avance)

automatique_descend()


root.mainloop()
