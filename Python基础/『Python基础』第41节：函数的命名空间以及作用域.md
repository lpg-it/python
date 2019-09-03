---
『Python基础』第41节 函数的命名空间以及作用域
---

## 1. 命名空间

### 1.1 命名空间介绍

​		在Python解释器开始执行之后, 就会在内存中开辟一个空间. 每当遇到一个变量的时候, 就会把变量名和值之间的关系记录下来. 

​		但是, 当遇到函数定义的时候, 解释器只是把函数名读入内存, 表示这个函数已经存在了, 至于函数内部的变量和逻辑, 解释器暂时是不关心的. 

​		也就是说, 一开始的时候函数只是加载进来而已, 只有当函数被调用的时候, 解释器才会根据函数内部声明的变量来进行开辟变量的内部空间. 随着函数执行完毕, 这些函数内部变量占用的空间也会随着函数执行完毕而被清空.

​		我们称这个**存放名字与值之间关系**的空间为**命名空间**.

​		代码在运行开始时, 创建的存储**变量名与值之间关系**的空间叫做**全局命名空间**.

​		在**函数**的运行中开辟的临时的空间叫做**局部命名空间**(临时命名空间).

​		在Python中, 还有一个空间叫做**内置命名空间**: 内置命名空间存放的就是一些内置函数等拿来即用的特殊的变量, 如 `input`, `print`这些. 

![](http://assets.processon.com/chart_image/5d6a059ce4b0f42553463875.png)

**总结一下**: 

- 内置命名空间: 存放python解释器为我们提供的
- 全局命名空间
- 局部命名空间

### 1.2 命名空间的加载顺序

​		加载顺序就是这三个空间加载到内存中的先后顺序, 也就是这三个空间在内存中创建的先后顺序.

​		首先, 在Python解释器启动之后, 即使没有创建任何的变量或者函数, 还是会有一些函数可以直接使用比如: print(), input()等. 所以肯定是**先加载内置命名空间**.

​		然后, 当py文件开始运行的时候, 从上往下一行一行的执行, 此时如果遇到了初始化变量, 就会创建全局命名空间, 将这些对应关系放进去.

​		如果遇到了**函数执行(调用)**(不是定义, 是执行)时, 在内存中开辟一个临时命名空间,加载函数中的一些变量等.

所以, 这三个空间的加载顺序为:

1. 内置命名空间: 程序运行开始加载
2. 全局命名空间: 程序运行中, 从上至下加载
3. 局部命名空间: 程序运行中, **函数调用**时才加载

### 1.3 命名空间的取值顺序

​		取值顺序就是引用一个变量, 先从哪一个空间开始引用. 这里有一个关键点: 从哪一个空间**开始引用**这个变量.

```python
# 如果在全局命名空间引用一个变量, 则先从全局命名空间引用, 全局命名空间如果没有, 会向内置命名空间引用
input = 666
print(input)  # 666

# 如果在局部命名空间引用一个变量, 先从局部命名空间引用,
# 局部命名空间如果没有, 会向全局命名空间引用,
# 全局命名空间如果没有, 会向内置命名空间引用.
input = 666
print(input)  # 666
def func():
    input = 333
    print(333)  # 333
func()
```

所以, **空间的取值顺序与加载顺序是相反的**, 取值顺序满足**就近原则**.

![](http://assets.processon.com/chart_image/5d6a0bc8e4b0fb9fe2d3e19f.png)

## 2. 作用域

作用域就是**作用范围**, 分为**全局作用域**和**局部作用域**.

- 全局作用域: 包含**内置命名空间**和**全局命名空间**. 在整个文件的任何位置都可以使用(遵循从上至下依次执行)
- 局部作用域: 包含局部命名空间. 在**函数内部**可以使用.

### 2.1 内置函数globals(), locals()

- globals(): 以字典的形式返回全局作用域中所有的变量对应关系.
- locals(): 以字典的形式返回**当前作用域**(不是局部作用域)的所有变量对应关系.

```python
# 在全局作用域下打印, 它们获取的都是全局作用域的所有内容
x = 2
y = 3
print(globals())
print(locals())
"""
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002A90F966908>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'E:/Project/Python_Road/0. 测试/1. 代码测试.py', '__cached__': None, 'x': 2, 'y': 3}

{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002A90F966908>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'E:/Project/Python_Road/0. 测试/1. 代码测试.py', '__cached__': None, 'x': 2, 'y': 3}
"""


# 在局部作用域下打印, 
# globals()获取的是全局作用域的所有内容,
# locals()获取的是局部作用域的所有内容.
x = 2
y = 3
def func():
    z = 6
	print(globals())
	print(locals())  # {'z': 6}
func()
"""
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000021CAA586908>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'E:/Project/Python_Road/0. 测试/1. 代码测试.py', '__cached__': None, 'x': 2, 'y': 3, 'func': <function func at 0x0000021CAA664BF8>}

{'z': 6}
"""
```

