"""
file = open("file_path", mode="模式",...)

with open("file_path", mode="模式",...) as file:
    file.read、write
"""
with open("demo09.txt", mode="r+", encoding="utf-8") as file:
    file.write("倭堕低梳髻，连娟细扫眉。终日两相思。为君憔悴尽，百花时。")

# print(file.read())
