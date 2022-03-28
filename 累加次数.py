# coding:utf-8
# 工程文件:python-wsa
# 代码文件:累加次数
# 创建时间:2022/3/28 10:36
y = int(input('请输入所要相加的数：'))
z = int(input("请输入所要相加的次数:"))
sum = 0
sx = 0
su_sum = 0
while sx < z:
	sum += 10 ** sx * y
	print('', sum, end='')
	su_sum += sum
	sx += 1
	
print(' =', su_sum)
