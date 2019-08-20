---
title: 『Python基础』第8节：格式化输出
date: '2019-08-12 23:34'
keywords: 格式化输出
description: 格式化输出
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
abbrlink: 122518175
---

现在有一个需求, 询问用户的姓名, 年龄, 工作, 爱好, 然后打印成以下格式

```python
************  info of Conan  ************
name: Conan
age: 23
job: student
hobbies: code
*****************  end  *****************
```

  在没学格式化输出之前, 你会怎么实现呢? 你会发现, 如果直接用字符串拼接的方式去实现, 这也太麻烦了吧...

  所以, 今天就学一下格式化输出的用法.

  你会发现这一大堆字符串只有很少一部分是变化的, 其余部分都是一个样子. 所以我们可以先在那些需要变化的内容下放一个占位符, 然后通过把字符串里的占位符与外部变量做一个映射关系就可以了. 

  具体如下所示

```python
name = input('name: ')
age = input('age: ')
job = input('job: ')
hobbies = input('hobbies: ')

# 下面的每一个%s都是一个占位符
info = """
************  info of %s  ************  # 代表 后面括号里的name
name: %s  # 代表 后面括号里的name
age: %s  # 代表 后面括号里的age
job: %s  # 代表 后面括号里的job
hobbies: %s  # 代表 后面括号里的hobbies
*****************  end  *****************
""" % (name, name, age, job, hobbies)  # 这行的 % 就是把前面的字符串与括号后面的变量关联起来

print(info)
```

  %s 就是代表字符串占位符, 除此之外, 还有%d(数字占位符). 

  如果把上面的age后面的%s 换成%d, 就代表必须是数字.

假如现在又有一个需求, 需要按照下列格式打印

```python
我是 Conan, 年龄 18, 目前学习进度为1%.
```

如果这样写, 程序会报错:

```python
name = input('name: ')
age = int(input('age: '))

msg = "我是%s, 年龄%d, 目前学习进度为1%." % (name, age)

print(msg)
```

  报错原因: 在格式化输出中, 只要出现 % 就认为是占位符的 % , 但是如果想向上面那样, 1%就是表示1%, 而不是占位符, 应该按照下面的方法: 

```python
name = input('name: ')
age = int(input('age: '))

msg = "我是%s, 年龄%d, 目前学习进度为1%%." % (name, age)

print(msg)
```

  我们注意到, 当我们真的只是想表达一个%的时候, 只需要写两个%就可以了, 第一个%是对第二个%的转义, 是告诉Python解释器这只是一个单纯的%, 而不是占位符.


