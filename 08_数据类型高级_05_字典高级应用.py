# 对字典的操作

# Python 字典是一种无序的数据类型，用于存储键值对。字典中的键必须是唯一的，而值可以是任意数据类型（包括其他字典）。下面是一些常用的 Python 字典方法：
#
#     clear(): 清空字典中的所有元素。
#     copy(): 返回字典的浅拷贝。
#     fromkeys(seq, value): 创建一个新字典，其中包含指定序列中的元素作为键，所有键对应的值都是指定的值。
#     get(key, default=None): 返回指定键的值，如果键不存在，则返回默认值（默认为 None）。
#     items(): 返回一个包含所有（键，值）对的元组的列表。
#     keys(): 返回一个包含字典所有键的列表。
#     values(): 返回一个包含字典所有值的列表。
#     pop(key, default): 删除并返回指定键的值，如果键不存在，则返回默认值（如果没有指定默认值，则会抛出 KeyError 异常）。
#     popitem(): 删除并返回字典中的一对键和值，以便以元组形式返回（在 Python 3.7+ 中，返回的是最后一个键值对）。
#     update(other_dict): 将另一个字典或键值对序列中的元素添加到当前字典中。
#     setdefault(key, default=None): 如果键存在于字典中，则返回其值。如果键不存在，则插入键并返回默认值（默认为 None）。
#     __contains__(key): 检查字典中是否包含指定的键，如果包含则返回 True，否则返回 False。
#
# 这些方法可以帮助你对字典进行操作，包括获取键值对、添加新的键值对、删除键值对等操作。



info = {
    'name': 'xiaofang',
    'age': 18,
}

info1 = {
    'name': 'xiaofang',
    'age': 18,
}

print(info.__contains__('name'))
print(info.__eq__(info1))



# print(info.get('age'))
# print(info.get('name'))

# print(info.get('gender'))  # Non-existent key will not report an error, returning None
# print(info.get('gender', 'female'))  # Non-existent key will not report an error, returning None

# add
# info['adress'] = 'china'
# print(info)

# delete
# pop()
# info.pop('name')  # delete according to key
# print(info)

# del
# del info['age']
# print(info)

# clear() :
# info.clear()
# print(info)

# del info  # delete all dic
# print(info) # info is not defined




# info1 = {
#     'name': 'xiaofang',
#     'age': 18,
# }
#
# # traversal dictionary
# for key in info1.keys():
#     print(key)
#
# for value in info1.values():
#     print(value)
#
# for key, value in info1.items():
#     print("key=%s, value=%s" % (key, value))
