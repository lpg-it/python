---
title: 『Python基础』第1节 Windows环境下安装Python3.x
date: 2019-06-27 22:31:45
keywords: Windows环境下安装Python3.x
description: Windows环境下安装Python3.x
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
abbrlink: 2270923467
---

# 一. Python安装

## 1. 下载安装包

```python
https://www.python.org/downloads/release/python-374/  # 3.7安装包
# 如需安装python2.7版本可以到这里下载
https://www.python.org/downloads/release/python-2716/  # 2.7安装包
```

## 2. 安装Python3.7

增加环境变量, 选择 `Customize installation`, 剩下的一直下一步就好.

![](https://i.loli.net/2019/08/08/SiGIog71fzuatWp.png)


## 3. 在命令行测试

打开 `cmd`, 输入 `python`.


# 二. pip安装

```
# 在CMD上执行
python3 -m pip install --upgrade pip --force-reinstall
python2 -m pip install --upgrade pip --force-reinstall

# 查看pip版本
pip3 -V
pip2 -V
```

 