# 列表的创建
# 方式一
l1 = [1, 2, 'conan']
print(l1)

# 方式二
"""
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
"""
l2 = list()
print(l2)  # []

l3 = list('conan')
print(l3)  # ['c', 'o', 'n', 'a', 'n']

# 方式三: 列表推导式 - 后面讲


# 列表的增删改查, 与字符串不同, 列表的所有操作都是在列表的基础上进行操作, 直接改变原列表
# 增
# append: 在列表最后追加
li = ['conan', 'jimmy', 'rachel', '小五郎']
li.append('阿笠博士')
print(li)
# print(li.append('阿笠博士'))

# 举例
# while 1:
#     name = input('请输入新演员(按Q或者q退出): ')
#     if name.upper() == 'Q':
#         break
#     li.append(name)
# print(li)


# insert: 任意位置插入
li = ['conan', 'jimmy', 'rachel', '小五郎']
li.insert(2, '阿笠博士')
print(li)


# extend: 迭代追加
li.extend('阿笠博士')
print(li)
li.extend([1, 2, '阿笠博士'])
print(li)


# 删
# pop: 按照索引删除, 如果索引不存在, 报错
li = ['conan', 'jimmy', 'rachel', '小五郎']
li.pop()  # 不指定索引值, 默认删除最后一个
print(li)

li.pop(1)
print(li)
# li.pop(88)  # IndexError: pop index out of range
# print(li)


# remove: 按照元素删除, 如果有相同元素, 则默认删除从左数第一个
li = ['conan', 'jimmy', 'rachel', '小五郎', 'conan']
li.remove('conan')
print(li)


# clear: 清空列表中所有元素
li = ['conan', 'jimmy', 'rachel', '小五郎']
li.clear()
print(li)


# del
li = ['conan', 'jimmy', 'rachel', '小五郎', 'conan']
# 按照索引删除
del li[2]
print(li)

# 按照切片删除
del li[:2]
print(li)

# 删除这个列表
del li


# 改
# 按照索引改
li = ['conan', 'jimmy', 'rachel', '小五郎']
li[1] = '阿笠博士'
print(li)

# 按照切片改
li = ['conan', 'jimmy', 'rachel', '小五郎']
li[:3] = 'qwerasdf'
print(li)

# 按照切片+步长 改, 要修改的元素数量必须一致
li = ['conan', 'jimmy', 'rachel', '小五郎']
li[::2] = 'qw'
print(li)


# 查
# 按照索引查
li = ['conan', 'jimmy', 'rachel', '小五郎']
print(li[2])

# 按照切片查
li = ['conan', 'jimmy', 'rachel', '小五郎']
print(li[::2])

# for循环
li = ['conan', 'jimmy', 'rachel', '小五郎']
for i in li:
    print(i)

