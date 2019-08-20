---
title: 『Python基础』第5节：条件控制
date: '2019-08-05 22:30'
keywords: 条件控制
description: 条件控制
categories: Python全栈之路
tags:
  - Python基础
avatar: 'https://wx1.sinaimg.cn/large/006bYVyvgy1ftand2qurdj303c03cdfv.jpg'
photos: >-
  https://static.2heng.xin/wp-content/uploads//2019/02/wallhaven-672007-1-1024x576.png
author: 李培冠
authorLink: https://lipeiguan.top
authorAbout: 一个好奇的人
authorDesc: 一个好奇的人
comments: true
abbrlink: 1805276075
---

## `if` 语句的使用

### 单分支

```python
if 条件:
    满足条件后要执行的代码

```

例如: 

```python
if 2 < 3:
    print(222)
print(333)

```

> 每个条件后面都要使用冒号 `:`, 表示接下来是满足条件后要执行的语句块
> 在Python中没有 `switch - case`  语句

### 双分支

```python
if 条件:
    满足条件要执行的代码
else:
    不满足条件就执行这里的代码

```

例如: 

```python
age = 18
if age >= 18:
    print('恭喜你, 成年了')
else:
    print('小屁孩儿')

```

> 缩进
> 你会发现, 在上面的代码中, 每个条件的下一行都缩进了4个空格. 这是python的特色.
> C/C++等语言利用花括号来构造代码块, 而python使用缩进的方式构造代码块.
> Python缩进有几个原则:
>     顶级代码必须顶行写. 即如果一行代码不依赖任何条件, 则不需要进行缩进
>     同一级别的代码, 缩进必须一致
>     官方建议缩进用4个空格. 

回到 `if` 中来, 条件控制也可以有多个分支条件

### if elif elif ...

```python
if 条件:
    满足条件要执行的代码
elif 条件:
    上面的条件不满足就执行这个代码
elif 条件:
    上面的条件不满足就执行这个代码
...

```

例如: 

```python
num = int(input('请输入一个数字: '))
if num == 1:
    print('晚上一起吃饭')
elif num == 2:
    print('晚上一起溜达')
elif num == 3:
    print('晚上一起玩游戏')

```

### if elif elif ... else

```python
if 条件:
    满足条件要执行的代码
elif 条件:
    上面的条件不满足就执行这个代码
elif 条件:
    上面的条件不满足就执行这个代码
else:
    上面所有的条件不满足就执行这个代码

```

例如: 

```python
num = int(input('请输入一个数字: '))
if num == 1:
    print('晚上一起吃饭')
elif num == 2:
    print('晚上一起代码')
elif num == 3:
    print('晚上一起溜达')
else:
    print('晚上一起玩游戏')

```

下面是 `if` 中常用的操作运算符: 

| 操作符 | 描述                     |
| ------ | ------------------------ |
| <      | 小于                     |
| <=     | 小于或等于               |
| >      | 大于                     |
| >=     | 大于或等于               |
| ==     | 等于, 比较两个值是否相等 |
| !=     | 不等于                   |

### 嵌套if

```python

if 条件:
    if 条件:
        if 条件: 
            ...
        else:
            ...

```

例如: 

```python
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

```

## 练习

### 练习1  利用if语句写出猜大小的游戏

```python
"""
设定一个理想数字比如: 66, 让用户输入数字, 如果比66大, 则显示猜的结果大了; 如果比66小, 则显示猜的结果小了; 只有等于66, 则显示猜的结果正确.
"""

num = int(input('请输入一个数字: '))
if num > 66:
    print('结果大了')
elif num < 66:
    print('结果小了')
elif num == 66:
    print('结果正确')

```

### 练习2  提示用户输入他的年龄, 程序进行判断.

```python
"""
如果小于10,提示小屁孩; 如果大于10,小于20, 提示青春期叛逆的小屁孩; 如果大于20,小于30.提示开始定性,开始混社会的小屁孩; 如果大于30,小于40提示看老大不小了，赶紧结婚小屁孩; 如果大于40, 小于50.提示家里有个不听话的小屁孩; 如果大于50.小于60.提示自己马上变成不听话的老屁孩; 如果大于60,小于70.提示活着还不错的老屁孩; 如果大于70,小于90.提示人生就快结束了的一个老屁孩; 如果大于90以上提示.再现了这个世界。
"""

age = int(input('请输入年龄: '))
if age < 10:
    print('小屁孩')
elif age < 20:
    print('青春期叛逆的小屁孩')
elif age < 30:
    print('开始定性, 开始混社会的小屁孩')
elif age < 40:
    print('老大不小了, 赶紧结婚小屁孩')
elif age< 50:
    print('家里有个不听话的小屁孩')
elif age < 60:
    print('自己马上变成不听胡的老屁孩')
elif age < 70:
    print('或者还不错的老屁孩')
elif age < 90:
    print('人生就快结束了的一个老屁孩')
elif age > 90:
    print('再见了这个世界')

```

### 练习3  百分制成绩转等级制

```python
"""
用户输入一个分数, 根据分数来判断用户考试成绩的档次.
>=90    A
>=80    B
>=70    C
>=60    D
<60    不及格
"""

score = int(input('请输入你的分数: '))
if score >= 90:
    print('A')
elif score >=80:
    print('B')
elif score >=70:
    print('C')
elif score >=60:
    print('D')
elif score < 60:
    print('不及格')

```

> 这里有个问题, 就是当用户输入97的时候, 它打印的结果为 `A`, 但是95明明也大于80呀, 为什么不打印呢?
> 这是因为代码是从上到下依次判断, 只要满足一个, 就不会继续往下走了, 这一点要清楚.


### 练习4

```python
"""
提示用户输入麻花藤, 判断用户输入的对不对. 如果对, 提示真聪明; 如果不对, 提示输入有误
"""

s = input('请输入麻花藤: ')
if s == '麻花藤':
    print('真聪明')
else:
    print('输入有误')

```

### 练习5

```python
"""
判断输入的边长能否构成三角形, 如果可以则计算出三角形的周长.
"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print(a + b + c)
else:
    print('a, b, c不能构成三角形')

```



