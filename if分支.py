# coding:utf-8
# 工程文件:python-wsa
# 代码文件:if分支
# 创建时间:2022/3/21 8:32
print("******练习一*******")
age = int(input("输入年龄:"))
if 0 <= age <= 120:
	print("恭喜你还活着")
else:
	print('年龄不正确')
print('******练习二******')
python_score = int(input("输入第一门成绩"))
score = int(input('输入第二门成绩'))
if 100 > python_score > 60 or 100 > score > 60:
	print('成绩合格')
else:
	print('成绩不合格')
print('********任务三******')
is_employee = bool(int(input('员工编号')))
if not is_employee:
	print('不允许入内')
else:
	print('允许入内')
