from tkinter import *

root = Tk()

frame = Frame(root, width=1100, height=800)
frame.pack(expand=True, fill=BOTH)

canvas = Canvas(frame, bg="white", width=1000, height=700)

coordinates = 600, 400, 700, 500
arc = canvas.create_rectangle(coordinates, fill="yellow")

canvas.pack(expand=True, fill=BOTH)

root.mainloop()
