class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'
    def get_score(self):
        return '%s: %s' %(self.name,self.score)
if __name__ == '__main__':
    f=Student('Bob',99)
    print(f.get_score())
    t=Student('Jack',66)
    print(t.get_grade())


# @property把方法变成属性， 广泛应用在类的定义中。
class Screen:
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an interger!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an interger!')
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width


# test:
if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')
