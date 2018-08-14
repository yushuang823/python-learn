class Person(object):
    x = 1


class Name1(Person):
    pass


class Name2(Person):
    pass


Name1.x = 2
print(Name1.x)
Name2.x = 3
print(Name2.x)
Person.x = 4
print(Person.x)

if __name__ == '__main__':
    s = {'a', 'b'}
    print(type(s))
    print('i\'m ok')
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print(d.get('d', 0) + d.get('a', 2))
    print(('1', '2') * 2)
    print('1q2213dsa' * 2)
