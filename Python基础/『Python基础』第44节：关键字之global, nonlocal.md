---
『Python基础』第44节 关键字之global, nonlocal
---

## 1. 关键字: global

​		在讲这个关键字之前, 大家先看一段代码:

```python
li = [1, 2, 3]
def func():
    li.append(666)
    print(li)
func()  # [1, 2, 3, 666]

count = 0
def func():
    count += 1  # 报错
func()

# 报错结果: UnboundLocalError: local variable 'count' referenced before assignment
```

​		局部作用域对全局作用域的变量(此变量只能是不可变的数据类型)只能进行引用, 而不能改变, 只要改变就会报错. 

​		但是有时候, 我们程序中会遇到局部作用域去改变全局作用域中一些变量的需求, 这要怎么做呢?

​		这就得用到关键字`global`.

### 1.1 声明一个全局变量

​		利用 `global` 可以在**局部作用域**中声明一个**全局变量**.

```python
def func():
    global count
    count = 6
func()
print(count)  # 6
```

注意: 

> 在局部作用域利用global声明的全局变量, 在局部作用域中是没有的.

### 1.2 修改全局变量


​		`global` 其中一个功能就是: 在**局部作用域**中, 可以更改**全局作用域**的变量.

```python
count = 0
def func():
    global count
    count += 1
    print(count)
func()  # 1
```



综上所述, `global` 关键字有两个作用: 

- 声明一个全局变量
- 在局部作用域想要对全局作用域的全局变量进行修改时, 需要用到 `global`(仅限**字符串**, **数字**)

## 2. 关键字: nonlocal

​		`nonlocal` 与 `global` 的用法差不多. 

​		当我们在**局部作用域**想要对**父级作用域**(不是**全局作用域**)的变量进行改变时, 需要用到 `nonlocal`.



```python
def func():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(count)
        print(locals())
    inner()
    print(locals())
func()
```



`nonlocal` 总结:

- 不能更改全局变量
- 在局部作用域中, 对父级作用域(或者更外层作用域非全局作用域)的变量进行引用和修改, 并且引用的哪层, 从那层以及以下, 此变量全部发生改变.

