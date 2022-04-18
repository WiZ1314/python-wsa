# coding:utf-8
# 工程文件:python-wsa
# 代码文件:空心方块
# 创建时间:2022/4/11 8:36
rows = 4
for i in range(rows):
	for y in range(rows):
		if y == 0 or y == rows - 1 or i == rows - 1 or i == 0:
			print('* ', end='')
		else:
			print('  ', end='')
	print('')
