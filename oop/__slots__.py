
class Student(object):
    __slots__ = ('name', 'age') # Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

s = Student()
s.name = 'Bart Simpson'
s.age = 18
s.score = 59 # AttributeError
