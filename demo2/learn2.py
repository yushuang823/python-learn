import math

if __name__ == '__main__':
    pass
    def abs(x):
        if x > 0:
            return x
        else:
            return -x

    print(abs(-5))
    def my_abs(x):
        if not isinstance(x, (int, float)):
            raise TypeError('bad operand type')
        if x >= 0:
            return x
        else:
            return -x


    print(my_abs(-9))
    # print(my_abs('S'))

def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print(move(100, 100, 60, math.pi / 6))
# 返回一元二次方程的两个解
import math


def quadratic(a, b, c):
    if a == 0:
        raise TypeError('a!=0')
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('Bad operand type')
    delta = math.pow(b, 2) - 4 * a * c
    if delta < 0:
        return '无实根'
    x1 = (math.sqrt(delta) - b) / (2 * a)
    x2 = -(math.sqrt(delta) + b) / (2 * a)
    return x1, x2



a = input("请输入a")
b = input("请输入b")
c = input("请输入c")

print(quadratic(9, 12, 4))
# 默认参数必须是不变对象
def add_end(L=[]):
    L.append('END')
    return L


print(add_end([1, 2, 3]))
print(add_end(['asd','as']))
print(add_end())


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())
print(add_end())
# 可变参数  numbers 只接受元组  且可接受任意多个参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3, 4))
print(calc(3, 4, 5, 6))
# 若本身有一个元组或者列表
nums = [1, 4, 6, 7]
print(calc(*nums))
