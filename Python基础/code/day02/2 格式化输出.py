# 格式化输出有三种, 这次只说第一种

# 假如要制作一个公共的模板, 让一个字符串的某些位置编程动态可传入的
"""
------------    info of Conan    ------------
name: Conan
age: 18
gender:male
job: student
-----------------    end    ------------------
"""
name = input('请输入你的名字: ')
age = input('请输入你的年龄: ')
gender = input('请输入你的性别: ')
job = input('请输入你的工作: ')
msg = """
------------    info of %s    ------------
name: %s
age: %s
gender: %s
job: %s
-----------------    end    ------------------
""" % (name, name, age, gender, job)
print(msg)


# 注意: 在格式化输出中, 如果只想表示一个 百分号(%), 而不是作为占位符使用, 应该使用连续的两个%%
msg = '我叫%s, 今年%s了, 学习进度2%%' % ('Conan', '18')
print(msg)
