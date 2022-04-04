# coding:utf-8
# 工程文件:python-wsa
# 代码文件:质数
# 创建时间:2022/4/4 8:14
c = 0
for n in range(2, 101):
	x = 1
	for m in range(2, n):
		if n % m == 0:
			x = 0
			break
	if x == 1:
		print('% 5d' % n, end="")
		c += 1
		if c % 5 == 0:
			print()
