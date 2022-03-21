# coding:utf-8
# 工程文件:python-wsa
# 代码文件:邮费
# 创建时间:2022/3/21 10:51
mx = int(input('请输入邮件重量（g）:'))
jia = bool(int(input('是否需要加急邮件(1=True，0=False):')))
if mx > 1000:
	if ((mx - 1000) % 500) == 0:
		yuan = 8 + (int((mx - 1000) / 500)) * 4
	else:
		yuan = 8 + (int((mx - 1000) / 500)+1) * 4
elif mx <= 1000:
	yuan = 8
if jia:
	yuan += 5
print('需要邮费: %d元' % yuan)
