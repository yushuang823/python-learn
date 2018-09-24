# 定制类
# __str__  显示对象的属性  结构清晰 容易看清内部数据
# class Student(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#
#     __repr__ = __str__
# if __name__ == '__main__':
#     s=Student('jack')
#     print(s)
#     print(Student('BOB'))
# __iter__迭代  如果一个类想被用于for.....in循环就必须实现一个__iter__()方法，然后该方法返回一个迭代对象，
# 然后不断调用__next__()拿到循环的下一个值，直到遇到StopIteration 错误时退出循环。       for...in必须作用于可迭代对象
# class Fib:
#     def __init__(self):
#         self.a, self.b = 0, 1  # 初始化a,b
#
#     def __iter__(self):
#         return self  # 实例本身是可迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b  # 计算下一个值
#         if self.a > 100000:  # 退出循环条件
#             raise StopIteration
#         return self.a  # 返回下一个值


# if __name__ == '__main__':
# for n in Fib():  # 类作用于for循环
#     print(n)


# __getitem__  类获取元素
class Fib:
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    f = Fib()
    print(f[2])
    print(f[9])
    print(f[5])


# __getattr__     当调用不存在的属性时，解释器会自动调用__getattr__    动态返回一个属性
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        arg = '%s/%s' % (self._path, path)
        return Chain(arg)

    def __str__(self):
        return self._path

    __repr__ = __str__


if __name__ == '__main__':
    result = Chain().status.user.timeline.list
    print(result)
