# coding:utf-8
# 工程文件:python-wsa
# 代码文件:打印1.2.3顺序
# 创建时间:2022/4/4 10:09
input('回车开始打印')
for i in range(1, 4):
	for j in range(1, 4):
		for k in range(1, 4):
			if i != j and j != k and i != k:
				print(i, j, k)
