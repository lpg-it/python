tu = (100, 'conan', True, [1, 2, 3])
print(tu[2], type(tu[2]))
print(tu[:3])

# 查看
for i in tu:
    print(i)


print(len(tu))

tu[-1].append(666)
print(tu)

# del tu[1]  # 不能删
# print(tu)


# 元组的拆包, 分别赋值
(a, b) = (1, 2)
print(a, b)

c = (5, 6)
a, b = c
print(a, b)
