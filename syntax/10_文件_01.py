f = open('访问模式.txt', 'r', encoding='utf-8')
# a = f.read()

for line in f.readlines():
    print(line)

f.close()