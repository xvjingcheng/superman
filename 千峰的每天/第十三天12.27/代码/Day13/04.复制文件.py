"""
读取本地指定文件所有内容
写入到一个新的文件
"""

import time
start_time = time.time()
file = open("MissDong.wma", mode="rb+")
# 读取文件内容
content = file.read()
file.close()

file = open("MissDong_Copy.wma", mode="wb+")
# 写入内容
file.write(content)
file.close()

end_time = time.time()
print("消耗总时间%s" % (end_time - start_time))
