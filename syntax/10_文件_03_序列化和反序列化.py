import json

# 通过文件操作，我们可以将字符串写入到一个本地文件。但是，如果是一个对象(例如列表、字典、元组等)，就无
# 法直接写入到一个文件里，需要对这个对象进行序列化，然后才能写入到文件里。
# 设计一套协议，按照某种规则，把内存中的数据转换为字节序列，保存到文件，这就是序列化，反之，从文件的字
# 节序列恢复到内存中，就是反序列化。
# 对象---》字节序列 === 序列化
# 字节序列--》对象 ===反序列化
# Python中提供了JSON这个模块用来实现数据的序列化和反序列化

# JSON(JavaScriptObjectNotation, JS对象简谱)是一种轻量级的数据交换标准。JSON的本质是字符串

# JSON提供了dump和dumps方法，将一个对象进行序列化。
# dumps方法的作用是把对象转换成为字符串，它本身不具备将数据写入到文件的功能。
person = {
    'name': 'xiaofang',
    'age': 18,
    'address': 'china'

}

result = json.dumps(person)
# print(type(result))
# print(result)

# 写入到文件
# with open('10_文件_03_序列化和反序列化.txt', 'w') as file:
#     file.write(result)
#
#     file.close()

# dump方法可以在将对象转换成为字符串的同时，指定一个文件对象，把转换后的字符串写入到这个文件里。
# with open('10_文件_03_序列化和反序列化1.txt', 'w') as file1:
#     json.dump(person, file1)
#
#     file1.close()



# 反序列化
# 使用loads和load方法，可以将一个JSON字符串反序列化成为一个Python对象。
# loads方法需要一个字符串参数，用来将一个字符串加载成为Python对象。
person1 = json.load('{"name": "xiaofang", "age": 18, "address": "china"}')
print(type(person1))
print(person1)