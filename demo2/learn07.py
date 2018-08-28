
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
