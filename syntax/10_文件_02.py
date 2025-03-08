# 除了 open函数而外，还有 一种加强版

# 读取一行就复制3次
# with open('a.txt', 'r') as f1, open('b.txt', 'w') as f2:
#     for line in f1:
#         stripped_line = line.strip()  # 去除行末的换行符
#         for _ in range(3):  # 复制3次
#             f2.write(stripped_line + '\n')  # 写入到输出文件并添加换行符

# 读取一行就复制3次 ，方法2
# with open('a.txt', 'r+') as file:
#     lines = file.readlines()  # 读取所有行
#     file.seek(0)  # 将文件指针移动到文件开头
#     for line in lines:
#         stripped_line = line.strip()  # 去除行末的换行符
#         for _ in range(3):  # 复制3次
#             file.write(stripped_line + '\n')  # 写入到文件并添加换行符
#     file.truncate()  # 截断文件，删除多余的内容

with open('a.txt', 'r+') as file:
    print(file.seek(10))
    print(file.tell())

