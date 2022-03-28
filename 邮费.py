# coding:utf-8
# 工程文件:python-wsa
# 代码文件:邮费
# 创建时间:2022/3/21 10:51
import math as m

mx = int(input('请输入邮件重量（g）:'))
jia = input('是否需要加急邮件:')
cx = (mx - 1000) / 500
if mx > 1000:
	yuan = 8 + m.ceil(cx) * 4
elif mx <= 1000:
	yuan = 8
if jia == 'y':
	yuan += 5
print('需要邮费: %d元' % yuan)
