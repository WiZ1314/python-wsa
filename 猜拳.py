# coding:utf-8
# 工程文件:python-wsa
# 代码文件:猜拳
# 创建时间:2022/3/28 9:10
import random

com = random.randint(1, 3)
ren = int(input('请输入剪刀(2)石头(1)布(3):'))
print('电脑出拳结果为%d--玩家出拳结果为%d' % (com, ren))
if (ren == 1 and com == 2) or (com == 1 and ren == 3) or (com == 3 and ren == 2):
	print('恭喜玩家获胜')
elif ren == com:
	print('平局')
else:
	print('电脑获胜')
