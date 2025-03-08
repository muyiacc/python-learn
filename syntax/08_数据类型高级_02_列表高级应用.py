# 对列表的操作一般都是增删查改

# 在Python中，列表是一种非常常用的数据类型，具有丰富的方法来操作和修改列表。以下是一些常用的列表方法：
#
#     append(x): 在列表末尾添加元素 x。
#     extend(iterable): 将可迭代对象中的元素逐个添加到列表末尾。
#     insert(i, x): 在索引 i 处插入元素 x。
#     remove(x): 移除列表中第一个值为 x 的元素。
#     pop(i): 移除并返回索引为 i 的元素，如果未指定索引，则默认移除并返回最后一个元素。
#     clear(): 移除列表中的所有元素。
#     index(x, start, end): 返回第一个值为 x 的元素的索引，如果未找到则引发 ValueError。
#     count(x): 返回元素 x 在列表中出现的次数。
#     sort(key=None, reverse=False): 对列表进行排序，可以指定排序时使用的关键字函数和是否降序排序。
#     reverse(): 反转列表中的元素顺序。
#     copy(): 返回列表的浅拷贝。
#
# 这些方法使得在Python中能够方便地对列表进行添加、删除、查找和排序等操作。

list = ['hello', 'world', 'python', 'python']

list.append('golang')
print(list)

list.extend([1, 1, 3])
print(list)

list.insert(-1, 'java')
print(list)

list.remove(1)
print(list)

pop_el = list.pop(1)
print(pop_el)
print(list)

python_index = list.index('python')
print(python_index)

o_count = list.count('python')
print(o_count)


# 按照首字符的大小排序
def first_char(item):
    return str(item)[0]


list.sort(key=first_char)
print(list)


print('---------------')
# 打印列表中首字符对应的数字
for item in list:
    match type(item).__name__:
        case 'int':
            print("%s是int类型" % item)
        case 'str':
            print(f"{item}，第一个字符 {item[0]} 的值为：{ord(item[0])}")
        case _:
            print("不匹配")


list.reverse()
print(list)

# 原始列表
original_list = [1, [2, 3], 4]
# 进行浅拷贝
shallow_copy = original_list.copy()
# 修改原始列表中的子列表
original_list[1][0] = 'a'
# 输出原始列表和浅拷贝后的列表
print(original_list)  # 输出: [1, ['a', 3], 4]
print(shallow_copy)   # 输出: [1, ['a', 3], 4]

# append 在末尾添加元素
# list.append('learn')
# print(list)

# insert 在指定位置插入元素
# list.insert(2, 'insert123')
# print(list)

# extend 合并两个列表
# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)

# 修改元素
# aa = ['a', 'b', 'c', 'd']
# aa[0] = 'b'
# print(aa)


# 查找 in  和 not in
# name_list = ['jack', 'tom', 'tony']
# input_name = input("请输入你要查找的名字：")
# if input_name in name_list:
#     print('存在这个名字')
# else:
#     print("没有这个名字")


# 删除元素
# del: delete according to the index
# print(len(list))
# del list[-1]
# print(len(list))

# pop: remove element, the last one is deleted by default, and an index can be specified for deletion
# print(list)
# list.pop()
# print(list)
# list.pop(0)
# print(list)

# remove:
