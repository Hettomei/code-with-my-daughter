from tkinter import *

root = Tk()

frame = Frame(root, width=1100, height=800)
frame.pack(expand=True, fill=BOTH)

canvas = Canvas(frame, bg="white", width=1500, height=700)

coordinates = 600, 400, 700, 500
mur_jaune = canvas.create_rectangle(coordinates, fill="yellow")

canvas.pack(expand=True, fill=BOTH)
photo = PhotoImage(file="voiture1.png")
voiture = canvas.create_image(150, 150, image=photo)


def roule(event):
    canvas.move(voiture, 10, 0)


def recule(event):
    canvas.move(voiture, -10, 0)


def monte(event):
    canvas.move(voiture, 0, -10)


def descend(event):
    canvas.move(voiture, 0, 10)


frame.focus_set()
frame.bind("<Right>", roule)
frame.bind("<Left>", recule)
frame.bind("<Up>", monte)
frame.bind("<Down>", descend)

root.mainloop()
