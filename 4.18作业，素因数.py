# coding:utf-8
# 工程文件:python-wsa
# 代码文件:4.18作业，素因数
# 创建时间:2022/4/18 11:25
"""
def IsPrime(m):
	for n in range(2, m):
		if m % n == 0:
			return 0
	return 1

'''
n = input("n=")
n = int(n)
for p in range(1, n + 1):
	if n % p == 0 and IsPrime(p) == 1:
		print(p)
'''
def xz(m):
	s = 0
	for i in range(1, m + 1):
		s += i
	return s


def zzzz(n):
	s = 0
	for m in range(1, n + 1):
		s += xz(m)
	return s


x = input('请输入')
x = int(x)
print(zzzz(x))

"""