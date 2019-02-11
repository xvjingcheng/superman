"""
浮雕布局
relief:3D效果
FLAT    ---平的
RAISED  ---凸起的
RIDGE   ---脊状边缘
SUNKEN  ---凹陷
GROOVE  ---沟状
"""
import tkinter

window = tkinter.Tk()

window.geometry("400x400")

BTN00 = tkinter.Button(window, text="BTN00", bg="red")
BTN00.grid(row=1, column=6)

BTN01 = tkinter.Button(window, text="平的平的", bg="orange", relief="flat")
BTN01.grid(row=2, column=5)

BTN02 = tkinter.Button(window, text="凸起凸起", bg="yellow", relief="raised")
BTN02.grid(row=3, column=4)

BTN03 = tkinter.Button(window, text="脊状脊状", bg="green", relief="ridge")
BTN03.grid(row=4, column=3)

BTN04 = tkinter.Button(window, text="凹陷凹陷", bg="blue", relief="sunken")
BTN04.grid(row=5, column=2)

BTN05 = tkinter.Button(window, text="沟状沟状", bg="blue", relief="groove")
BTN05.grid(row=6, column=1)

window.mainloop()
