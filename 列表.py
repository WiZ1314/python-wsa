# coding:utf-8
# 工程文件:python-wsa
# 代码文件:列表
# 创建时间:2022/5/2 10:52
s1 = 'hello hello python python python'
print(s1.replace('python', 'java', 3))
print(s1.replace('python', 'java', 4))
print(id(s1))
lst = ['hello', 'world', 'python']
print('|'.join(lst))
print(' '.join(lst))
print(s1.startswith('h'))
print(s1.endswith('h'))
print('-----------------')
a = 'hello'
b = 'world'
c = 'hello world'
print(a.upper())
print(id(a))
print(id(a.upper()))
print(b.lower())
print(c.title())
print(c.capitalize())
print(c.swapcase())
print(c.rjust(20, '*'))
print(c.center(20, '*'))
print(c.ljust(20, '&'))
print('*************')
leib = ['hello', 'world', 'python']
for i in range(len(leib)):
	print(leib[i])
print('///')
for st in leib:
	print(st)
print('//////')
