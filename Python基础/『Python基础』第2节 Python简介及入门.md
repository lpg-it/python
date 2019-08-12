---
title: 『Python基础』第2节 Python简介及入门
---

# 一. Python介绍

​        Python是一门高级计算机程序设计语言，1989年，荷兰的Guido von Rossum创造了它。Guido是是一个牛人，1982年，他从阿姆斯特丹大学获得了数学和计算机硕士学位，因此他可以算是一位数学家，不过他更享受使用计算机解决问题的感觉。Python只是由Guido的一次hacking产生的，1989年圣诞节假期，早就萌发了设计一门好用的高级语言的想法的Guido，放弃了休息，全身心的投入到了设计新语言的活动中去，结果产生了世界上少有的几门最优美、最易用、最简洁的高级程序设计语言之一——Python语言。

[最新的TIOBE排行榜: Python继续在TIOBE指数中飙升](https://www.tiobe.com/tiobe-index/)

​       Python不断上升的受欢迎程度是以其他编程语言的普及程度下降为代价的。其中一种编程语言是R，但Perl已经被打败了。 Perl目前处于TIOBE指数的第19位，这是Perl的历史最低点。请注意，Perl在2005年排名第3，评级超过10％。 Perl的非常规语法及其不明确的未来（Perl 5与Perl 6）对语言造成了很大的伤害。 Perl 6本月进入了排名第93位的前100名，但这可能为时已晚，无法再次成为主要参与者。

​       TIOBE编程社区索引是编程语言普及的一个指标。 索引每月更新一次。 评级基于全球技术工程师，课程和第三方供应商的数量。 流行的搜索引擎，如谷歌，必应，雅虎，维基百科，亚马逊，YouTube和百度，用于计算评级。 值得注意的是，TIOBE索引与最佳编程语言或编写大多数代码行的语言无关。

![TIOBE排行榜](C:\Users\Administrator\Desktop\YxLtN7FwhXrIpcv.png)

# 二. 目前Python的主要领域

1. WEB开发——最火的Python web框架Django, 支持异步高并发的Tornado框架，短小精悍的flask,bottle, Django官方的标语把Django定义为the framework for perfectionist with deadlines(大意是一个为完全主义者开发的高效率web框架)

2. 网络编程——支持高并发的Twisted网络框架， py3引入的asyncio使异步编程变的非常简单

3. 爬虫——爬虫领域，Python几乎是霸主地位，Scrapy\Request\BeautifuSoap\urllib等，想爬啥就爬啥

4. 云计算——目前最火最知名的云计算框架就是OpenStack,Python现在的火，很大一部分就是因为云计算

5. 人工智能——谁会成为AI 和大数据时代的第一开发语言？这本已是一个不需要争论的问题。如果说三年前，Matlab、Scala、R、Java 和 Python还各有机会，局面尚且不清楚，那么三年之后，趋势已经非常明确了，特别是前两天 Facebook 开源了 PyTorch 之后，Python 作为 AI 时代头牌语言的位置基本确立，未来的悬念仅仅是谁能坐稳第二把交椅。

6. 自动化运维——问问中国的每个运维人员，运维人员必须会的语言是什么？10个人相信会给你一个相同的答案，它的名字叫Python

7. 金融分析——我个人之前在金融行业，10年的时候，我们公司写的好多分析程序、高频交易软件就是用的Python,到目前,Python是金融分析、量化交易领域里用的最多的语言

8. 科学运算—— 你知道么,97年开始，NASA就在大量使用Python在进行各种复杂的科学运算，随着NumPy, SciPy, Matplotlib, Enthought librarys等众多程序库的开发，使的Python越来越适合于做科学计算、绘制高质量的2D和3D图像。和科学计算领域最流行的商业软件Matlab相比，Python是一门通用的程序设计语言，比Matlab所采用的脚本语言的应用范围更广泛

9. 游戏开发——在网络游戏开发中Python也有很多应用。相比Lua or C++,Python 比 Lua 有更高阶的抽象能力，可以用更少的代码描述游戏业务逻辑，与 Lua 相比，Python 更适合作为一种 Host 语言，即程序的入口点是在 Python 那一端会比较好，然后用 C/C++ 在非常必要的时候写一些扩展。Python 非常适合编写 1 万行以上的项目，而且能够很好地把网游项目的规模控制在 10 万行代码以内。另外据我所知，知名的游戏<文明> 就是用Python写的

# 三. Python在一些公司的应用

- 谷歌：Google App Engine 、code.google.com 、Google earth 、谷歌爬虫、Google广告等项目都在大量使用Python开发
- CIA: 美国中情局网站就是用Python开发的
- NASA: 美国航天局(NASA)大量使用Python进行数据分析和运算
- YouTube:世界上最大的视频网站YouTube就是用Python开发的
- Dropbox:美国最大的在线云存储网站，全部用Python实现，每天网站处理10亿个文件的上传和下载
- Instagram:美国最大的图片分享社交网站，每天超过3千万张照片被分享，全部用python开发
- Facebook:大量的基础库均通过Python实现的
- Redhat: 世界上最流行的Linux发行版本中的yum包管理工具就是用python开发的
- 豆瓣: 公司几乎所有的业务均是通过Python开发的
- 知乎: 国内最大的问答社区，通过Python开发(国外Quora)
- 春雨医生：国内知名的在线医疗网站是用Python开发的
- 除上面之外，还有搜狐、金山、腾讯、盛大、网易、百度、阿里、淘宝 、土豆、新浪、果壳等公司都在使用Python完成各种各样的任务。

# 四. Python的发展史

​       1989年，Guido开始写Python语言的编译器。

　　1991年，第一个Python编译器诞生。它是用C语言实现的，并能够调用C语言的库文件。从一出生，Python已经具有了：类，函数，异常处理，包含表和词典在内的核心数据类型，以及模块为基础的拓展系统。

　　Granddaddy of Python web frameworks, Zope 1 was released in 1999

　　Python 1.0 - January 1994 增加了 lambda, map, filter and reduce.

　　Python 2.0 - October 16, 2000，加入了内存回收机制，构成了现在Python语言框架的基础

　　Python 2.4 - Nov. 30, 2004, 同年目前最流行的WEB框架Django 诞生

　　Python 2.5 - Sept. 19, 2006

　　Python 2.6 - Oct. 2, 2008

　　Python 2.7 - July 3, 2010

　　Python 3.0 - December 3, 2008 (这里要解释清楚 为什么08年就出3.0，2010年反而又推出了2.7？是因为3.0不向下兼容2.0，导致大家都拒绝升级3.0，无奈官方只能推出2.7过渡版本)

　　Python 3.1 - June 26, 2009

　　Python 3.2 - Feb. 20, 2011

　　Python 3.3 - Sept. 29, 2012

　　Python 3.4 - March 17, 2014

​       2014年11月，宣布Python 2.7将在2020年之前得到支持，并重申将不会发布2.8版本

　　Python 3.5 - Sept. 13, 2015

　　Python 3.6 - Dec. 23, 2016

​       Python 3.7 - June 27, 2018

# 五. Python的种类

Cpython

Ipython

PyPy

Jpython

IronPython


