# coding:utf-8
# 工程文件:python-wsa
# 代码文件:打印等边三角形
# 创建时间:2022/4/18 9:05
def prin_triangle(m):
	for i in range(m):
		for j in range(m - 1 - i):
			print(" ", end='')
		for j in range(i + 1):
			print("* ", end='')
		print()


n = int(input('请输入'))
prin_triangle(n)
