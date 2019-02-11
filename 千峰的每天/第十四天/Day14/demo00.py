import tkinter

# 创建窗口
from tkinter import Frame

window = tkinter.Tk()
# 设置窗口
window.title("英汉词典")
window.geometry("500x500")


# 控制台输出信息的方法
def show_info():
    print("666")


# 显示按钮
btn_show = tkinter.Button(window, text="查询", command=show_info)
btn_show.pack(side="left")

# 退出按钮
btn_exit = tkinter.Button(window, text="退出", command=window.quit)
btn_exit.pack(side="right")

# 按钮布局
btn_frame = Frame(window, height=30)
btn_frame.pack()
#
# # 显示按钮
# btn_show = tkinter.Button(btn_frame, text="查询", command=show_info)
# btn_show.pack(side="left")
#
# # 退出按钮
# btn_exit = tkinter.Button(btn_frame, text="退出", command=window.quit)
# btn_exit.pack(side="right")

# 消息循环
window.mainloop()
