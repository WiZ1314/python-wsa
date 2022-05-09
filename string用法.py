# coding:utf-8
# 工程文件:python-wsa
# 代码文件:string用法
# 创建时间:2022/5/2 10:24
s1 = 'hello hello python python'
s2 = 'hellohellopythonpython'
print(s1.isalpha())
print(s2.isalpha())
s3 = '12345678'
print(s3.isdigit())
print(s3.isnumeric())
s4 = 'hhhh1111'
print(s4.isalnum())
print(s4.split())
s5 = 'hello|hello|python|python'
print(s5.split())
print(s5.split('|'))
print(s5.split('|', maxsplit=1))
print(s5.rsplit())
print(s5.rsplit('|'))
print(s5.rsplit('|', maxsplit=1))























