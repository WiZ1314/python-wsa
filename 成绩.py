# coding:utf-8
# 工程文件:python-wsa
# 代码文件:成绩
# 创建时间:2022/3/14 11:15
# 计算学生成绩
m = input("数学成绩:")
c = input("语文成绩:")
e = input("英语成绩:")
m = float(m)
c = float(c)
e = float(e)
s = m + c + e
print("总分: ", s, "平均:%5.3f" % (s/3))
