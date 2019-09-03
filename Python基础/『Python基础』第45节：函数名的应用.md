---
『Python基础』第45节 函数名的应用
---

## 1. 函数名的应用

​		函数名的定义和变量几乎一致.

​		在变量的角度, 函数名其实就是一个变量, 具有变量的功能: 可以赋值. 但是作为函数名它也有特殊的功能就是加上 `()` 就会执行对应的函数, 所以我们可以把函数名当做一个特殊的变量.

​		那么接下来, 我们就来研究一下这个特殊的变量

### 1.1 函数的内存地址

```python0
def func():
    print(666)
print(func)  # <function func at 0x0000028B925A1B70>
```

​		通过上面的代码我们可以知道, 函数名指向的是这个函数的内存地址. 

​		所以, 当我们运行 `函数名()` 时, 其实就是执行的 `函数的内存地址()` , 就相当于: 

```python
a = 11
b = 22
c = a + b
print(c)  # 33
```

在上面的代码中, `a + b` 并不是两个变量的相加, 而是这两个变量指向的 **int对象** 的相加.

### 1.2 函数名可以赋值给其他变量

```python
def func():
    print(666)
f = func  # 把函数当成一个变量赋值给另一个变量
f()  # 666
```

通过变量的赋值, 变量 `f` 和变量 `func` 都指向这个函数的内存地址, 所以 `f()` 可以执行这个函数

### 1.3 函数名可以当做容器类的元素

​		从上面我们可以知道, 函数名其实就是一个变量, 那么变量当然可以当做容器类类型的元素的.

```python
def func1():
    print('in func1')
def func2():
    print('in func2')
def func3():
    print('in func3')
li = [func1, func2, func3]
for i in li:
    i()
# in func1
# in func2
# in func3
```

### 1.4 函数名可以当做函数的参数

```python
def func1():
    print('in func1')
def func2(f):
    print('in func2')
    f()
func2(func1)
# in func2
# in func1
```

### 1.5 函数名可以作为函数的返回值

```python
def func1():
    print('in func1')
def func2(f):
    print('in func2')
    return f
ret = func2(func1)
ret()  # 此时, ret, f func1 都是指向 func1 这个函数的内存地址
# in func2
# in func1
```

