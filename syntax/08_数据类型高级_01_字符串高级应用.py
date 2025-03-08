# 字符串在 Python 中是不可变的序列，因此有很多可用的方法。以下是一些常用的字符串方法：
#
#     upper(): 返回字符串的大写版本。
#     lower(): 返回字符串的小写版本。
#     capitalize(): 返回字符串的首字母大写版本。
#     title(): 返回字符串中每个单词的首字母大写版本。
#     strip(): 返回移除字符串两侧空白字符的版本。
#     lstrip(): 返回移除字符串左侧空白字符的版本。
#     rstrip(): 返回移除字符串右侧空白字符的版本。
#     replace(old, new): 返回将字符串中所有的 old 子串替换为 new 的版本。
#     split(sep=None, maxsplit=-1): 返回根据指定分隔符 sep 将字符串分割成子串的列表。
#     join(iterable): 返回使用字符串作为分隔符将可迭代对象中的元素连接起来的字符串。
#     startswith(prefix): 如果字符串以指定的 prefix 开头，则返回 True，否则返回 False。
#     endswith(suffix): 如果字符串以指定的 suffix 结尾，则返回 True，否则返回 False。
#     find(sub[, start[, end]]): 返回字符串中第一次出现子字符串 sub 的索引，如果未找到则返回 -1。
#     index(sub[, start[, end]]): 返回字符串中第一次出现子字符串 sub 的索引，如果未找到则引发 ValueError。
#     count(sub[, start[, end]]): 返回子字符串 sub 在字符串中出现的次数。
#
# 这些方法使得在处理字符串时能够进行各种操作，包括大小写转换、分割、替换等。

a = ' hello world123 '
b = " HELLO world123 "
c = 'hello'
print(type(a))
print(type(b))

print(a.upper())
print(b.lower())
print(a.capitalize())
print(c.capitalize())  # 这个方法前面有空格会失效
print(a.title())

print(a.lstrip())
print(a.rstrip())
print(a.strip())

print(a.replace('123', '789'))
print(a.split(' '))
print(c.split(' '))

print('.'.join(['a', 'b', 'c']))

# 获取长度:len len函数可以获取字符串的长度。
# print(len(a))

# 查找内容:find 查找指定内容在字符串中是否存在，如果存在就返回该内容在字符串中第一次
# 出现的开始位置索引值，如果不存在，则返回-1
# print(a.find('o'))

# 判断:startswith,endswith 判断字符串是不是以谁谁谁开头/结尾
# print(a.startswith('he'))
# print(a.endswith('123'))

# 计算出现次数:count 返回 str在start和end之间 在 mystr里面出现的次数
# print(a.count('l'))

# 替换内容:replace 替换字符串中指定的内容，如果指定次数count，则替换不会超过count次。
# print(a.replace('123', '789'))

# 切割字符串:split 通过参数的内容切割字符串
# print(a.split(' ')) # ['hello', 'world123']

# 修改大小写:upper,lower 将字符串中的大小写互换
# print("hello".upper())
# print("HELLO".lower())

# 空格处理:strip 去空格，去掉首位空格
# print('  abc  def g  '.strip())

# 字符串拼接:join 字符串拼接
# print('hello'.join('123')) # 1hello2hello3

# 判断字符串是否全部为空格
# astr = "     "
# if astr.isspace():
#     print("只包含空格")
# else:
#     print("不只是包含空格")
