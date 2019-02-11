import tkinter

# 创建主窗口
window = tkinter.Tk()

window.title("Lable")

window.geometry("400x400+1000+200")
# 创建label控件
label = tkinter.Label(master=window, text="abcdefghijklmnopqrstuvwxyz",
                      wraplength=300, justify="right",
                      width=30, height=10,
                      font="20,黑体", foreground="red",
                      background="blue", anchor="ne")
# 把控件添加到主窗口
# pack是一个布局管理器，一个弹性的容器
label.pack()

window.mainloop()
