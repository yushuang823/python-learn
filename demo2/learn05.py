import time
import functools


    # 返回函数
    # 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
    # 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
#     def lazy_sum(*args):
#         def sum():
#             ax = 0
#             for n in args:
#                 ax = ax + n
#             return ax
#
#         return sum()
# f = lazy_sum(1, 3, 5, 7, 9)
# print(f)


# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#
#         fs.append(f)
#     return fs
#
#
# f1, f2, f3 = count()
#
# print(f1)
# print(f2)
# print(f3)
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）


#
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kwargs):
#         print('begin call')
#         time_begin = time.clock()
#         result = fn(*args, **kwargs) # 执行真正的逻辑
#         print('end call')
#         time_end = time.clock()
#         print('%s executed in %s ms' % (fn.__name__, time_end - time_begin))
#         return result
#
#     return wrapper
#
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     print('I am fast')
#     return x + y
#
# @metric
# def fast2(x, y):
#     time.sleep(0.5)
#     print('I am fast')
#     return x + y
#
#
# if __name__ == '__main__':
#
#     f = fast(11, 22)
#     if f != 33:
#        print('测试失败!')
# 偏函数 。。。。当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
# print(int('123'))     #默认是十进制
# print(int('123456',base=8))   #如果传入base参数，就可以做N进制的转换
# # functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
# import functools
# int2=functools.partial(int,base=2)
# print(int2('100001'))
# print(int2('10000000'))
# print(int2('10001',base=10))  #也可以在固定参数的情况下传入其他值
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def set_gender(self,gender):
        self.__gender =gender
    def get_gender(self):
        return self.__gender
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


