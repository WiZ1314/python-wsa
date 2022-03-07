# coding:utf-8
# 工程文件:python-wsa
# 代码文件:收银
# 创建时间:2022/3/7 11:00
a = eval(input('输入商品个数'))
for i in range(1, a + 1):
	xi = float(input('输入商品金额'))
p = 0
for i in range(1, a + 1):
	p = xi + p
print('合计价格%-5.2f' % p)
