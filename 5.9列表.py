# coding:utf-8
# 工程文件:python-wsa
# 代码文件:5.9列表
# 创建时间:2022/5/9 8:20
name_lines = ['张三', '李四', '王五', '王小二']
for my_name in name_lines:l
c	print('My name is %s' % my_name)
for my_names in range(len(name_lines)):
	print('My names are %s' % name_lines[my_names])

print('添加元素之前', name_lines,id(name_lines))
name_lines.append('马六')
print('添加元素后', name_lines, id(name_lines))
list2=['hello', 'liming']
name_lines.append(list2)
print('添加元素2', name_lines, id(name_lines))
name_lines.extend(list2)
print('元素3', name_lines, id(name_lines))
name_lines.insert(1,90)
print('元素4', name_lines, id(name_lines))
list3=[True,False,'hello']
name_lines[1:]=list3
print(name_lines)


