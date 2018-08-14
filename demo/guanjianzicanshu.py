def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

if __name__ == '__main__':
    extra = {'city': 'beijing', 'job': 'teacher'}
    person('xiaoming', 12 , **extra)
