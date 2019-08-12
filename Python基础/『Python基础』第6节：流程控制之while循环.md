---
『Python基础』第6节：流程控制之while循环
---

在生活中经常遇到循环的事情, 比如循环列表播放歌曲等. 在Python中, 也有循环, 就是其流程控制语句while.

## 1. 基本循环

```python
while 条件:
    循环体

# 如果条件为真, 那么就执行循环体
# 如果条件为假, 那么就不执行循环体.
```

举个例子: 

```python
while True:
    print('你不要担心')
    print('青春')
    print('有一天')
```

上面的代码有一个问题就是: 没有停止的时候. 只要电脑不死机, 就会一直循环下去. 那么具体的它是怎么执行的呢? 看下面这张图.

![](https://i.loli.net/2019/08/08/Mw7ZP8EadJLesOr.png)

那么应该如何终止循环呢?

## 2.  终止循环

### 2.1 改变条件

第一种终止循环的方式就是改变条件.

> 利用标志位改变条件

```python
flag = True
while flag:
    print('你不要担心')
    print('青春')
    flag = False
    print('有一天')
```


### 2.2 关键字break

在循环中, 只要遇到 `break` 马上退出循环.

```python
flag = True
while flag:
    print('你不要担心')
    print('青春')
    break
    print('有一天')
```

### 2.3 调用系统命令

`quit()`, `exit()`, 后面会讲到, 在这里不再讲解, 不推荐使用.

### 2.4 关键字continue (终止本次循环)

`continue` 用于终止本次循环, 然后继续下一次的循环.

```python
flag = True
while flag:
    print('你不要担心')
    print('青春')
    continue
    print('有一天')
```



## 2. while ... else ...

`while` 后面的 `else` 的作用是: 当while循环正常执行完, 中间没有被 `break` 终止的话, 就会执行else后面的语句; 如果被break终止, 则不会执行else后面的语句.

```python
count = 0
while count < 5:
    count += 1
    print(count)
else:
    print('循环正常执行完, 没有被break打断.')
```

如果执行过程中被break终止, 就不会执行else后面的语句

```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        break
    print(count)
else:
    print('这里的循环不会执行.')
```



## 练习

### 练习1 利用while输出1-100所有的数字

```python
count = 1
while count < 101:
    print(count)
    count += 1
```

### 练习2 使用while循环求出1-100所有数的和

```python
sum = 0
count = 1
while count < 101:
    sum += count
    count += 1
print(sum)
```

### 练习3 打印1-100所有的偶数

```python
count = 1
while count < 101:
    if count % 2 == 0:
        print(count)
    count += 1
```

### 练习4 使用while循环打印 1 2 3 4 5 6 8 9 10

```python
count = 0
while count < 10:
    count += 1
    if count == 7:
        continue
    print(count)
```

### 练习5 请输出 1 2 3 4 5 95 96 97 98 99 100

```python
count = 0
while count < 100:
    count += 1
    if 5 < count < 95:
        continue
    print(count)
```






