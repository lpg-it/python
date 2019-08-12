---
『Python基础』第4节：基础数据类型之字符串
---

## 一. 字符串

字符串，由任意字节的字符组成，用单引号（`'`）、双引号（`“`）或三引号（`"""`）成对表示。

简单的说，凡是用引号括起来的就是字符串。

```python
name = 'Conan'

name1 = "Conan"
```

单双引号配合使用：

```python
s = 'I am Conan'
print(s)
s = "I'm Conan"
print(s)
```

当一个字符串有多行时，一般考虑使用三引号：

```python
msg = """
床前明月光，
疑是地上霜，
举头望明月，
低头思故乡。
"""
注：只有引号，没有字节内容的字符串也是合法的。例如name = ''
```

### 2.2.1 字符串的基本操作

字符串值基本操作包括读取、合并、修改、删除、查找

#### 1. 字符串值的读取

s = 'Tom is a cat'

代码中的字符串在内存中的存放顺序如下表所示：

| s字符串：      | T    | o    | m    |      | i    | s    |      | a    |      | c    | a    | t    |
| -------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 对应下标地址： | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   |


从上表可以看出，字符串中的每个字符都对应一个下标。字符串的下标都是从0开始。

> 注：下面对字符串进行的操作，形成的都是一个新的字符串，与原来的字符串没有关系

（1）按照索引取值：[下标]。

```python
s1  = s[2]        # 读取下标为2的字符
print(s1)
结果：m
```

（2）按照切片取值：[左下标: 右下标]，顾头不顾尾。

```python
s2 = s[4:6]        # 读取下标为4，5的字符
print(s2)
结果：is
```

（3）带冒号省略下标方式切片：[左下标: ]、[: 右下标]、[ : ]。

```python
s3 = s[: 3]        # 读取下标为前三个的字符
print(s3)
结果：Tom
[: 3] 指的是从字符串的开始，读到下标为2的字符

s4 = s[9: ]        # 读取下标从第9到最后的字符
print(s4)
结果：cat

s5 = s[:]        # 读取整个字符串
print(s5)
结果：Tom is a cat
```

（4）负数下标读取：用负数下标从右到左读取对应的字符串值。

```python
s6 = s[-1]        # 从右往左，读取右边第一个字符
print(s6)
结果：t

s7 = s[-3: -1]        # 从右往左，读取倒数第三个、倒数第二个字符
print(s7)
结果：ca
```

（5）带步长的切片读取：[左下标: 右下标: 步长]。

```python
s8 = s[: : 2]         # 从头到尾，步长为2，读取对应字符
print(s8)
结果：Tmi  a

# 如果想倒序取值，加一个反向步长（步长前加负号）
s9 = s[-1:-6: -2]
print(s9)
结果：tca
注1：Python在采用下标读取其他对象值时，也统一采用类似风格的下标使用方法，如后面要讲到的列表、元组等。
注2：使用下标时，超出字符串范围读取值，解释器将报错。
```

#### 2. 字符串值合并

对于不同的字符串，可以通过加号（`+`）进行合并操作. 

> str + str

```python
name = 'Conan'
job = 'student'
res = name + ', ' + job  # 用加号合并三个字符串
print(res)  # Conan, student
```

字符串值也可以与数字相乘(`*`). 

> str * int

```python
s = '锦鲤'
s1 = s * 6  # 重复显示6个锦鲤
print(s1)  # 结果：锦鲤锦鲤锦鲤锦鲤锦鲤锦鲤
```

> 字符串中, 可以进行 `+`, `*` 操作, 不能进行 `-`, `/` 操作

#### 3. 字符串值修改

```python
replace：替换
s = 'Tom is a cat, Tom...'
s1 = s.replace('Tom', 'Jack')        # 前面为要替换的内容，后面为替换的内容
print(s1)
结果：Jack is a cat, Jack...

# 可以设置替换次数，但是只能从前往后开始替换
s2 = s.replace('Tom', 'Jack', 1)
print(s2)
结果：Jack is a cat, Tom...
```

```python
name = 'I am a student'
new_name = name[: 7] + 'teacher'
print(new_name)
结果：I am a teacher
上述字符串值的修改，是通过读取子字符串并合并的方法实现的。
不能直接对字符串做如下修改操作：
name[3] = 'i'        # 解释器将报错
```

#### 4. 字符串值删除

```python
strip：默认去除字符串前后的空格、换行符(\n)、制表符(\t)
name = '\tblame kidd '
print(name.strip())
结果：'blame kidd'        # 加引号是为了区分空格

# 也可以指定去除的字符
name = '**blame kidd*'
print(name.strip('*'))        # 去除字符串首尾的*
结果：blame kidd

name = 'iwakiddwa'
print(name.strip('wai'))
结果：kidd

去除字符串前面的空格：lstrip
去除字符串后面的空格：rstrip


# 应用举例：登录账户时
username = input('请输入用户名：').strip()
if username == 'kidd':
    print('登录成功！')
```

```python
del：删除整个字符串值
del(name)        # 清楚内存中的name，再次调用name将报错
说明：del(x)函数函数内存中一个指定的对象x，x可以是字符串、数字、列表、元组、字典、类等。
```

