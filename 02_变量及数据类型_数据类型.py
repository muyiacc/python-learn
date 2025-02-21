# number 类型
aint = 10  # int
along = 10  # long，实际上，python3中已经可以用int类型表示很大的整数，不再需要使用long类型
afloat = 10.0  # float
acomplex = 10 + 110j  # complex

print(aint)
print(along)
print(afloat)
print(acomplex)

# 布尔类型
abool = True  # 需要首字母大写
bbool = False

print(abool)
print(bbool)

# String 类型
astring = 'hello world'

print(astring)

# list 列表
alist = [1436, -23, '3', 100.01]

print(alist)

alist[-1] = '最后一个'

print(alist[-1])

# tuple 元组
atuple = (1, 346, 2, 2, '1')
# atuple = (124, 5, 758, 3) # 可重新赋值
# atuple[0] = 102  # 不可对元组的元素重新赋值 TypeError: 'tuple' object does not support item assignment

print(atuple)

adictionary = {
    'a': 10,
    'b': 10
}

print(adictionary)
print(adictionary['a'])
