"""

"""
import time

start_time = time.time()
# 创建读和写的流对象
file_r = open(r"E:\一周不死，全额退款.mp4", mode="rb")
file_w = open(r"E:\一周不死，全额退款-副本.mp4", mode="wb")

while True:
    # 读取文件内容
    content = file_r.read(8 * 1024)
    if len(content) != 0:
        # 写入文本内容
        file_w.write(content)
    else:
        break

file_w.close()
file_r.close()

end_time = time.time()
print("消耗总时间%s" % (end_time - start_time))