#### 5. 字符串值查找

```python
判断以什么为开头：startswith
print(name.startswith('bl'))        # 判断是否以bl开头
结果：True

print(name.startswith('e', 4))        # 判断第5个位置之后的字符串以什么开头
结果：True

print(name.startswith('la', 1, 5))        # 判断第2个位置到第5个位置的字符串以什么为开头
结果：True
判断以什么为结尾：endswith
与startswith用法一致
```

```python
通过元素找索引，找到第一个元素就返回索引值，没有此元素则返回-1：find
print(name.find('a'))
结果：2

print(name.find('d'))
结果：7

print(name.find('w'))
结果：-1

print(name.find('m', 1, -1))        # find可以设置查找的字符串的开始位置和结束位置
结果：3
```

```python
通过元素找索引，找到第一个元素就返回其索引值，没有此元素则报错：index
print(name.index('a'))
结果：2

print(name.index('w'))        # 没有w，报错
```

### 2.2.2 其它常用操作

#### 1. 获取字符串长度

用len函数可以获取字符串长度

```python
name = 'blame kidd'
print(len(name))
结果：10
说明：len(x)函数返回一个对象的长度，x可以是字符串、列表、元组、字典。
注：
在python3.6版本中，把一个汉字看作一个字符串长度
在python2.x版本中，把一个汉字看作两个字符串长度
```

#### 2. r/R原始字符串控制符号

```python
print('D:\back\name')        # 字符串里含特殊转移符号，\b, \n
结果：D:ack        # 没有使用r情况下，\b转为了退格符，实现了退一格的效果
ame        # \n转为了换行符，实现了其后字母的换行显示

print(r'D:\back\name')
结果：D:\back\name        # 在使用r情况下，字符串原样输出，转义字符不起作用
```

#### 3. split：将字符串分割成列表(str -- > list), 默认按照空格分割

```python
s = 'apple huawei xiaomi'
l1 = s.split()        # 默认按照空格分割
print(l1)
结果：['apple', 'huawei', 'xiaomi']

s = 'apple, huawei xiaomi'
l2 = s.split(',')
print(l2)
结果：['apple', 'huawei xiaomi']
注意这三个的区别：
s1 = ' apple huawei xiaomi'
print(s1.split())
结果：['apple', 'huawei', 'xiaomi']

s2 = ' apple huawei xiaomi'
print(s2.split(' '))
结果：['', 'apple', 'huawei', 'xiaomi']

s3 = ',apple,huawei,xiaomi'
print(s3.split(','))
结果：['', 'apple', 'huawei', 'xiaomi']
# 可以设置split的分割次数
s = 'blameliop'
print(s.split('l', 1))
结果：['b', 'lameliop]
```

#### 4. join：自定制连接符，将可迭代对象中的元素连接起来

```python
s = 'kidd'
s1 = '*'.join(s)
print(s1)
结果：k*i*d*d
```

#### 5. capitalize：首字母大写

```python
name = 'blame kidd'
print(name.capitalize())
结果：Blame kidd
```

#### 6. title：非字母隔开的每个部分的首字母大写

```python
name = 'blame kidd'
print(name.title())
结果：Blame Kidd
```

#### 7. center：字符串居中，前后填充自定义的字符

```python
name = 'blame kidd'
print(name.center(20, '*'))
结果：*****blame kidd*****
```

#### 8. upper：字符串全部大写；lower：字符串全部小写

```python
name = 'Blame Kidd'
print(name.upper())
结果：BLAME KIDD

print(name.lower())
结果：blame kidd
应用场景：验证码不区分大小写
code = 'AjkG'.lower()
your_code = input('请输入验证码：').lower()
if code == your_code:
    print('验证成功！')
```

#### 9. swapcase：大小写转换

```python
name = 'BlaMe kiDd'
print(name.swapcase())
结果：bLAmE KIdD
```

#### 10. 格式化输出：%、format

```python
# %s为格式化字符串；%d为格式化整数
name = 'blame kidd'
age = 18
print('My name is %s, My age is %d'%(name, age))
结果：My name is blame kidd, My age is 18
format有三种方式
第一种：
s1 = '我叫{}, 今年{}'.format('kidd', '18')
print(s1)
结果：我叫kidd, 今年18

第二种：
s2 = '我叫{0}, 今年{1}, 我还是叫{0}'.format('kidd', '18')
print(s2)
结果：我叫kidd, 今年18, 我还是叫kidd

第三种：
s3 = '我叫{name}, 今年{age}, 我还是叫{name}'.format(age = '18', name = 'kidd')
print(s3)
结果：我叫kidd, 今年18, 我还是叫kidd
```

#### 11. is系列

```python
name = 'kidd123'
print(name.isalpha())        # 判断name是否全部以字母组成
结果：False

print(name.isdigit())        # 判断name是否全部以数字组成
结果：False

print(name.isalnum())        # 判断name是否以字母或者数字组成
结果：True
```

#### 12. count：计数

```python
name = 'blame kidd'
print(name.count('d'))        # 计算给定字符出现几次，可以进行切片
结果：2
```

 