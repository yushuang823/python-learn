# IO编程
# #读写文件文本' r w a + u;
# if __name__ == '__main__':
#     # file = open('./test.txt','r',encoding='utf-8',errors='ignore')
#     # s = file.read()
#     # print(s)
#     with open('test.txt', 'w') as f:
#         f.write('abcv你哈')
#     with open('test.txt', 'r') as f:
#         s=f.read()
#         print(s)
# StringIO顾名思义就是在内存中读写str。首先使用StringIO 有两种模式：
# 第一种是StringIO()无参数 直接用write写进去 再用getvalue()读取str；
# 另外一种就是使用StringIO()里面有str内容然后使用readline()对函数内容进行读取
# from io import StringIO
# if __name__ == '__main__':
#      f=StringIO()
#      f.write('好好学习')
#      print(f.getvalue())
# from io import StringIO
# f=StringIO('好好学习\n天天向上\n加油赛！')
# while True:
#      content=f.readline()
#      if content=='':
#          break
#      print(content.strip())
# from io import StringIO
#
# f = StringIO('hello\nword\nzhong\nguo')
# for line in f.readlines():
#     print(line.strip())

# from io import BytesIO
# f=BytesIO()   #首先创建一个BytesIO()再写入
# f.write('你好'.encode('utf-8'))
# print(f.getvalue())    #getvalue()方法得到值

# if __name__ == '__main__':
#      from io import BytesIO
#      f=BytesIO(b'\xe7\x92\x87\xe7\x92\x87')  #也可以先用一个bytes初始化BytesIO然后再像文件一样读取
#      print(f.read())
from io import StringIO

file = StringIO("璇璇\n是一个\n好孩子！\n")
for line in file.readlines():
    print(line.strip())

from io import StringIO

file = StringIO('璇璇\n是一个\n好孩子！')
print(file.read())

from io import StringIO

file = StringIO("璇璇\n是一个\n好孩子！")
while True:
    content = file.readline()
    if content == '':
        break
    print(content.strip())
