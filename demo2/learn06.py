# max2=functools.partial(max,10)
# print(max2(2,3,4,5))
import functools


# 1.定义一个student，包含姓名，性别，年龄，班级，成绩
# 2.成绩int 0～100
# 3.包含getScore（）用来返回成绩的int值
# 4.实现一个装饰器，用于3中的getScore（）成绩查询方法，用于讲数值型成绩转换为abcd四等

def get(func):
    def wrapper(*args, **kw):
        # print('call %s():' % func.__name__)
        result = func(*args, **kw)

        if result > 90 and result <= 100:
            return 'A'
        elif result > 80 and result <= 90:
            return 'B'
        elif result > 60 and result <= 80:
            return 'C'
        elif result <= 60:
            return 'D'
        return result

    return wrapper


def set(func):
    def wrapper(*args, **kw):
        # print('call %s():' % func.__name__)
        score = args[1]
        if 0 <= score and score <= 100:
            result = func(*args, **kw)
        else:
            raise ('成绩不合法 %d' % score)
        return result

    return wrapper


class Student(object):
    def __init__(self, name, gender, age, grade):
        self.name = name
        self.gender = gender
        self.age = age
        self.__score = -1
        self.grade = grade

    def set_score(self, score):
        if 0<= score and score <=100:
           self.__score = score
        else:
            #print('成绩不合法 ',score)
            raise Exception('成绩不合法 ',score) # raise 用于抛出异常类
    # @set
    # def set_score(self, score):
    #     self.__score = score

    @get
    def get_score(self):
        return self.__score


if __name__ == '__main__':
    std1 = Student('bob', 'male', 33, '二班')
    std1.set_score(880)
    print(std1.get_score())

