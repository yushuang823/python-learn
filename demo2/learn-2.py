# 枚举类      把Student的gender属性改造为枚举类型，可以避免使用字符串：
from enum import Enum, unique


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name  # 姓名
        self.gender = gender  # 性别


# 测试:
if __name__ == '__main__':
    bart = Student('Bart', Gender.Male)
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')
    male1 = Student('BOB', Gender.Male)
    male2 = Student('BOB', Gender.Male)
    male3 = Student('BOB', Gender.Male)
    male4 = Student('BOB', Gender.Female)
    students = [male1, male2, male3, male4]

    for stu in students:
        if stu.gender == Gender.Male:
            print(stu.name, stu.gender.value)
            print(stu.name, stu.gender)
    print(Gender(0))