# 如果首行，尾行为空，则删除
f = open('访问模式.txt', 'r+', encoding='utf-8')

for line in f.readlines():
    if line.isspace():
        line = ''

    f.write(line)