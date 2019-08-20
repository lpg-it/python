
# 1. 在没有()的情况下, 优先级: not > and > or
# 情况1: 两边都是比较运算
print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)
print(True or False)

# 情况2: 两边都是整数
print(1 or 2)
print(3 or 2)
print(-1 or 2)
print(0 or 2)

print(1 and 2)
print(0 and 1)
print(5 and 0)


# str --> int: 只能是纯数字
s1 = '100100'
print(int(s1))
s2 = '00100'
print(int(s2))

# int --> str  任意数字
i = 0
print(str(i), type(str(i)))


# int --> bool    非零即True, 0为False
i = 0
print(bool(i))
# bool --> int
print(int(True))
print(int(False))


# 面试题
print(1 and 2 or 3 and 4)
