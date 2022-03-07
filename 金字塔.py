# coding:utf-8
# 工程文件:python-wsa
# 代码文件:金字塔
# 创建时间:2022/3/7 9:24
import time
a = input('请输入金字高度塔的')
b = eval(a)
for i in range(1, b + 1):
	for j in range(1, b - i + 1):
		print(' ', end=" ")
	for k in range(1, 2 * i):
		print('*', end=' ')
	time.sleep(1)
	print()
