# coding:utf-8
# 工程文件:python-wsa
# 代码文件:99乘法表
# 创建时间:2022/4/4 10:02
input('回车输出九九乘法表')
for i in range(1, 10):
	for j in range(1, i + 1):
		print(i, '*', j, '=', i * j, ' ', end='')
	print()
