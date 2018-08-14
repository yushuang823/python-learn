import copy
import random

from dateutil import parser

# if __name__ == '__main__':
    # print(format(3.145))
    # print(format(3.145, '0= 6'))
    # print(str(3.145).format('0=+10'))

    # Parse a string in one of the supported formats, using the ``parserinfo`` parameters.
    # 解析字符串到 datatime.datetime
    # dt = parser.parse("Aug 28 2015 12:00AM")
    # print(dt.year)
    # print(dt.day)
    # print(dt.month)
    # print(dt.hour)
    # print(dt.minute)
    # print(dt.second)
    # print(dt)

    # while break else
    #  i=0
    #  while i < 10:
    #      print(i)
    #      i += 2  # i = i+2
    #      if i == 6:
    #          break
    #  else:
    #      print(0)

    # print('aaa')
    # print('aaaaaa')
    # print('sqq\b\baaa')
    # print('sqq\faaa')
    # print('bbb')

    # 2是进制数base
    # print(int('11111',2))
    # num1=list(range(6))
    # print(num1[4])

    #
    # def func1():
    #     x = 5
    #     print(x)
    #
    # def func2():
    #     x += 1 # x = x+1
    #     print()
    #
    #
    # func1()
    # func2()
    # def demo(chars):
    #     word =""
    #     for c in chars:
    #         word+=c
    #         yield word
    # print(list(demo('abc')))

    # f0, f1, f2 = [lambda x: x * i for i in range(3)]  # [lambda x:x*0,]
    # for i in range(3):
    #     print(i)
    # print(random.sample(range(10),5))

    # a = [1, 2, ['a', 'b']] # a 有一个列表引用类型 A  =  ['a', 'b']， [1, 2, A]
    # b = a
    # c = copy.copy(a)   #浅克隆  [1, 2, A]
    # d = copy.deepcopy(a)    #深克隆  [1, 2, ['a', 'b']]
    # a.append(4) #  [1, 2,4， ['a', 'b']]
    # a[2].append('c') # a,b = [1, 2,4， ['a', 'b','c']] A  =  ['a', 'b','c']，c =  [1, 2, A]  = [1,2,['a','b','c']] d = [1, 2, ['a', 'b']]
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    # s = 'a\nb\tc'
    # print(len(s))

    # x = 1
    # y = 2
    # min = x if x < y else y  # min =  x if x<y = y 【条件为True时的结果】 if 【条件】 else 【条件为False时的结果】
    # max = x if x > y else y  # min =  x if x<y = y
    #
    # print(min)
    # print(max)
    # res=map(lambda x:x.upper(),['a','b','c'])
    # print(list(res))
   #  print(9%(5//2))
   #  print(5//2)
   #  print(9%2)
