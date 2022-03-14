# coding:utf-8
# 工程文件:python-wsa
# 代码文件:p15
# 创建时间:2022/3/14 10:28
# 任务一
print('------------任务一------------')
n = int(input('输入整数'))
if n % 2 != 0:
	print('奇数')
else:
	if n % 2 == 0:
		print('偶数')
	else:
		print('非奇非偶')
# 任务二
print('------------任务二------------')
nian = int(input('输入年份'))
if ((nian % 4 == 0) and (nian % 100 != 0)) or (nian % 400 == 0):
	print('%d是闰年' % nian)
else:
	print('%d不是闰年' % nian)
# 任务三
print('------------任务三------------')
word = input("请输入字母：")
len(word)
if word < 'A' or word > 'Z':
	print("大写！")
else:
	print('小写')
