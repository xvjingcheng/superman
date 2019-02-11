import tkinter

# 创建窗口对象
window = tkinter.Tk()
# 设置窗口标题
window.title("我的第一个窗口")
# 设置窗口位置和尺寸,参数以字符串的格式编写，前两个是宽和高，用小写埃克斯x连接，后面是屏幕中的位置，用加号连接
window.geometry("400x400+1000+200")


def show():
    print("我是show按钮")


button = tkinter.Button(master=window, text="查询", width=10, height=1, command=show)
button.pack()
btn_quit = tkinter.Button(master=window, text="退出", width=10, height=1, command=window.quit)
btn_quit.pack()

# 框架
frame = tkinter.Frame(master=window, width="100", height=100, bg="red")
frame.pack()

window.mainloop()
