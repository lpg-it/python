# # 字典的创建方式
# # 方式一:
# dic = dict((('k1', 'v1'), ('k2', 'v2')))
# print(dic)
#
# # 方式二:
# dic = dict(one=1, two=2, three=3)
# print(dic)
#
# # 方式三:
# dic = dict({'k1': 'v1', 'k2': 'v2'})
# print(dic)
#
#
# # 验证字典的合法性
# # dic = {[11, 22, 33]: 'qwe'}
# # print(dic)
#
# dic = {1: '123', 1: '456', 2: '789'}
# print(dic)  # {1: '456', 2: '789'}
#
#
# # 字典的增删改查
# dic = {'name': '柯南', 'age': 18, 'hobby_list': ['打篮球', '唱歌', '跳舞']}
# # 增: 直接增加: 有则改之, 无则增加
# dic['gender'] = '男'
# print(dic)
# dic['age'] = 23  # 改
# print(dic)
#
# # setdefault: 有则不变, 无则增加
# dic.setdefault('k1')
# print(dic)
# dic.setdefault('k1', 'v1')
# print(dic)
# dic.setdefault('k2', 'v2')
# print(dic)
# dic.setdefault('name', 'conan')
# print(dic)


# 删
# pop, 按照 键 删除 键值对, 有返回值, 返回删除的键值对
# 如果有第二个参数, 则字典中有无此键都不会报错
dic = {'name': '柯南', 'age': 18, 'hobby_list': ['打篮球', '唱歌', '跳舞']}
dic.pop('age')
print(dic)
# dic.pop('123')  # KeyError: '123'
dic.pop('123', '没有此键.')
ret = dic.pop('123', '没有此键.')
print(ret)  # 没有此键.
print(dic)

# clear: 清空
# dic.clear()
# print(dic)

# del
# del dic['name']
# print(dic)
# del dic['age11']  # KeyError: 'age11'
# print(dic)
# del dic
# print(dic)


# 改
dic['name'] = 'kidd'
print(dic)


# 查
print(dic['name'])
# print(dic['name11'])  # KeyError: 'name11'

# get ***
print(dic.get('name'))
print(dic.get('name1'))  # None
print(dic.get('name1', '没有此键'))  # 没有此键


# 三个特殊的
# keys(), values(), items()

# keys()
print(dic.keys(), type(dic.keys()))  # dict_keys(['name', 'hobby_list']) <class 'dict_keys'>

# 可以转化成列表
li = list(dic.keys())
print(li)
for i in li:
    print(i)


# values()
print(dic.values(), type(dic.values()))  # dict_values(['kidd', ['打篮球', '唱歌', '跳舞']]) <class 'dict_values'>

# 可以转化成列表
li = list(dic.values())
print(li)
for i in li:
    print(i)


# items()
print(dic.items(), type(dic.items()))
# dict_items([('name', 'kidd'), ('hobby_list', ['打篮球', '唱歌', '跳舞'])]) <class 'dict_items'>

for key, value in dic.items():
    print(key, value)

a, b = ('name', 'conan')
print(a, b)


# 面试题
# 用一行代码转换a, b之间的值
a = 18
b = 12
a, b = b, a
print(a, b)


# 练习题
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
dic['k4'] = 'v4'
print(dic)

# 请在修改字典中 "k1" 对应的值为 "conan"，输出修改后的字典
dic['k1'] = 'conan'
print(dic)

# 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic['k3'].append(44)
dic.get('k3').append(44)
print(dic)

# 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
dic.get('k3').insert(0, 18)
print(dic)

