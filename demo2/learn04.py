if __name__ == '__main__':
    pass
# #递归函数
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(5))
# #尾递归优化
# def fact(n):
#     return fact_iter(n,1)
# def fact_iter(num,product):
#     if num==1:
#         return product
#     return fact_iter(num-1,num*product)
# print(fact(6))
# 汉若塔问题
# def move(n, a, b, c):
#     if n == 1:
#         print(a, '->', c)
#     else:
#         move(n - 1, a, c, b)
#         move(1, a, b, c)
#         move(n - 1, b, a, c)
#
#
# move(6, 'a', 'b', 'c')
# 高阶函数
# def add(x,y,f):
#     return f(x)+f(y)
# print(add(-3,-3,abs))

# map()函数接收两个参数，一个是函数，一个是Iterable（可迭代对象）(列表，元组，字典，字符串,集合)
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。map()传入的第一个参数是f，即函数对象本身。
# 由于结果r是一个Iterator（迭代器），Iterator是惰性序列...因此通过list()函数让它把整个序列都计算出来并返回一个list。
# def f(x):
#     return x * x
#
#
# print(list(map(f, [1, 2, 3, 4, 5, 6])))
# print(list(map(str, [1, 2, 4, 5, 6, 8])))
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# from functools import reduce

# 求和
# def add(x, y):
#     return x + y


# print(reduce(add, [1, 2, 3, 4, 5, 6]))

# 化为整数
# def fn(x, y):
#     return x * 10 + y


# print(reduce(fn, [1, 2, 6, 5, 3]))
# 字符串化为整数
# def fn(x, y):
#     return x * 10 + y
#
#
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}
#     return digits[s]


# print(char2num('5'))
# print(list(map(char2num, '12345')))
# print(reduce(fn, map(char2num, '1435')))
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
# def normalize(s):
#     return s[0].upper() + s[1:].lower()
#
#
# print(list(map(normalize, ['adam', 'LISA', 'barT'])))
#
#
# def normalize(s):
#     return s.title()  # title,首字母大写其余的小写。
#

# print(list(map(normalize, ['adam', 'LISA', 'barT'])))
# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
# filter()函数返回的是一个Iterator，也就是一个惰性序列，filter()完成计算结果，要用list()函数获得所有结果并返回list。
# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty,['A','',None,'B','C','  D   '])))
# 删除指定的字符strip()
# str = '    abc   '
# print(str.strip())
# str2 = '000abc000'
# print(str2.strip('0'))
# print(str2.lstrip('0'))
# print(str2.rstrip('0'))
# # 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
# def is_palindrome(n):
#     return n == int(str(n)[::-1])
# print(list(filter(is_palindrome,range(1,1000))))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55,
#                               66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')
# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？


# 假设我们用一组tuple表示学生名字和成绩：
# 请用sorted()对上述列表分别按名字排序：
# 请用sorted()对上述列表分别按分数排序：
# sorted(iterable,cmp(两个参数比较大小)，key(),reverse(True降序，默认值False升序))  四个参数默认时为None
# 返回值为列表
#
# L1=[-1,3,5,2,8,-9]
# # print(sorted(L1))
# # print(sorted(L1,key=abs))
# # L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# # print(sorted(L, key=lambda x: x[0]))
# # print(sorted(L, key=lambda x: x[1], reverse=True))
# lambda匿名函数有个限制，就是只能有一个表达式，不用写return，
# 返回值就是该表达式的结果匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
# L2 = list(filter(lambda n: n % 2 == 1, range(1, 20)))
# print(L2)
# f = lambda x: x * x
# print(f(6))
