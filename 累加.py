# coding:utf-8
# 工程文件:python-wsa
# 代码文件:累加
# 创建时间:2022/3/28 10:27
x = int(input('输入累加次数'))
i = 0
n = 0
while i <= x:
	n += i
	i += 1
print("累加结果为 %d" % n)
