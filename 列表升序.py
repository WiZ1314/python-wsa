# coding:utf-8
# 工程文件:python-wsa
# 代码文件:列表升序
# 创建时间:2022/5/9 10:49
lst = [4, 5, 6, 55, 67, 34, 4, 5, 23, 45, 678, 342]
print(len(lst))
print(lst.count(4))

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)
lst.sort(reverse=False)
print(lst)

lst.reverse()
print(lst)

lst = ['hello', 'world', '77', 'hello']
print(lst.index('hello'))
print(lst.index('hello', 1, 4))
lst[3] = 'python'
print(lst)
print(lst[-3])

print('/////-1-/////')
ls = [5, 3, 8, 19, 11]
ls.sort(reverse=False)
print(ls)
ls.sort(reverse=True)
print(ls)
print('/////-2-////')
ls = [5, 3, 8, 11, 4]
ls.reverse()
print(ls)
print('/////-3-////')
ls1 = [4, 5, 2, 7]
ls2 = [3, 6]
ls = ls1 + ls2
ls.sort(reverse=True)
print(ls)
print('/////-4-////')
ls4 = [1, 2, 5, 2, 9, 1, 3, 2, 1, 1]
print(list(set(ls4)))
