# 这是单行注释
"""
这是多行注释
"""

# 输出print
print('hello 老铁')

print(1 + 2 + 3)
print((1 + 2 + 3) * 3 / 2)
print((((1 + 2 + 3) * 3 / 2) + 100) / 24)

x = 1 + 2 + 3
y = x * 3 / 2
z = (y + 100) / 24
print(x, y, z)

# x,y,z 都是变量
# 变量练习, 判断下列哪些是变量, 哪些不是变量
"""
x8 = 100  # True
b__ = 12  # True
4g = 12  # False
_ = 11  # True
*r = 12  # False
r3t4 = 10  # True
t_ = 66  # True
"""

# 变量的小高级:写出下面的输出结果
age1 = 18
age2 = age1
age3 = age2
age2 = 12
print(age1, age2, age3)  # 18 12 18


# 常量, 约定俗成不能改变
NAME = 'Conan'
print(NAME)
# NAME = 'Blame'
# print(NAME)


# 基础数据类型
# int
"""
x = 100
y = 2
z = x * y
print(z)
"""


# str
s1 = 'day1'
s2 = 'python'
s3 = """python"""
print(s1, s2, s3)

# 单双引号可以配合使用
content = 'I am Conan, 18 years old.'
print(content)
content = "I'm Conan, 18 years old."
print(content)

# 三引号: 换行的字符串
msg = """
今天我想写首诗,
歌颂我的同桌,
你看他那乌黑的短发,
好像一只炸毛鸡.
"""
print(msg)

# str可以进行 +, *. 但是不能进行-, /.
# str + str : 字符串的拼接
s1 = 'Conan'
s2 = 'Li'
print(s1 + s2)

# str * int
s1 = '学习'
print(s1 * 8)


# bool: True  False
print(2 > 1)
print(3 < 1)
print(True, type(True))
print('True', type('True'))

s1 = '100'
s2 = 100
print(s1, type(s1))
print(s2, type(s2))


# 用户交互input: 出来的都是字符串类型
# username = input('请输入用户名: ')
# password = input('请输入密码: ')
# print(username, type(username))
# print(password, type(password))

# 让用户输入姓名, 年龄, 性别, 然后打印一句话: 我叫: , 今年: , 性别:
# name = input('请输入姓名: ')
# age = input('请输入年龄: ')
# gender = input('请输入性别: ')
# print(f'我叫: {name}, 今年: {age}, 性别: {gender}')


# 流程控制语句if
# 单独 if
print(111)
if 2 < 1:
    print(222)
print(333)

# if else
s1 = '100'
x = int(s1)
print(x, type(x))

age = input('请输入年龄: ')
if int(age) > 18:
    print('恭喜你, 成年了.')
else:
    print('小屁孩儿')

# if elif elif ...  多选一
num = int(input('猜数(1 - 10): '))
if num == 1:
    print('晚上请吃饭')
elif num == 2:
    print('晚上一起溜达')
elif num == 3:
    print('晚上一起玩游戏')

# if elif elif ... else  多选一
num = int(input('猜数(1 - 10): '))
if num == 1:
    print('晚上请吃饭')
elif num == 2:
    print('晚上写代码')
elif num == 3:
    print('晚上一起溜达')
else:
    print('晚上一起玩游戏')
print('组合')

# 嵌套的if
"""
if 条件:
    if 条件:
        if 条件: 
            ...
"""
username = input('请输入用户名: ')
password = input('请输入密码: ')
code = 'df23'
your_code = input('请输入验证码: ')

if your_code == code:
    if username == 'Conan' and password == '123':
        print('登录成功')
    else:
        print('账号或密码错误')
else:
    print('验证码错误.')


score = int(input('请输入分数: '))

if score > 100:
    print('最高才100分...')
elif score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >=60:
    print('C')
elif score >= 40:
    print('D')
else:
    print('太笨了...')
