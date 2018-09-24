# namedtuple('名称', [属性list]):namedtuple是一个函数，
# 它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
if __name__ == '__main__':
    from collections import namedtuple, deque, defaultdict,OrderedDict,Counter

    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x)
    print(p.y)
    # 用坐标和半径表示一个圆，也可以用namedtuple定义：
    Circle = namedtuple('Circle', ['x', 'y', 'r'])
    p = Circle(2, 3, 5)
    print(p.x)
    print(p.y)
    print(p.r)
    # deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：这样就可以非常高效地往头部添加或删除元素。
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    print(q)
    # defaultdict使用dict时，如果引用的Key不存在，就会抛出KeyError。
    # 如果希望key不存在时，返回一个默认值，就可以用defaultdict：
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    print(dd)
    print(dd['key1'])
    print(dd['key2'])
    # OrderedDict 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
    # 如果要保持Key的顺序，可以用OrderedDict：
    d=dict([('a',1),('b',2),('c',3)])
    print(d)
    d2=OrderedDict([('a',1),('b',2),('c',3)])
    print(d2)
    # 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
    od=OrderedDict()
    od['x']=1
    od['y']=2
    od['z']=3
    print(list(od.keys()))

# Counter是一个简单的计数器，例如，统计字符出现的个数：Counter实际上也是dict的一个子类，
    c=Counter()
    for ch in 'students':
        c[ch]=c[ch]+1
    print(c)



