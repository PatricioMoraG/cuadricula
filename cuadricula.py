from sys import argv
import tkinter as tk
from tkinter import filedialog
import cv2

def onOpen():
    global photo
    filename = filedialog.askopenfilename()
    photo = tk.PhotoImage(file=filename)
    img = cv.imread(cv.samples.findFile("starry_night.jpg"))
    can.create_image(2, 2, image=photo)

ventana = tk.Tk()

photo = tk.PhotoImage(file="spinner.png")
can = tk.Canvas(ventana, height=500, width=500)
can.create_image(250,250, image=photo)
can.pack()

button = tk.Button(ventana, text ="Load Image", command=onOpen)
button.pack()

ventana.mainloop()
