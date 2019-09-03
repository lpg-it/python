---
『Python基础』第42节 函数的嵌套
---

## 1. 函数的嵌套

​		函数的嵌套就是一个函数中, 还有函数.

​		理解函数的嵌套只需要明白一点, 只要遇见了 `函数名 + ()` 就是函数的调用, 如果没有就不是函数的调用.

下面, 我们通过一些例子来进行理解.

**例1: **

```python
def func1():
    print('in func1')
    print(3)
def func2():
    print('in func2')
    print(4)
func1()
print(1)
func2()
print(2)
# 结果:
# in func1
# 3
# 1
# in func2
# 4
# 2
```

**例2: **

```python
def func1():
    print('in func1')
    print(3)
def func2():
    print('in func2')
    func1()
    print(4)
print(1)
func2()
print(2)
# 结果
# 1
# in func2
# in func1
# 3
# 4
# 2
```

**例3: **

```python
def func1():
    print(1)
    def func2():
        print(2)
    print(3)
    func2()
    print(4)
print(5)
func1()
print(6)
# 结果
# 5
# 1
# 3
# 2
# 4
# 6
```

