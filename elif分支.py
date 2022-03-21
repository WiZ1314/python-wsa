# coding:utf-8
# 工程文件:python-wsa
# 代码文件:elif分支
# 创建时间:2022/3/21 9:58
a = int(input("输入成绩:"))
if 100 >= a >= 90:
	print("成绩为A")
elif 89 >= a >= 80:
	print('成绩为B')
elif 79 >= a >= 70:
	print('成绩为C')
elif 69 >= a >= 60:
	print('成绩为D')
else:
	print('成绩为E')
