# 在文件打开是，如果文件不存在就会直接报错，影响后续代码执行

try:
    with open('aa.txt', 'r') as f:
        pass
except:
    print("文件没有找到")