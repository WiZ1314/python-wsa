# coding:utf-8
# 工程文件:python-wsa
# 代码文件:列表-元素删除方法
# 创建时间:2022/5/9 10:29
name_list=['张三', '李四', '王五', '李四']
name_list.remove('李四')
print(name_list)

name_list.pop(2)
print(name_list)

name_list.pop()
print(name_list)

del name_list[0]
print(name_list)

name_list.clear()
print(name_list)

del name_list
#print(name_list)
