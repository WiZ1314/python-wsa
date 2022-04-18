# coding:utf-8
# 工程文件:python-wsa
# 代码文件:输出异常
# 创建时间:2022/4/11 9:28
try:
	Name = input("姓名:")
	if Name.strip() == "":
		raise Exception("无效的的姓名")
	Gender = input("性别:")
	if Gender != "男" and Gender != "女":
		raise Exception("无效的性别")
	Age = input("年龄:")
	Age = float(Age)
	if Age < 18 or Age > 30:
		raise Exception("无效的年龄")
	print(Name, Gender, Age)
except Exception as err:
	print(err)
