import tkinter

# 创建窗口对象
window = tkinter.Tk()
# 设置窗口标题
window.title("我的第一个窗口")
# 设置窗口位置和尺寸,参数以字符串的格式编写，前两个是宽和高，用小写埃克斯x连接，后面是屏幕中的位置，用加号连接
window.geometry("400x400+1000+200")

window.mainloop()
