# coding:utf-8
# 工程文件:python-wsa
# 代码文件:if嵌套
# 创建时间:2022/3/21 10:17
has_ticket = bool(int(input('是否有车票(1=True，0=False):')))
if has_ticket:
	knife_length = int(input("输入刀的长度:"))
	if knife_length > 20:
		print('刀具长度为%dcm危险器械不允许上车' % knife_length)
	else:
		print('允许上车')
else:
	print('没有车票，不允许上车')
