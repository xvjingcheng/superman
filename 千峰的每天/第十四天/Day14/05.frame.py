"""
框架

"""
from tkinter import *

window = Tk()

window.geometry("400x300+1000+200")
# 框架，容器
frame = Frame(master=window, width=3000, height=30)
frame.pack(side="top")

# 输入框
entry = Entry(frame, width=30)
entry.pack(side="left")

# 按钮
btn_quit = Button(frame, text="退出")
btn_quit.pack(side="right")

# 按钮
btn_in = Button(frame, text="查询")
btn_in.pack(side="right")

txt = Text(window, width=40, height=20)
txt.pack()

window.mainloop()
