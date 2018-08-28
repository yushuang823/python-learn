if __name__ == '__main__':
    pass
    # 关键字参数，name 和age是必选参数。关键字参数可以传入0个或者任意个，且在函数体内部自动形成一个字典dict
    def person(name, age, **kw):
        print('name:', name, 'age:', age, 'other:', kw)


    print(person('jack', 20))
    print(person('jane', 33, city='beijing', job='teacher'))
    dela = {'city': 'beijing', 'gender': 'male', 'job': 'teacher'}
    print(person('jack', 39, **dela))

    # 命名关键字参数
    # 检查关键字参数city,job是否在里面,但是仍然可以传入任意关键字参数
    def person(name, age, **kw):
        if 'city' in kw:
            pass
        if 'job' in kw:
            pass
        print('name:', name, 'age:', age, 'other:', kw)
    print(person('jack', 33, city='biejing', job='doctor', zipcode=123456))
    # 限制关键字参数的名字，只接受指定的关键字参数
    def person(name, age, *, city, job):
        print(name, age, city, job)


    print(person('jack', 22, city='shanghai', job='doctor'))

    # 如果已经定义了一个可变参数，则后面的命名关键字参数就不需要特殊符号分隔符*
    # 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
    # person()函数仅接受2个位置参数。
    def person(name, age, *args, city, job):
        print(name, age, args, city, job)

    print(person('jack', 22, 1, 3, 4, city='beijing', job='doctor'))
    # print(person('Jack', 24, 1, 1, 'Beijing', 'Engineer'))   #会报错，关键字参数名没有写
    # 命名关键字参数可以有缺省值
    def person(name,age,*,city='beijing',job):
        print(name,age,city,job)
    print(person('mick',12,job='doctor'))
    def person(name, age, city, job):
        pass                                 #person有两个位置参数
   # 缺少 *，city和job被视为位置参数

    # 参数组合    参数定义的顺序必须是：必选参数 默认参数 可变参数 命名关键字参数 关键字参数
    # 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
    def f1(a, b, c=0, *args, **kw):
        print(a, b, c, args, kw)


    def f2(a, b, c=0, *, d, **kw):
        print(a, b, c, d, kw)


    args = (1, 2, 3)
    kw = {'d': 'D', 'x': '#'}
    print(f1(*args, **kw))
    print(f2(*args, **kw))
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
L=[]
def the_input(number=eval(input('相乘总个数：') )):
    for i in range(number):
        n=eval(input('输入相乘个数：'))
        L.append(n)
    print(L)
the_input()
def product(*args):
    sum=1
    for n in args:
        sum=sum*n
    return sum
print('五个数相乘的总值是：',product(*L))








