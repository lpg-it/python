# while循环初识
# while True:
#     print('狼的诱惑')
#     print('青春')
#     print('你不要担心')


# 循环如何终止?
flag = True
while flag:
    print('狼的诱惑')
    print('青春')
    flag = False
    print('你不要担心')

# 用while循环输出1-100所有的数字
# 第一种方法
count = 1
flag = True
while flag:
    print(count)
    count += 1
    if count > 100:
        flag = False

# 第二种方法
count = 1
while count < 101:
    print(count)
    count += 1

# 用while循环计算 1 + 2 + 3 + ... + 100的结果
sum = 0
count = 1
while count < 101:
    sum += count
    count += 1
print(sum)

# 用while循环打印1 - 100所有的偶数
count = 1
while count < 101:
    if count % 2 == 0:
        print(count)
    count += 1

# break: 循环中遇到break直接退出循环
while True:
    print('狼的诱惑')
    print('青春')
    break
    print('你不要担心')
print(111)

# 用while循环打印1 - 100所有的偶数, 使用break
count = 0
while 1:
    count += 2
    print(count)
    if count >= 100:
        break

# continue: 退出 本次 循环, 继续 下一次 循环
flag = True
while flag:
    print(111)
    print(222)
    flag = False
    continue
    print(333)

# 请输出 1 2 3 4 5 95 96 97 98 99 100
count = 0
while count < 100:
    count += 1
    if 5 < count < 95:
        continue
    print(count)

# while else: while循环如果被break打断, 则不执行else语句
count = int(input('请输入一个数字: '))
while count < 5:
    print(count)
    if count == 2:
        break
    count += 1
else:
    print(666)
