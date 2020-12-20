from tkinter import *
import sys

root = Tk()

frame = Frame(root, width=1100, height=800)
frame.pack(expand=True, fill=BOTH)

canvas = Canvas(frame, bg="white", width=1500, height=700)

coordinates = 600, 400, 800, 500

canvas.pack(expand=True, fill=BOTH)
photo = PhotoImage(file="traineaup.png")
cad = PhotoImage(file="cadeau.png")

voiture = canvas.create_image(150, 150, image=photo)
mur_jaune = canvas.create_rectangle(coordinates, fill="red")
Label(canvas, text="maison", bg="red", font=("Courier", 30)).place(x=610, y=410)


def roule(event):
    canvas.move(voiture, 10, 0)


def recule(event):
    canvas.move(voiture, -10, 0)


def monte(event):
    canvas.move(voiture, 0, -10)


def descend(event):
    canvas.move(voiture, 0, 10)


def pose_cadeau(event):
    x, y = canvas.coords(voiture)
    cadeau = canvas.create_image(x - 150, y, image=cad)


def close(event):
    root.destroy()
    sys.exit()  # if you want to exit the entire thing


frame.focus_set()
frame.bind("<Right>", roule)
frame.bind("<Left>", recule)
frame.bind("<Up>", monte)
frame.bind("<Down>", descend)
frame.bind("<space>", pose_cadeau)
frame.bind("<Escape>", close)

root.mainloop()
