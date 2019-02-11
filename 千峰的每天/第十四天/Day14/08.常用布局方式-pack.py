"""
相对布局
    pack
        side=left/right/top/bottom
"""
import tkinter

window = tkinter.Tk()

window.geometry("400x400")

button1 = tkinter.Button(window, text="BTN1", bg="yellow")
button1.pack(side="top")

button2 = tkinter.Button(window, text="BTN2", bg="yellow")
button2.pack(side="left")

button3 = tkinter.Button(window, text="BTN3", bg="yellow")
button3.pack(side="bottom")

button4 = tkinter.Button(window, text="BTN4", bg="yellow")
button4.pack(side="right")

window.mainloop()
