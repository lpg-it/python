---
title: 『Python基础』第4节：基础数据类型初识
date: '2019-08-05 23:30'
keywords: 基础数据类型初识
description: 基础数据类型初识
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
abbrlink: 3074067626
---

本节只是对基础数据类型做个简单介绍, 详情会在之后慢慢介绍

## 什么是数据类型?

  我们人类可以分清数字与字符串的区别, 可是计算机不能. 虽然计算机很强大, 但在某种程度上又很傻, 除非你明确告诉它数字与字符串的区别.
  因此, 在每个编程语言中都有叫 `数据类型` 的东西, 其实就是对常用的数据类型进行了明确的划分. 
  Python中常用的数据类型有很多种, 本节只介绍3中: 数字、字符串、布尔类型

## 整数类型 - int

在32位机器上，整数的位数为32位，取值范围为-2**31～2**31-1，即-2147483648～2147483647

在64位系统上，整数的位数为64位，取值范围为-2**63～2**63-1，即-9223372036854775808～9223372036854775807

> 除了 `int` 之外, 还有 `float`浮点型, 复数型, 但本节暂时不讲.

## 字符串类型 - str

在python中, 被引号包起来的字符都被认为是字符串

```python
name = 'Conan'  # 单引号
age = "18"  # 双引号, 只要加引号就是字符串
age2 = 18  # int类型

msg = """My name is Conan, I am 23 years old!"""  # 3个双引号也可以, 当然, 3个单引号也是一样的

```

那么, 单引号与双引号有神马区别呢? 其实单双引号没有任何区别, 只不过在特定场景下, 需要单双引号的配合使用

```python
msg = "I am 23 years old."  # 这时用单双引号都可以.
msg = "I'm 23 years old."  # 这时外面用双引号, 里面用单引号

```

> 而多引号一般作用于多行的字符串

```python
msg = """
床前明月光,
疑是地上霜,
举头望明月,
低头思故乡.
"""
```

### 字符串的拼接

数字可以进行加减乘除运算, 而字符串也可以, 只不过字符串只能是 `相加` 或者 `相乘`.

#### 字符串 + 字符串

> 相加其实就是简单的拼接, 且只能都是字符串, 不能与数字或其他类型进行拼接

```python
name = 'Conan'
age = '23'
print(name + age)  # Conan23
```

#### 字符串 * 整数

> 相乘就是复制自己多少次, 再拼接到一起

```python
name = 'Conan'
print(name * 6) # ConanConanConanConanConanConan

```

## 布尔类型 - bool

布尔类型很简单, 只有两个值. 一个是 `True`( 真 ), 一个是 `False`( 假 ), 主要用于逻辑判断

```python
x = 3
y = 5
print(x > y)  # 不成立就是False
print(x < y)  # 成立就是True

```

