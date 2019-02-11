import tkinter

window = tkinter.Tk()
window.geometry("400x300+1000+200")
window.resizable(width=True, height=False)

# 输入框布局
input_frame = tkinter.Frame(window, width=30, height=30)
# input_frame.pack(side="top")
input_frame.place(x=50, y=10)
entry = tkinter.Entry(input_frame, width=30)
entry.pack(side="left")

# 查询按钮
btn_search = tkinter.Button(input_frame, text="查询")
# btn_search.pack(side="left")
btn_search.place(x=200, y=1)

# 退出按钮
btn_search = tkinter.Button(input_frame, text="退出", command=window.quit)
btn_search.pack(side="right")

scroll = tkinter.Scrollbar()
scroll.pack(side="right", fill=tkinter.Y)

txt = tkinter.Text(window, width=50, height=18)
txt.pack(side="bottom")

# 关联滚动条和文字
txt.config(yscrollcommand=scroll.set)
scroll.config(command=txt.yview)

window.mainloop()
