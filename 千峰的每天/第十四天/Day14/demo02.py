import tkinter
from tkinter import *


# 显示信息
def show_info():
    text.insert("1.0", entry.get() + "\n")


# 创建窗口
window = tkinter.Tk()

# 配置窗口
window.title("英汉词典")
window.geometry("500x300")
window.resizable(width=True, height=False)

# 输入框布局
input_frame = Frame(window, width=30, height=30)
input_frame.pack(side="top")

# 输入框
entry = Entry(input_frame, width=30)
entry.pack(side="left")

# 查询按钮
btn_search = Button(input_frame, text="查询", command=show_info)
btn_search.pack(side="left")

# 退出按钮
btn_search = Button(input_frame, text="退出", command=window.quit)
btn_search.pack(side="right")


# 清空数据
def clear_info():
    text.delete(0.0, tkinter.END)


# 滚动条
scroll = tkinter.Scrollbar()
scroll.pack(side="right", fill=tkinter.Y)

# 文本
text = Text(window, width=68, height=20)
text.pack(side="bottom")

# 关联滚动条和文字
text.config(yscrollcommand=scroll.set)
scroll.config(command=text.yview)

# 循环消息
window.mainloop()
